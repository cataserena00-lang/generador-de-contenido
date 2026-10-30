# Código del pipeline (Python y deploy)

Código fuente concatenado. Los secretos están ocultos como `***OCULTO***`.

## tools/build.py

~~~~python
"""Arma salida/<fecha>/tablero.html a partir de entrada/<fecha>/ (autocontenido).

Uso:  python tools/build.py 2026-10-27
Lee:  entrada/<fecha>/parte.json, docs/*.txt, fotos/*.jpg|png
      data/circuitos.json, data/fiscal.json, assets/marca/*.svg, assets/fuentes/*.ttf
Fotos: se toman por la clave 'doc' de cada obra (<doc>_1.jpg, <doc>_2.jpg...).
       Una foto manual llamada <id-obra>.jpg (o <id-obra>_N.jpg) tiene prioridad.
"""
import base64, glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1] if len(sys.argv) > 1 else sorted(os.listdir(os.path.join(ROOT, "entrada")))[-1]
IN = os.path.join(ROOT, "entrada", fecha)
OUT = os.path.join(ROOT, "salida", fecha)
os.makedirs(OUT, exist_ok=True)

rd = lambda p: open(p, encoding="utf-8").read()
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
mime = lambda p: "image/png" if p.lower().endswith(".png") else "image/jpeg"

parte = json.load(open(os.path.join(IN, "parte.json"), encoding="utf-8"))
circuitos = json.load(open(os.path.join(ROOT, "data", "circuitos.json"), encoding="utf-8"))["circuitos"]
fiscal = json.load(open(os.path.join(ROOT, "data", "fiscal.json"), encoding="utf-8"))
_cp = os.path.join(IN, "contenido.json")   # piezas redactadas a mano para el día (generales, periódicos, por tipo)
contenido = json.load(open(_cp, encoding="utf-8")) if os.path.exists(_cp) else {}

svg = {os.path.basename(p)[:-4]: rd(p) for p in glob.glob(os.path.join(ROOT, "assets", "marca", "*.svg")) if not os.path.basename(p).startswith("_")}

CACHE = os.path.join(ROOT, "entrada", "_cache")  # docs y fotos bajados de Drive (los comparten todos los días)

def fotos_de(key):
    for base in (IN, CACHE):   # una foto suelta en la carpeta del día pisa la de Drive
        ps = sorted(glob.glob(os.path.join(base, "fotos", key + "_*.*")) + glob.glob(os.path.join(base, "fotos", key + ".*")))
        if ps:
            return [liviana(p) for p in ps]
    return []

def liviana(p, lado=1500, calidad=80):
    """Reduce la foto (máx. 1500 px de lado, JPEG) para que el tablero siga pesando < 10 MB."""
    import warnings; warnings.filterwarnings("ignore")
    import pymupdf
    pg = pymupdf.open(p)[0]
    z = min(1.0, lado / max(pg.rect.width, pg.rect.height))
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=False)
    return "data:image/jpeg;base64," + base64.b64encode(pix.tobytes("jpeg", jpg_quality=calidad)).decode()

fotos, docs = {}, {}
for o in parte["obras"]:
    manual = fotos_de(o["id"])
    key = o.get("doc")
    if manual:
        fotos[o["id"]] = manual
        o["doc_foto"] = o["id"]
    if key:
        fotos.setdefault(key, fotos_de(key))
        for base in (IN, CACHE):
            p = os.path.join(base, "docs", key + ".txt")
            if os.path.exists(p):
                docs[key] = rd(p).strip()
                break
    if manual:  # la clave de foto pasa a ser el id de la obra
        o["doc_orig"], o["doc"] = key, o["id"]
        if key and key in docs:
            docs[o["id"]] = docs[key]

fuentes = ""
for w, name in ((900, "Black"), (800, "ExtraBold"), (700, "Bold"), (600, "SemiBold")):  # UI: Bold/Black (manual); placas: ExtraBold/SemiBold (carteles)
    p = os.path.join(ROOT, "assets", "fuentes", f"Poppins-{name}.ttf")
    fuentes += f"@font-face{{font-family:Poppins;font-weight:{w};src:url(data:font/ttf;base64,{b64(p)}) format('truetype')}}\n"

