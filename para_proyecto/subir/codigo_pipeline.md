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
Galería: assets/galeria/<clave_rubro>/*.jpg|png (claves de TIPOS: mant, frio, rampas, bacheo, rehab, hormigon, pav, plaza).
       Fotos genéricas por tipo de obra; se usan en la placa cuando la obra no trae foto del parte.
       No van dentro del tablero: se escriben en deploy/galeria/ y salida/<fecha>/galeria/ (rutas relativas).
       Para sumar fotos: soltarlas en la carpeta del rubro y volver a correr este build.
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

def liviana(p, lado=1500, calidad=80, por_pixel=False, crudo=False):
    """Reduce la foto (máx. 1500 px de lado, JPEG) para que el tablero siga pesando < 10 MB.
    por_pixel: mide en píxeles reales (una PNG de 96 dpi no se achica de más). Lo usa la galería; las fotos del parte siguen igual.
    crudo: devuelve los bytes del JPEG en lugar del dataURL (la galería se escribe como archivos sueltos)."""
    import warnings; warnings.filterwarnings("ignore")
    import pymupdf
    pg = pymupdf.open(p)[0]
    k = 1.0
    if por_pixel:
        px = pymupdf.Pixmap(p)
        k = px.width / pg.rect.width   # píxeles por punto
        px = None
    z = min(k, lado / max(pg.rect.width, pg.rect.height))
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=False)
    jpg = pix.tobytes("jpeg", jpg_quality=calidad)
    return jpg if crudo else "data:image/jpeg;base64," + base64.b64encode(jpg).decode()

GAL_DIR = os.path.join(ROOT, "assets", "galeria")
GAL_EXT = (".jpg", ".jpeg", ".png", ".webp")

GAL_OUT = "galeria"   # carpeta de la galería al lado del tablero: deploy/galeria/ y salida/<fecha>/galeria/
MARCA_RAIZ = "_copia_de_deploy_galeria.txt"  # marca que identifica <raíz>/galeria/ como copia generada (solo esa se borra)

def galeria():
    """La galería NO viaja dentro del tablero: cada foto de assets/galeria/<rubro>/ se recomprime a 990 px de lado máximo
    (su tamaño real), JPEG calidad 75, y se escribe en deploy/galeria/<rubro>/<nombre>.jpg; también se copia a salida/<fecha>/galeria/.
    Cada build borra antes esas carpetas para que no queden fotos viejas.
    Devuelve {rubro: [{src: 'galeria/<rubro>/<nombre>.jpg', nombre: archivo original}, ...]}, con rutas relativas al tablero, por nombre de archivo."""
    import shutil
    destinos = [os.path.join(ROOT, "deploy", GAL_OUT), os.path.join(OUT, GAL_OUT)]
    for dst in destinos:
        if os.path.isdir(dst):
            shutil.rmtree(dst)
    out = {}
    if not os.path.isdir(GAL_DIR):
        return out
    for rubro in sorted(os.listdir(GAL_DIR)):
        d = os.path.join(GAL_DIR, rubro)
        if not os.path.isdir(d) or rubro.startswith((".", "_")):
            continue
        fs, usados = [], set()
        for nombre in sorted(os.listdir(d), key=str.lower):
            if not nombre.lower().endswith(GAL_EXT) or nombre.startswith((".", "_")):
                continue
            arch = os.path.splitext(nombre)[0] + ".jpg"
            if arch.lower() in usados:
                print(f"  galería: {rubro}/{nombre} se saltea (ya hay otra foto que se llama {arch})")
                continue
            try:
                jpg = liviana(os.path.join(d, nombre), lado=990, calidad=75, por_pixel=True, crudo=True)
            except Exception as e:
                print(f"  galería: no se pudo leer {rubro}/{nombre} ({e})")
                continue
            usados.add(arch.lower())
            for dst in destinos:
                os.makedirs(os.path.join(dst, rubro), exist_ok=True)
                open(os.path.join(dst, rubro, arch), "wb").write(jpg)
            fs.append(dict(src=f"{GAL_OUT}/{rubro}/{arch}", nombre=nombre))
        out[rubro] = fs
    return out

def galeria_a_raiz():
    """Copia deploy/galeria/ a <raíz>/galeria/, como las copias de index.html y anuncios.html: la raíz y deploy/ van siempre iguales
    (no sabemos todavía cuál publica Vercel). Borra la copia anterior solo si tiene la marca: así nunca se borran fotos subidas a mano."""
    import shutil
    src, dst = os.path.join(ROOT, "deploy", GAL_OUT), os.path.join(ROOT, GAL_OUT)
    if os.path.isdir(dst):
        if not os.path.exists(os.path.join(dst, MARCA_RAIZ)):
            print(f"AVISO: {GAL_OUT}/ en la raíz no es una copia del build (falta {MARCA_RAIZ}); no se toca. Si son fotos originales, moverlas a assets/galeria/.")
            return
        shutil.rmtree(dst)
    if os.path.isdir(src):
        shutil.copytree(src, dst)
        open(os.path.join(dst, MARCA_RAIZ), "w", encoding="utf-8").write(
            "Copia generada por tools/build.py desde deploy/galeria/. No editar: se borra y se vuelve a escribir en cada build.\n"
            "Las fotos originales van en assets/galeria/<rubro>/.\n")

def peso_dir(d):
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(d) for f in fs) / 1e6 if os.path.isdir(d) else 0.0

def rubros_texto():
    """Cómo se nombra cada rubro en texto (para el rótulo de la galería), de para_proyecto/subir/dic_rubros.csv."""
    import csv
    p = os.path.join(ROOT, "para_proyecto", "subir", "dic_rubros.csv")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8-sig", newline="") as f:
        return {r["clave"]: r["como_se_nombra_en_texto"] for r in csv.DictReader(f, delimiter=";")}

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
        # Las obras completas de cada día (sin docs ni fotos) alimentan la vista semanal por zona: cada obra se muestra con los datos de su último parte.
        hist.append(dict(fecha=d, enEjecucion=len(act), finalizadas=None, puestos=j["puestos"], ids=[o["id"] for o in act],
                         obras=[{k: v for k, v in o.items() if k != "doc_orig"} for o in j["obras"] if o.get("estado", "ejecucion") == "ejecucion"]))

gal = galeria()
galeria_a_raiz()
gal_mb = peso_dir(os.path.join(ROOT, "deploy", GAL_OUT))
data = dict(parte=parte, circuitos=circuitos, fiscal=fiscal, contenido=contenido, hist=hist, assets=dict(svg=svg, fotos=fotos, docs=docs, galeria=gal, rubros_texto=rubros_texto()))
html = rd(os.path.join(ROOT, "tools", "plantilla.html"))
html = html.replace("/*__FONTS__*/", fuentes).replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
dst = os.path.join(OUT, "tablero.html")
open(dst, "w", encoding="utf-8").write(html)
pub = os.path.join(ROOT, "deploy")  # copia lista para publicar (ver deploy/LEEME.md)
os.makedirs(pub, exist_ok=True)
open(os.path.join(pub, "index.html"), "w", encoding="utf-8").write(html)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)   # la raíz y deploy/ van siempre iguales (ver deploy/LEEME.md)
total_mb = os.path.getsize(dst) / 1e6
print(f"{dst}  {total_mb:.1f} MB  obras={len(parte['obras'])}  con foto={sum(1 for o in parte['obras'] if fotos.get(o.get('doc')))}")
print(f"galería (deploy/{GAL_OUT}/, archivos sueltos): {gal_mb:.1f} MB · " + (", ".join(f"{k}={len(v)}" for k, v in gal.items()) or "sin carpetas en assets/galeria") + f" · tablero total {total_mb:.1f} MB")
if total_mb > 10:
    print(f"AVISO: el tablero pesa {total_mb:.1f} MB (> 10 MB). Alternativa: servir la galería como archivos sueltos en deploy/galeria/.")