# histórico: todos los partes guardados en entrada/<fecha>/parte.json (alimenta los contenidos periódicos)
hist = []
for d in sorted(os.listdir(os.path.join(ROOT, "entrada"))):
    p = os.path.join(ROOT, "entrada", d, "parte.json")
    if not d.startswith("_") and d <= fecha and os.path.exists(p):
        j = json.load(open(p, encoding="utf-8"))
        act = [o for o in j["obras"] if not o.get("grupo") and o.get("estado", "ejecucion") == "ejecucion"]
        # Una esquina con varias rampas es UNA obra. Hasta el 22/10 el encabezado del parte contaba cada rampa por separado,
        # así que "en ejecución" se toma de los ítems del parte y no del encabezado, para que toda la serie use el mismo criterio.
        hist.append(dict(fecha=d, enEjecucion=len(act), finalizadas=None, puestos=j["puestos"], ids=[o["id"] for o in act]))

data = dict(parte=parte, circuitos=circuitos, fiscal=fiscal, contenido=contenido, hist=hist, assets=dict(svg=svg, fotos=fotos, docs=docs))
html = rd(os.path.join(ROOT, "tools", "plantilla.html"))
html = html.replace("/*__FONTS__*/", fuentes).replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
dst = os.path.join(OUT, "tablero.html")
open(dst, "w", encoding="utf-8").write(html)
pub = os.path.join(ROOT, "deploy")  # copia lista para publicar (ver deploy/LEEME.md)
os.makedirs(pub, exist_ok=True)
open(os.path.join(pub, "index.html"), "w", encoding="utf-8").write(html)
print(f"{dst}  {os.path.getsize(dst)/1e6:.1f} MB  obras={len(parte['obras'])}  con foto={sum(1 for o in parte['obras'] if fotos.get(o.get('doc')))}")
~~~~

## tools/fetch_docs.py

~~~~python
"""Baja los Google Docs que aparecen en entrada/<fecha>/lista.txt (texto y fotos) a entrada/_cache.

Uso:  python tools/fetch_docs.py 2026-10-28
Los docs tienen que estar compartidos con "cualquiera con el enlace". Lo ya bajado no se vuelve a bajar.
"""
import html, json, os, re, sys, urllib.request, zipfile, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1]
lista = open(os.path.join(ROOT, "entrada", fecha, "lista.txt"), encoding="utf-8").read()
CACHE = os.path.join(ROOT, "entrada", "_cache")
os.makedirs(os.path.join(CACHE, "docs"), exist_ok=True)
os.makedirs(os.path.join(CACHE, "fotos"), exist_ok=True)
dpath = os.path.join(ROOT, "data", "docs.json")
docs = json.load(open(dpath, encoding="utf-8"))

ids = sorted(set(re.findall(r"docs\.google\.com/document/d/([\w-]+)", lista)))
for i in ids:
    key = docs.setdefault(i, "d_" + re.sub(r"\W", "", i[:8]).lower())
    if os.path.exists(os.path.join(CACHE, "docs", key + ".txt")):
        print(f"ok    {key} (ya estaba)")
        continue
    try:
        req = urllib.request.Request(f"https://docs.google.com/document/d/{i}/export?format=docx", headers={"User-Agent": "Mozilla/5.0"})
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req, timeout=60).read()))
    except Exception as e:
        print(f"FALLA {key}: {e}  (¿el doc está compartido con 'cualquiera con el enlace'?)")
        continue
    x = z.read("word/document.xml").decode("utf8")
    paras = [re.sub(r"<[^>]+>", "", p) for p in re.findall(r"<w:p[ >].*?</w:p>", x, flags=re.S)]
    open(os.path.join(CACHE, "docs", key + ".txt"), "w", encoding="utf-8").write("\n".join(html.unescape(p) for p in paras).strip())
    ms = [n for n in z.namelist() if n.startswith("word/media/")]
    for n_, n in enumerate(ms, 1):
        open(os.path.join(CACHE, "fotos", f"{key}_{n_}{os.path.splitext(n)[1]}"), "wb").write(z.read(n))
    print(f"baja  {key}: {len(ms)} fotos")
json.dump(docs, open(dpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
~~~~

## tools/parse_lista.py

~~~~python
"""Convierte entrada/<fecha>/lista.txt (la "LISTA DE DIFUSIÓN") en entrada/<fecha>/parte.json.

Uso:  python tools/parse_lista.py 2026-10-28
Aplica las reglas de data/reglas_parte.md (rubro, calle y entre-calles, barrio, circuito).
"""
import datetime, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: json.load(open(os.path.join(ROOT, p), encoding="utf-8"))
fecha = sys.argv[1]
INP = os.path.join(ROOT, "entrada", fecha)
CACHE = os.path.join(ROOT, "entrada", "_cache")
txt = open(os.path.join(INP, "lista.txt"), encoding="utf-8").read().replace(" ", " ").replace("\t", " ")

CIRC = rd("data/circuitos.json")["circuitos"]
DOCS = rd("data/docs.json")
MEMO = rd("data/memorias.json")
FIN = rd("data/finalizadas.json")
TABLA_P = os.path.join(ROOT, "data", "barrio_circuito.json")
TABLA = json.load(open(TABLA_P, encoding="utf-8")) if os.path.exists(TABLA_P) else {}

def quitar_tildes(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
def norm(s): return re.sub(r"\s+", " ", quitar_tildes(s).lower()).strip()
def slug(s): return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-")[:50]
CHICAS = {"de", "del", "la", "las", "los", "y", "e", "el", "en", "con", "a", "al"}
CORR = {"Industial": "Industrial", "Rio": "Río", "Olayon": "Olayón", "Andres": "Andrés", "Jardin": "Jardín", "Cordoba": "Córdoba", "Hector": "Héctor", "Menendez": "Menéndez",
        "Jose": "José", "Guemes": "Güemes", "Ombu": "Ombú", "Aeronautico": "Aeronáutico", "Platanos": "Plátanos", "America": "América", "Maria": "María",
        "Adrian": "Adrián", "Gaston": "Gastón", "Nicolas": "Nicolás", "Malbran": "Malbrán", "Hipolito": "Hipólito", "Escolastico": "Escolástico",
        "Magan": "Magán", "Velez": "Vélez", "Geronimo": "Gerónimo", "Fermin": "Fermín", "Martinez": "Martínez", "Arguello": "Argüello", "Paraiso": "Paraíso",
        "Tristan": "Tristán", "Raul": "Raúl", "Cesar": "César", "Cañada": "Cañada", "Dean": "Deán", "Rincon": "Rincón", "Simon": "Simón", "Galvez": "Gálvez"}
def tc(s):  # mayúscula inicial en palabras en minúscula o todas en mayúscula; respeta el resto; repone tildes frecuentes
    out = []
    for i, w in enumerate(s.split()):
        if re.fullmatch(r"\(\w\)", w): out.append(w.upper()); continue
        if w.lower() in CHICAS and i and (w.isupper() or w.islower()): out.append(w.lower()); continue
        if (w.isupper() and len(w) > 2 and w not in ("IPV", "EPEC", "UPC")) or w.islower():
            w = w[:1].upper() + w[1:].lower()
        out.append(CORR.get(w, w))
    return " ".join(out)
def limpiar(s): return re.sub(r"\s+", " ", s).strip(" .,-–·")

# ---------- encabezado ----------
puestos = int(re.search(r"Puestos de trabajos?\s+directos\s+(\d+)", txt, re.I).group(1))
enej = int(re.search(r"OBRAS EN EJECUCI[ÓO]N\s+(\d+)", txt, re.I).group(1))

# ---------- rubros ----------
RUBROS = {"MANTENIMIENTO DE CALLES": "mant", "BACHEO EN FRIO": "frio", "RAMPAS": "rampas", "BACHEO CON ASFALTO": "bacheo",
          "REHABILITACION CON ASFALTO": "rehab", "REHABILITACION Y BACHEO CON HORMIGON": "hormigon", "PAVIMENTACION": "pav"}
def rubro_de(l):
    n = norm(l).upper()
    if n.startswith("PLAZAS"): return "plaza"
    return RUBROS.get(n)

OBRAS = []
items, rubro, estado = [], None, "ejecucion"
for raw in txt.splitlines():
    l = raw.strip().lstrip("•●").strip()
    if not l or re.match(r"LISTA DE DIFUSI", l, re.I) or re.match(r"(Puestos de trabajos?|OBRAS EN EJECUCI)", l, re.I): continue
    r = rubro_de(l)
    if r: rubro, estado = r, "ejecucion"; continue
    n = norm(l).upper()
    if n in ("EN EJECUCION",): estado = "ejecucion"; continue
    if n in ("TERMINADAS", "FINALIZADAS"): estado = "terminada"; continue
    if rubro is None: continue
    solo_link = re.fullmatch(r"https?://\S+", l)
    num = re.match(r"^(\d+)[\.\)]\s*(.*)$", l)
    es_rampa = rubro == "rampas" and re.search(r"·\s*\d+\s*rampa", l)
    if solo_link:
        if items: items[-1]["links"].append(l)
    elif num or es_rampa:
        items.append(dict(rubro=rubro, estado=estado, texto=(num.group(2) if num and not es_rampa else l), links=[]))
        if es_rampa and num and re.match(r"^\d+[\.\)]", l): items[-1]["texto"] = num.group(2)
    elif items and rubro != "rampas" and items[-1]["rubro"] == rubro:
        items[-1]["texto"] += " " + l           # continuación de la línea anterior (BARRIO:… en el renglón de abajo)

# ---------- lectura de cada ítem ----------
def corregir_pueyrredon(s): return re.sub(r"Av\.?\s*J[:.]?\s*M+\.?\s*de Pueyrred[oó]n", "Av. J. M. de Pueyrredón", s, flags=re.I)
def leer(it):
    t = it["texto"]
    it["links"] += re.findall(r"https?://\S+", t)
    t = re.sub(r"https?://\S+", " ", t)
    nota = []
    if re.search(r"\(?\s*nocturno\s*\)?", t, re.I): nota.append("Nocturno"); t = re.sub(r"\(?\s*nocturno\s*\)?", " ", t, flags=re.I)
    m = re.search(r"\(?\s*(\d+)\s*(?:da|ra|ta|º|°)?\s*intervenci[oó]n\s*\)?", t, re.I)
    if m: nota.append(f"{m.group(1)}.ª intervención"); t = t.replace(m.group(0), " ")
    m = re.search(r"-?\s*(\d+)\s*(?:er|ra|da|ta)?\s*etapa\b", t, re.I)
    if m and not re.search(r"etapa\s+(ii|2)", m.group(0), re.I): nota.append(f"{m.group(1)}.ª etapa"); t = t.replace(m.group(0), " ")
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\s+zz\s*$", "", t, flags=re.I)                    # basura al final del renglón
    t = re.sub(r"(?<=\d)\s*ª\s*$", "A", t)                         # "-6ª" = circuito 6A
    code = None
    m = re.search(r"[-–]\s*0?(\d{1,2}[A-Za-z]?)\s*$", t)
    if m: code = m.group(1).upper(); t = t[:m.start()]
    elif re.search(r"[-–]\s*$", t): code = "heredar"; t = re.sub(r"[-–]\s*$", "", t)
    d = dict(tipo=it["rubro"], estado=it["estado"], links=it["links"], nota=nota, codigo=code, rampas=None, barrio=None, via=None, entre=None, sector=None, orden=len(OBRAS))
    if it["rubro"] == "rampas":
        c = re.search(r"(\d+)\s*rampa", t); d["rampas"] = int(c.group(1))
        esq = corregir_pueyrredon(t.split("·")[0]); esq = re.sub(r"\s+x\s+", " y ", esq); esq = re.sub(r"\s+y\s*\.?\s*$", "", esq)
        d["via"] = tc(limpiar(esq)); d["nota"] = [f"{c.group(1)} {'rampa' if c.group(1)=='1' else 'rampas'}"]
        d["codigo"] = "10G" if "Pueyrred" in d["via"] else "1"      # las rampas de este parte son siempre de dos zonas
        return d
    b = re.split(r"\bb(?:arrio)?\s*:\s*", t, maxsplit=1, flags=re.I)
    calle, barrio = (b[0], b[1]) if len(b) == 2 else (t, None)
    if barrio: barrio = re.sub(r"^(?:b(?:arrio)?\s*:\s*)+", "", re.sub(r"^b[°º]\s*", "", barrio.strip(), flags=re.I), flags=re.I).strip()
    if d["tipo"] in ("mant", "frio", "pav", "plaza") and not barrio and not re.search(r"\b(e/|entre)\b", calle, re.I):
        pass
    if d["tipo"] == "plaza":
        nombre = re.sub(r"^\s*(?:\d+´\s*/?\s*(?:\d+)?\s*)", "", calle)
        nombre = re.sub(r"^\s*plaza\s*/?\s*", "", nombre.replace("/", " "), flags=re.I)
        d["via"] = "Plaza " + tc(limpiar(nombre))
    elif d["tipo"] in ("bacheo", "rehab", "hormigon"):
        calle = re.sub(r"\s+", " ", calle)
        m = re.search(r"\s(?:e/\s*|entre\s+|e\s+)", calle)
        via, entre = (calle[:m.start()], calle[m.end():]) if m else (calle, None)
        entre = re.sub(r"N°\s*", "", entre) if entre else entre
        d["via"], d["entre"] = tc(limpiar(via)), (tc(limpiar(entre)) if entre else None)
    else:  # mant, frio, pav: la línea completa es el nombre (y el barrio)
        s = re.sub(r"^\s*B[°º]?\s+", "", calle.strip())
        d["sector"] = tc(limpiar(s))
        if d["tipo"] in ("mant", "frio") and not re.search(r"\b(e/|entre)\b", calle, re.I): barrio = d["sector"]
    d["barrio"] = tc(limpiar(barrio)) if barrio else None
    if d["tipo"] == "pav":
        for k, v in MEMO.items():
            if k.startswith("_"): continue
            if norm(d["sector"]).startswith(k): d["sector"], d["memoria"] = v["sector"], v
    return d

OBRAS = []
for it in items:
    OBRAS.append(leer(it))

# plazas: el parte las nombra a veces distinto o las repite; se unifican para no contarlas dos veces
PLAZA_ALIAS = {"plaza luis galeano": "Plaza Pedro Luis Galeano", "plaza barrios unidos": "Plaza Centro América"}   # mismas plazas con otro nombre en el parte
vistas, filtradas = set(), []
for o in OBRAS:
    if o["tipo"] == "plaza":
        o["via"] = PLAZA_ALIAS.get(norm(o["via"]), o["via"])
        if slug(o["via"]) in vistas: continue
        vistas.add(slug(o["via"]))
    filtradas.append(o)
OBRAS = filtradas

# ---------- rampas sin código heredan de la anterior ----------
prev = None
for o in OBRAS:
    if o["tipo"] == "rampas":
        if o["codigo"] == "heredar": o["codigo"], o["circ_inferido"] = prev, True
        prev = o["codigo"]

# ---------- barrio: grafía única por barrio normalizado ----------
vistos = {}
for o in OBRAS:
    if o["barrio"]:
        k = norm(re.sub(r"\s*etapa\s*ii$", "", o["barrio"]))
        k = re.sub(r"^(el|la|los|las)\s+", "", k)
        o["barrio"] = vistos.setdefault(k, o["barrio"])

# ---------- circuito y barrio inferidos ----------
def bkey(b): return re.sub(r"^(el|la|los|las)\s+", "", norm(re.sub(r"\s*etapa\s*ii$", "", re.sub(r"^b[°º]\s*", "", b, flags=re.I))))
por_codigo = {}
for o in OBRAS:
    if o["codigo"] and o["barrio"] and o["tipo"] != "rampas": por_codigo.setdefault(o["codigo"], o["barrio"])
por_barrio = {}
for o in OBRAS:
    if o["codigo"] and o["barrio"]: por_barrio.setdefault(bkey(o["barrio"]), o["codigo"])
avisos_rev = []
for o in OBRAS:
    o["barrio_inferido"] = None
    if o["tipo"] == "rampas": continue                               # nunca se infiere barrio en rampas
    if o["tipo"] == "pav" and not o["barrio"] and o.get("memoria"):  # ajuste propio: el barrio de la memoria va antes que inferir por código
        o["barrio"], o["barrio_inferido"] = o["memoria"].get("barrio") or o["sector"], "memoria"
    if not o["barrio"] and o["codigo"] and o["codigo"] in por_codigo:
        o["barrio"], o["barrio_inferido"] = por_codigo[o["codigo"]], "codigo"
    if not o["codigo"]:
        if o["barrio"] and bkey(o["barrio"]) in por_barrio: o["codigo"], o["circ_inferido"] = por_barrio[bkey(o["barrio"])], True
        elif o["barrio"] and bkey(o["barrio"]) in TABLA: o["codigo"], o["circ_inferido"] = TABLA[bkey(o["barrio"])], True
        elif o.get("memoria"): o["codigo"], o["circ_inferido"] = o["memoria"]["circuito"], True
    if o["codigo"] and o["codigo"] not in CIRC and o["codigo"] != "?":
        avisos_rev.append(f"Código {o['codigo']} sin circuito registrado en data/circuitos.json ({o.get('via') or o.get('sector')}): revisar.")

# ---------- ids, docs y métricas ----------
def doc_id(url):
    m = re.search(r"docs\.google\.com/document/d/([\w-]+)", url); return m.group(1) if m else None
def texto_doc(key):
    p = os.path.join(CACHE, "docs", key + ".txt"); return open(p, encoding="utf-8").read() if os.path.exists(p) else None
usos = {}
for o in OBRAS:
    ids = [doc_id(u) for u in o["links"] if doc_id(u)]
    o["doc_key"] = DOCS.get(ids[0], "d_" + ids[0][:8].lower()) if ids else None
    o["doc_url"] = next((u for u in o["links"] if doc_id(u)), None)
    if o["doc_key"]: usos[o["doc_key"]] = usos.get(o["doc_key"], 0) + 1
ids_count = {}
out = []
grupos = {"1": dict(rampas=0, esquinas=0, doc="rampas_centro"), "10G": dict(rampas=0, esquinas=0, doc="rampas_pueyrredon")}
for o in OBRAS:
    base = slug(o["via"] or o["sector"])
    base_id = f"{o['tipo']}_{base}"
    n = ids_count.get(base_id, 0); ids_count[base_id] = n + 1
    oid = base_id if n == 0 else base_id + "_" + (slug(o["entre"]) if o["entre"] else str(n + 1))
    met = {}
    if o["doc_url"]: met["driveUrl"] = o["doc_url"]
    if "Nocturno" in o["nota"]: met["nocturno"] = True
    if o["tipo"] == "pav" and o.get("memoria"): met["cuadras"], met["plazo"] = o["memoria"]["cuadras"], o["memoria"]["plazo"]
    key = o["doc_key"]
    if o["tipo"] == "pav" and o.get("memoria"): key = key or o["memoria"]["memoria"]
    if o["tipo"] == "rampas":
        g = grupos[o["codigo"]]; g["rampas"] += o["rampas"]; g["esquinas"] += 1; key = None
    elif key and texto_doc(key):
        t = texto_doc(key); tn = norm(t)
        ok = usos.get(o["doc_key"], 1) == 1 or bool(o["entre"] and norm(o["entre"]) in tn)   # un doc compartido solo vale para el tramo que nombra
        if ok:
            m2 = {int(x.replace(".", "")) for x in re.findall(r"(\d[\d\.]*)\s*m(?:²|2)\b", t)}
            ml = {int(x.replace(".", "")) for x in re.findall(r"(\d[\d\.]*)\s*metros\s+lineales", t)}
            if len(m2) == 1: met["m2"] = m2.pop()
            if len(ml) == 1: met["ml"] = ml.pop()
    if o["tipo"] == "plaza" or o["estado"] == "terminada": pass
    out.append(dict(id=oid, circuito=o["codigo"] or "?", tipo=o["tipo"], via=o["via"], entre=o["entre"], sector=o["sector"], barrio=o["barrio"],
                    rampas=o["rampas"], doc=key, grupo=False, estado=o["estado"], nota=o["nota"], barrio_inferido=o["barrio_inferido"],
                    circ_inferido=bool(o.get("circ_inferido")), metricas=met))
# grupos de rampas (placa y texto de conjunto)
for c, g in grupos.items():
    if not g["esquinas"]: continue
    via = "Zona céntrica · %d esquinas" % g["esquinas"] if c == "1" else "Av. J. M. de Pueyrredón · %d esquinas" % g["esquinas"]
    link = next((u for o in OBRAS if o["tipo"] == "rampas" and o["codigo"] == c for u in o["links"] if doc_id(u)), None)
    out.append(dict(id="rampas_grupo_" + ("centro" if c == "1" else "pueyrredon"), circuito=c, tipo="rampas", via=via, entre=None, sector=None, barrio=None,
                    rampas=g["rampas"], doc=g["doc"], grupo=True, estado="ejecucion", nota=[], barrio_inferido=None, circ_inferido=False,
                    metricas=dict(esquinas=g["esquinas"], **({"driveUrl": link} if link else {}))))

# ---------- tabla barrio -> circuito (el código del parte gana; sin letra no pisa uno con letra) ----------
for o in OBRAS:
    if o["barrio"] and o["codigo"] and o["codigo"] in CIRC and not o.get("circ_inferido") and o["tipo"] != "rampas":
        k = bkey(o["barrio"]); viejo = TABLA.get(k)
        if viejo is None or not (re.fullmatch(r"\d+", o["codigo"]) and re.search(r"[A-Z]$", viejo)): TABLA[k] = o["codigo"]
json.dump(TABLA, open(TABLA_P, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)

d = datetime.date.fromisoformat(fecha)
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
reales = [o for o in out if not o["grupo"] and o["estado"] == "ejecucion"]
parte = dict(fecha=fecha, fecha_texto=f"{dias[d.weekday()]} {d.day} de {meses[d.month-1]} de {d.year}", enEjecucion=enej, puestos=puestos,
             finalizadas=next((FIN[k] for k in sorted((k for k in FIN if not k.startswith("_") and k <= fecha), reverse=True)), None), acumulados=dict(cuadras_pavimentadas=1100, rampas_programa=2100),
             programaRampas=dict(total=2100, nuevas=2000, en_esquinas_sin_rampa=1317, reparadas=100, fuente="Doc Drive 'Córdoba Accesible: 2.100 rampas para una ciudad más inclusiva'"),
             avisos=rd("data/avisos.json")["avisos"] + avisos_rev, obras=out)
json.dump(parte, open(os.path.join(INP, "parte.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
por_tipo = {}
for o in reales: por_tipo[o["tipo"]] = por_tipo.get(o["tipo"], 0) + 1
print(f"{fecha}: {len(reales)} obras leídas (encabezado dice {enej}) · puestos {puestos} · {por_tipo}")
if len(reales) != enej: print(f"   AVISO: el encabezado dice {enej} y se leyeron {len(reales)}")
sin = [o["via"] or o["sector"] for o in reales if o["circuito"] == "?"]
if sin: print("   sin circuito:", sin)
inf = [(o["via"] or o["sector"], o["barrio"], o["barrio_inferido"]) for o in reales if o["barrio_inferido"]]
if inf: print("   barrio inferido:", inf)
~~~~

## deploy/middleware.js

~~~~javascript
// Acceso por usuario y contraseña (HTTP Basic) validado en el servidor.
// Las credenciales viven en variables de entorno de Vercel (TABLERO_USUARIO / TABLERO_CLAVE),
// nunca en el HTML. Si no están cargadas, el sitio queda cerrado.
export const config = { matcher: '/(.*)' };

const cerrado = (status, headers = {}) =>
  new Response(status === 503 ? 'Sitio no configurado.' : 'Acceso restringido.', {
    status,
    headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store', ...headers },
  });

function igual(a, b) {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

export default function middleware(request) {
  const user = process.env.TABLERO_USUARIO;
  const pass = process.env.TABLERO_CLAVE;
  if (!user || !pass) return cerrado(503);

  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    try {
      const dec = new TextDecoder().decode(Uint8Array.from(atob(auth.slice(6)), c => c.charCodeAt(0)));
      const i = dec.indexOf(':');
      if (i > -1 && igual(dec.slice(0, i), user) && igual(dec.slice(i + 1), pass)) {
        return new Response(null, { headers: { 'x-middleware-next': '1' } });
      }
    } catch (_) { /* credencial mal formada */ }
  }
  return cerrado(401, { 'www-authenticate': 'Basic realm="Tablero de obras", charset="UTF-8"' });
}
~~~~

## deploy/vercel.json

~~~~json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Robots-Tag", "value": "noindex, nofollow, noarchive" },
        { "key": "Cache-Control", "value": "private, no-store" },
        { "key": "X-Frame-Options", "value": "DENY" }
      ]
    }
  ]
}
~~~~

## .claude/launch.json

~~~~json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "tablero",
      "runtimeExecutable": "python",
      "runtimeArgs": ["-m", "http.server", "8123", "--directory", "salida"],
      "port": 8123
    }
  ]
}
~~~~