~~~~

## tools/build_anuncios.py

~~~~python
"""Arma salida/anuncios/<fecha>/tablero_anuncios.html (autocontenido) a partir de entrada/anuncios/<fecha>/anuncios.json.

Uso:  python tools/build_anuncios.py 2026-10-30
Lee:  entrada/anuncios/<fecha>/anuncios.json, entrada/anuncios/<fecha>/contenido.json (opcional: textos editados a mano),
      data/dic_departamentos.csv, assets/marca/gobierno-color.svg, assets/marca/gobierno-gestion.svg, assets/marca/cinta-tricolor.svg, assets/fuentes/*.ttf
"""
import base64, csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1] if len(sys.argv) > 1 else sorted(d for d in os.listdir(os.path.join(ROOT, "entrada", "anuncios")) if d[:2] == "20")[-1]
IN = os.path.join(ROOT, "entrada", "anuncios", fecha)
OUT = os.path.join(ROOT, "salida", "anuncios", fecha)
os.makedirs(OUT, exist_ok=True)
rd = lambda p: open(p, encoding="utf-8").read()
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()

datos = json.load(open(os.path.join(IN, "anuncios.json"), encoding="utf-8"))

# Orden por inversión para el listado de la placa: al tablero solo llega el puesto (orden_inv, 1 = mayor inversión), nunca el monto.
# Fuente: orden_inversion del parser (columna Inversión de la base). Si el anuncios.json es anterior y no lo trae, se estima con
# el monto escrito en texto_original ("80 millones de pesos"); sin monto queda al final de su grupo.
RE_MILL = re.compile(r"(\d[\d\.,]*)\s*(mil\s+millones|millones|mill[oó]n)", re.I)
def _monto_txt(t):
    m = RE_MILL.search(t or "")
    if not m: return None
    n = float(m.group(1).replace(".", "").replace(",", "."))
    return n * (1e9 if m.group(2).lower().startswith("mil ") else 1e6)
if not any("orden_inversion" in a for a in datos["anuncios"]):
    _v = sorted(((_monto_txt(a.get("texto_original")), a["id"]) for a in datos["anuncios"] if a.get("tiene_inversion")), key=lambda x: -(x[0] or 0))
    _rk = {i: k + 1 for k, (v, i) in enumerate(_v) if v}
    for a in datos["anuncios"]: a["orden_inversion"] = _rk.get(a["id"])
for a in datos["anuncios"]: a["orden_inv"] = a.pop("orden_inversion", None)
_cp = os.path.join(IN, "contenido.json")
contenido = json.load(open(_cp, encoding="utf-8")) if os.path.exists(_cp) else {}
with open(os.path.join(ROOT, "data", "dic_departamentos.csv"), encoding="utf-8-sig") as f:
    deptos = list(csv.DictReader(f, delimiter=";"))
svg = {k: rd(os.path.join(ROOT, "assets", "marca", k + ".svg")) for k in ("gobierno-color", "gobierno-gestion", "cinta-tricolor")}

fuentes = ""
for w, name in ((900, "Black"), (800, "ExtraBold"), (700, "Bold"), (600, "SemiBold")):
    fuentes += f"@font-face{{font-family:Poppins;font-weight:{w};src:url(data:font/ttf;base64,{b64(os.path.join(ROOT, 'assets', 'fuentes', f'Poppins-{name}.ttf'))}) format('truetype')}}\n"

_tx = os.path.join(ROOT, "data", "anuncios_textos.json")   # redacción con IA por meta (tools/redactar_anuncios.py); se revisa a mano
textos = json.load(open(_tx, encoding="utf-8")).get("textos", {}) if os.path.exists(_tx) else {}
data = dict(datos=datos, deptos=deptos, contenido=contenido, textos=textos, svg=svg)
html = rd(os.path.join(ROOT, "tools", "plantilla_anuncios.html"))
html = html.replace("/*__FONTS__*/", fuentes).replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
dst = os.path.join(OUT, "tablero_anuncios.html")
open(dst, "w", encoding="utf-8").write(html)
pub = os.path.join(ROOT, "deploy")  # copia lista para publicar, junto a deploy/index.html (obras)
os.makedirs(pub, exist_ok=True)
open(os.path.join(pub, "anuncios.html"), "w", encoding="utf-8").write(html)
open(os.path.join(ROOT, "anuncios.html"), "w", encoding="utf-8").write(html)   # la raíz y deploy/ van siempre iguales (ver deploy/LEEME.md)
print(f"{dst}  {os.path.getsize(dst)/1e6:.1f} MB  anuncios={datos['total']}")
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

## tools/parse_anuncios.py

~~~~python
"""Convierte el seguimiento de anuncios (xlsx, hoja "Tablero") en entrada/anuncios/<fecha>/anuncios.json.

Uso:  python tools/parse_anuncios.py <archivo.xlsx> [fecha AAAA-MM-DD]
Lee:  data/dic_localidades.csv (maestra localidad -> departamento), data/dic_departamentos.csv (nombre publicable, alias, PIT),
      data/dic_estado_anuncio.csv (estado desagregado -> estado normalizado y etiqueta de placa).
Regla: no se inventa nada. La inversión se lee y no se publica. El texto de placa es una propuesta automática, editable en el tablero;
       lo que no se pudo limpiar queda marcado en "avisos" para revisarlo a mano.
"""
import csv, json, os, re, sys, unicodedata, datetime
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1]
fecha = sys.argv[2] if len(sys.argv) > 2 else datetime.date.today().isoformat()
OUT = os.path.join(ROOT, "entrada", "anuncios", fecha)
os.makedirs(OUT, exist_ok=True)

def norm(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode().upper()
    return re.sub(r"\s+", " ", s).strip()

def leer_csv(nombre):
    with open(os.path.join(ROOT, "data", nombre), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))

LOC = {r["localidad_norm"]: r for r in leer_csv("dic_localidades.csv")}
DEP = {}
for r in leer_csv("dic_departamentos.csv"):
    DEP[r["departamento_norm"]] = r
    for a in filter(None, r["alias"].split("|")):
        DEP[norm(a)] = r
EST = {r["estado_desagregado_norm"]: r for r in leer_csv("dic_estado_anuncio.csv")}

# ---------- texto de placa: limpieza conservadora del texto narrativo ----------
SUJETOS = r"(?:el\s+)?(?:gobernador|mandatario(?:\s+provincial)?|gobierno(?:\s+provincial|\s+de\s+c[oó]rdoba)?|provincia|llaryora)(?:\s+(?:de\s+c[oó]rdoba|provincial|mart[ií]n\s+llaryora|llaryora))?"
VERBOS = r"(?:anunci[oó]|confirm[oó]|comprometi[oó]|prometi[oó]|inaugur[oó]|habilit[oó]|firm[oó]|entreg[oó]|present[oó]|lanz[oó]|destac[oó]|adelant[oó]|ratific[oó]|se\s+comprometi[oó]\s+a|anunci[oó]\s+que|confirm[oó]\s+que|inform[oó]\s+que)"
RE_MONTO = re.compile(r"(?:(?:de|por|con)\s+)?(?:una\s+inversi[oó]n\s+(?:de\s+)?)?(?:\$\s?|US\$\s?|USD\s?)?\s*\d[\d\.,]*\s*(?:millones|mill[oó]n|mil)?\s*(?:de\s+)?(?:pesos|d[oó]lares|millones\s+de\s+pesos)?", re.I)
# un monto es una cifra CON marca de dinero ($, millones, pesos); un número solo (Ruta 6, 30 polideportivos) no se toca
NUM = r"(?:\d[\d\.,]*|un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|quince|veinte|treinta|cuarenta|cincuenta|cien|cientos?|mil)"
MONTO = r"(?:\b(?:m[aá]s|cerca|alrededor|unos|unas|casi|superior(?:es)?\s+a|los|las)\s+(?:de\s+)?)?(?:(?:\$|US\$|USD)\s*\d[\d\.,]*(?:\s*mil\b)?(?:\s*(?:millones|mill[oó]n)\b)?(?:\s+(?:de\s+)?(?:pesos|d[oó]lares))?|\b" + NUM + r"(?:\s+mil\b)?\s+(?:millones|mill[oó]n)\b(?:\s+(?:de\s+)?(?:pesos|d[oó]lares))?|\b" + NUM + r"(?:\s+mil\b)?\s+(?:de\s+)?(?:pesos|d[oó]lares)\b)"
ES_MONTO = re.compile(r"(?:\$|US\$|USD|millones|mill[oó]n|pesos|d[oó]lares)", re.I)
FUTUROS = [(r"construir[aá]n?", "Construcción de"), (r"ampliar[aá]n?", "Ampliación de"), (r"pavimentar[aá]n?", "Pavimentación de"), (r"finalizar[aá]n?", "Finalización de"),
           (r"entregar[aá]n?", "Entrega de"), (r"inaugurar[aá]n?", "Inauguración de"), (r"refaccionar[aá]n?", "Refacción de"), (r"renovar[aá]n?", "Renovación de"),
           (r"instalar[aá]n?", "Instalación de"), (r"invertir[aá]n?\s+en", "Inversión en"), (r"destinar[aá]n?", "Destino de"), (r"aportar[aá]n?", "Aporte de"), (r"financiar[aá]n?", "Financiamiento de")]
def limpiar_placa(txt):
    """Propuesta de texto de placa: sin sujeto inicial, sin monto, sin comillas ni saltos, sustantivo adelante cuando se puede. Siempre editable."""
    t = re.sub(r"\s+", " ", str(txt)).strip().strip('"“”«»').strip()
    avisos = []
    t = re.sub(r"\s*(?:Referencia|Ref\.?|Nota)\s*:.*$", "", t, flags=re.I)              # colas internas del seguimiento
    t = re.sub(r"^(?:Adem[aá]s|Asimismo|Tambi[eé]n|Por otra parte|Por su parte)\s*,?\s*", "", t, flags=re.I)
    t = re.sub(r"^[A-ZÁÉÍÓÚÑ][\w\s\.]{2,40}?:\s+(?=[A-ZÁÉÍÓÚÑ])", "", t)                   # "Villa María: Llaryora anunció..." -> sin el encabezado
    # sujeto + verbo al inicio: "El gobernador Martín Llaryora anunció la construcción de" -> "la construcción de"
    t2 = re.sub(r"^\W*(?:" + SUJETOS + r"\s+)?(?:tambi[eé]n\s+)?" + VERBOS + r"\s+(?:que\s+)?", "", t, flags=re.I)
    if t2 == t:
        t2 = re.sub(r"^\W*" + SUJETOS + r"\s+", "", t, flags=re.I)
    t = t2.strip()
    # montos: "aportes de 20 millones para" -> "aportes para"; "recibió 70 millones de pesos para" -> "recibió fondos para"; "30 millones para X" -> "Fondos para X"
    if ES_MONTO.search(t):
        t = re.sub(r"(?:,\s*)?(?:con|por|de)\s+(?:una\s+)?inversi[oó]n\s+(?:de\s+|por\s+|superior\s+a\s+|cercana\s+a\s+)?" + MONTO + r"\s*(?:,)?", " ", t, flags=re.I)
        t = re.sub(r"(?:,\s*)?(?:por|de)\s+" + MONTO + r"(?=\s+(?:para|en|destinad|que|con|y|a)\b|\s*[,.;]|$)", "", t, flags=re.I)
        t = re.sub(MONTO, "fondos", t, flags=re.I)
        t = re.sub(r"\bfondos\s+(?:de\s+)?fondos\b", "fondos", t, flags=re.I)
        t = re.sub(r"\s*\(fondos\)", "", t)
        t = re.sub(r",?\s*sumando fondos,?", "", t, flags=re.I)
        t = re.sub(r"\s{2,}", " ", t).strip(" ,;:.")
    # futuro -> sustantivo: "construirá un polideportivo" -> "Construcción de un polideportivo"
    for pat, rep in FUTUROS:
        m = re.match(r"^(?:se\s+|la\s+provincia\s+|el\s+gobierno\s+)?" + pat + r"\s+", t, flags=re.I)
        if m:
            t = rep + " " + t[m.end():]
            break
    t = re.sub(r"^(?:la|el|los|las|una|un)\s+", "", t, flags=re.I).strip(" .")
    if t:
        t = t[0].upper() + t[1:]
    t = re.sub(r"\s+:", ":", t); t = re.sub(r"\s*:\s*$", "", t); t = t.strip(' "“”«».,;')
    if ES_MONTO.search(t) or re.search(r"\$|\b\d{1,3}(?:\.\d{3}){2,}\b", t): avisos.append("monto o cifra en el texto")
    if re.search(r"\b(gobernador|llaryora|mandatario)\b", t, re.I): avisos.append("nombra al gobernador")
    if re.search(r"\b(anunci|comprometi|prometi|vamos a|ser[aá]n?\b|habr[aá]\b|[a-z]+r[aá]n?\b)", t, re.I) and re.search(r"\b(anunci|comprometi|prometi|vamos a|ser[aá]n?\b|habr[aá]\b|(?:construir|ampliar|invertir|entregar|destinar|financiar|realizar|ejecutar|llegar|sumar)[aá]n?\b)", t, re.I): avisos.append("verbo de anuncio o futuro")
    if len(t) > 140: avisos.append("texto largo para placa")
    if not t: avisos.append("texto vacío tras la limpieza")
    return t, avisos

df = pd.read_excel(src, sheet_name="Tablero")
df = df[df["Anuncio"].notna()]
# grafía publicable de cada localidad: la maestra viene en mayúsculas sin tildes; si la base trae la misma localidad con tildes, se prefiere esa
GRAFIA = {}
for v in df["Localidad"].dropna().astype(str):
    k = norm(v); cand = re.sub(r"\s+", " ", v).strip()
    if k not in GRAFIA or sum(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ().-" for ch in cand.upper()) > sum(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ().-" for ch in GRAFIA[k].upper()):
        GRAFIA[k] = cand
GRAF = {r["palabra"]: r["con_tilde"] for r in leer_csv("dic_grafia.csv")}   # tildes que la maestra no trae (palabra por palabra)
def titulo(s):
    w = [x for x in str(s).split(" ") if x]
    out = []
    for i, x in enumerate(w):
        xl = x.lower()
        if xl in ("de", "del", "la", "las", "los", "el", "y", "e") and i > 0: out.append(xl)
        elif x.upper() in GRAF: out.append(GRAF[x.upper()])
        else: out.append(xl[0].upper() + xl[1:])
    return " ".join(out)
out, avisos_glob, vistos = [], [], {}
for _, r in df.iterrows():
    anuncio = str(r["Anuncio"]).strip()
    alcance = {"Local": "local", "Provincial": "provincial", "PIT": "pit"}.get(str(r["Alcance del anuncio"]).strip(), "otro")
    ln, dn = norm(r["Localidad"]), norm(r["Departamento"])
    loc, dep, avisos = None, None, []
    if ln in LOC:
        m = LOC[ln]; loc = titulo(GRAFIA.get(ln, m["localidad_maestra"])); dep = DEP.get(m["departamento_norm"])
        if dn and dn not in ("PROVINCIA",) and DEP.get(dn) is not dep and DEP.get(dn):
            avisos.append(f"departamento de la base ({r['Departamento']}) distinto al de la maestra ({dep['nombre_publicable']}); se usa la maestra")
    elif ln in ("PROVINCIA", "-", ""):
        loc = None; dep = DEP.get(dn)
        if alcance == "local": avisos.append("anuncio local sin localidad")
    else:
        avisos.append(f"localidad fuera de la maestra: {r['Localidad']}")
        dep = DEP.get(dn)
    est_des = norm(r["Estado (desagregado)"])
    e = EST.get(est_des)
    estado_base = {"CUMPLIDO": "cumplido", "EN EJECUCIÓN": "en_ejecucion", "EN EJECUCION": "en_ejecucion", "PENDIENTE": "pendiente"}.get(norm(r["Estado"]), "otro")
    if not e:
        avisos.append(f"estado desagregado sin diccionario: {r['Estado (desagregado)']}")
        e = {"estado": estado_base, "estado_detalle": "sin_dato", "etiqueta_placa": {"cumplido": "Cumplido", "en_ejecucion": "En ejecución"}.get(estado_base, ""), "publicable": "no"}
    elif e["estado"] != estado_base and estado_base != "otro":
        avisos.append(f"estado ({r['Estado']}) no coincide con el desagregado ({r['Estado (desagregado)']}); se usa el estado")
        e = dict(e, estado=estado_base)
    placa, av2 = limpiar_placa(anuncio)
    avisos += av2
    clave = (norm(anuncio), ln)
    if clave in vistos:
        avisos_glob.append(f"Duplicado: meta {r['Meta']} repite la meta {vistos[clave]} ({loc or r['Localidad']}); se deja una sola")
        continue
    vistos[clave] = int(r["Meta"])
    fa = pd.to_datetime(r["Fecha de anuncio"], errors="coerce")
    inv = r["Inversión"]
    out.append(dict(
        id=int(r["Meta"]), fecha_anuncio=fa.date().isoformat() if pd.notna(fa) else None, anio=int(r["Año"]) if pd.notna(r["Año"]) else None,
        alcance=alcance, localidad=loc, localidad_base=str(r["Localidad"]).strip(),
        departamento=dep["nombre_publicable"] if dep else None, departamento_norm=dep["departamento_norm"] if dep else None, pit=(dep["pit"] == "si") if dep else False,
        eje=str(r["Eje"]).strip() if pd.notna(r["Eje"]) else None, ministerio=str(r["Ministerio"]).strip() if pd.notna(r["Ministerio"]) else None,
        tipo_discurso=str(r["Tipo de discurso"]).strip() if pd.notna(r["Tipo de discurso"]) else None,
        estado=e["estado"], estado_detalle=e["estado_detalle"], etiqueta=e["etiqueta_placa"], publicable=(e["publicable"] == "si"),
        estado_base_txt=str(r["Estado"]).strip() if pd.notna(r["Estado"]) else None,   # textual de la base, para la tabla "Textuales de la base"
        estado_desagregado_txt=str(r["Estado (desagregado)"]).strip() if pd.notna(r["Estado (desagregado)"]) else None,
        texto_original=anuncio, texto_placa=placa, detalle=str(r["Detalle del anuncio"]).strip() if pd.notna(r["Detalle del anuncio"]) else None,
        tiene_inversion=bool(pd.notna(inv) and str(inv).strip() not in ("-", "")),
        _inv=pd.to_numeric(str(inv).replace("$", "").replace(".", "").replace(",", ".").strip(), errors="coerce") if pd.notna(inv) else None,
        fuente_anuncio=str(r["Fuente del anuncio"]).strip() if pd.notna(r["Fuente del anuncio"]) else None,
        fuente_seguimiento=str(r["Fuente de Seguimiento"]).strip() if pd.notna(r["Fuente de Seguimiento"]) else None,
        avisos=avisos,
    ))

# la inversión no sale del parser: solo el puesto (1 = mayor), que usa la placa de listado para ordenar
_rk = sorted((a for a in out if a["_inv"] is not None and pd.notna(a["_inv"]) and a["_inv"] > 0), key=lambda a: -a["_inv"])
_pos = {a["id"]: k + 1 for k, a in enumerate(_rk)}
for a in out:
    a.pop("_inv"); a["orden_inversion"] = _pos.get(a["id"])

res = dict(fecha=fecha, fuente=os.path.basename(src), total=len(out), avisos=avisos_glob, anuncios=out)
json.dump(res, open(os.path.join(OUT, "anuncios.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
n = lambda f: sum(1 for a in out if f(a))
print(f"{OUT}/anuncios.json  anuncios={len(out)}  cumplidos={n(lambda a:a['estado']=='cumplido')}  en ejecución={n(lambda a:a['estado']=='en_ejecucion')}  "
      f"sin localidad={n(lambda a:a['alcance']=='local' and not a['localidad'])}  con avisos de placa={n(lambda a:any(x in ' '.join(a['avisos']) for x in ('monto','gobernador','verbo','largo')))}  duplicados={len(avisos_glob)}")
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

## tools/redactar_anuncios.py

~~~~python
"""Redacta con IA el texto de placa, un titular y un resumen de cada anuncio, UNA sola vez por anuncio (meta).

Uso:  python tools/redactar_anuncios.py <fecha> [--solo-nuevos] [--limite N] [--modelo claude-sonnet-4-6]
Lee:  entrada/anuncios/<fecha>/anuncios.json
Escribe: data/anuncios_textos.json  {"textos": {"<meta>": {"placa", "titular", "resumen", "duda", "modelo", "fecha", "revisado": false}}}
Requiere la variable de entorno ANTHROPIC_API_KEY (nunca va en archivos ni en el repo).

Reglas que recibe el modelo (las mismas del equipo): no inventar nada que no esté en el texto; sin montos ni signos de pesos; sin "el gobernador anunció";
sustantivo adelante; una frase corta para la placa (hasta 90 caracteres); lo cumplido en pasado o como hecho, lo en marcha en presente, nunca en futuro.
Los textos quedan con revisado=false: el tablero los usa, pero el Chequeo de calidad los lista hasta que alguien los marque revisados (o los corrija).
"""
import json, os, sys, time, datetime, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
fecha = next((a for a in args if a[:2] == "20"), None) or sorted(d for d in os.listdir(os.path.join(ROOT, "entrada", "anuncios")) if d[:2] == "20")[-1]
solo_nuevos = "--solo-nuevos" in args
limite = int(args[args.index("--limite") + 1]) if "--limite" in args else None
modelo = args[args.index("--modelo") + 1] if "--modelo" in args else "claude-sonnet-4-6"
KEY = os.environ.get("ANTHROPIC_API_KEY")
if not KEY:
    sys.exit("Falta ANTHROPIC_API_KEY en el entorno (PowerShell: $env:ANTHROPIC_API_KEY='...'). No la escribas en ningún archivo.")

datos = json.load(open(os.path.join(ROOT, "entrada", "anuncios", fecha, "anuncios.json"), encoding="utf-8"))
dst = os.path.join(ROOT, "data", "anuncios_textos.json")
store = json.load(open(dst, encoding="utf-8")) if os.path.exists(dst) else {"_nota": "Redacción con IA por meta. revisado=false hasta que alguien lo revise. Corregir acá o en contenido.json.", "textos": {}}
T = store["textos"]

SISTEMA = """Sos redactor de prensa del Gobierno de la Provincia de Córdoba (tono de prensa.cba.gov.ar: claro, oficial, sin adjetivos de más).
Recibís un anuncio de gestión tal como lo registró el área de seguimiento (texto narrativo, a veces una cita textual del gobernador) y su estado real.
Devolvés SOLO un JSON con estas claves:
- "placa": una frase corta (máximo 90 caracteres) para una placa gráfica, sustantivo adelante ("Construcción del cuartel de bomberos", "Aporte para el club Sportivo Independiente", "Red de gas natural para el barrio Norte"). Sin punto final.
- "titular": un titular de nota (máximo 110 caracteres) que diga qué se hizo y dónde. Si el estado es cumplido, en pasado o como hecho concreto; si está en marcha, en presente, nunca en futuro.
- "resumen": una o dos oraciones para el cuerpo de una gacetilla, solo con lo que dice el anuncio y su detalle.
- "duda": "" si el anuncio describe una acción concreta publicable; si no (es una frase de ocasión, una valoración, un dato vago, una promesa sin objeto, o depende de otra localidad), explicá en pocas palabras por qué no conviene publicarlo.
Reglas que no se pueden romper: no agregar ningún dato que no esté en el texto (ni cantidades, ni plazos, ni beneficiarios, ni nombres); sin montos, cifras en pesos ni la palabra "millones"; no escribir "el gobernador", "Llaryora", "anunció", "prometió" ni "comprometió"; sin barras "/"; nunca usar las palabras "circuito" ni "seccional". Si el texto cuenta varias cosas, la placa toma la principal. Si el texto ya es una buena placa, devolvelo casi igual."""

def pedir(a):
    user = (f"Anuncio: {a['texto_original']}\n" + (f"Detalle: {a['detalle']}\n" if a.get('detalle') else "") +
            f"Estado: {a['estado']} ({a['etiqueta']})\nLocalidad: {a['localidad'] or a['localidad_base']}\nDepartamento: {a['departamento'] or '-'}\nAlcance: {a['alcance']}")
    body = json.dumps({"model": modelo, "max_tokens": 400, "temperature": 0.2, "system": SISTEMA, "messages": [{"role": "user", "content": user}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={"content-type": "application/json", "x-api-key": KEY, "anthropic-version": "2023-06-01"})
    for intento in range(4):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=90))
            txt = "".join(c.get("text", "") for c in r["content"]).strip().strip("`")
            txt = txt[txt.find("{"):txt.rfind("}") + 1]
            return json.loads(txt)
        except Exception as e:
            if intento == 3: raise
            time.sleep(2 * (intento + 1))

pend = [a for a in datos["anuncios"] if a["estado"] in ("cumplido", "en_ejecucion") and (not solo_nuevos or str(a["id"]) not in T)]
if limite: pend = pend[:limite]
print(f"a redactar: {len(pend)} anuncios (ya había {len(T)})")
hoy = datetime.date.today().isoformat()
for i, a in enumerate(pend, 1):
    if str(a["id"]) in T and not solo_nuevos and T[str(a["id"])].get("revisado"):
        continue   # lo revisado a mano no se pisa
    try:
        r = pedir(a)
    except Exception as e:
        print(f"FALLA meta {a['id']}: {e}"); continue
    T[str(a["id"])] = {"placa": str(r.get("placa", "")).strip(" ."), "titular": str(r.get("titular", "")).strip(), "resumen": str(r.get("resumen", "")).strip(), "duda": str(r.get("duda", "")).strip(),
                       "modelo": modelo, "fecha": hoy, "revisado": False}
    if i % 25 == 0 or i == len(pend):
        json.dump(store, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{i}/{len(pend)} guardados")
json.dump(store, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
con_duda = sum(1 for v in T.values() if v.get("duda"))
print(f"listo: {len(T)} textos en {dst}; {con_duda} con duda para revisar. Después: python tools/build_anuncios.py {fecha}")
~~~~

## deploy/middleware.js

~~~~javascript
// Acceso por usuario y contraseña (HTTP Basic) validado en el servidor.
// Las credenciales viven en variables de entorno de Vercel, nunca en el HTML ni en el repositorio:
//   TABLERO_ACCESOS                  una credencial por línea, con el formato usuario:clave (una por persona).
//                                    Las líneas vacías y las que empiezan con # se ignoran.
//   TABLERO_USUARIO / TABLERO_CLAVE  la credencial compartida original; sigue valiendo mientras esté cargada.
// Si no hay ninguna credencial cargada, el sitio queda cerrado.
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

// Credenciales habilitadas. Se leen en cada pedido: al cambiar la variable y redesplegar, el cambio vale enseguida.
function accesos() {
  const lista = (process.env.TABLERO_ACCESOS || '')
    .split('\n')
    .map(l => l.trim())
    .filter(l => l && l[0] !== '#')
    .map(l => { const i = l.indexOf(':'); return i > 0 ? [l.slice(0, i), l.slice(i + 1)] : null; })
    .filter(c => c && c[1]);                                  // sin usuario o sin clave, la línea no habilita a nadie
  const user = process.env.TABLERO_USUARIO, pass = process.env.TABLERO_CLAVE;
  if (user && pass) lista.push([user, pass]);
  return lista;
}

export default function middleware(request) {
  const habilitados = accesos();
  if (!habilitados.length) return cerrado(503);

  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    try {
      const dec = new TextDecoder().decode(Uint8Array.from(atob(auth.slice(6)), c => c.charCodeAt(0)));
      const i = dec.indexOf(':');                             // la clave puede tener ":": corta en el primero
      if (i > -1) {
        const usuario = dec.slice(0, i), clave = dec.slice(i + 1);
        if (habilitados.some(([u, c]) => igual(u, usuario) && igual(c, clave))) {
          return new Response(null, { headers: { 'x-middleware-next': '1' } });
        }
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
