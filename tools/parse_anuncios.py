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
        texto_original=anuncio, texto_placa=placa, detalle=str(r["Detalle del anuncio"]).strip() if pd.notna(r["Detalle del anuncio"]) else None,
        tiene_inversion=bool(pd.notna(inv) and str(inv).strip() not in ("-", "")),
        fuente_anuncio=str(r["Fuente del anuncio"]).strip() if pd.notna(r["Fuente del anuncio"]) else None,
        fuente_seguimiento=str(r["Fuente de Seguimiento"]).strip() if pd.notna(r["Fuente de Seguimiento"]) else None,
        avisos=avisos,
    ))

res = dict(fecha=fecha, fuente=os.path.basename(src), total=len(out), avisos=avisos_glob, anuncios=out)
json.dump(res, open(os.path.join(OUT, "anuncios.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
n = lambda f: sum(1 for a in out if f(a))
print(f"{OUT}/anuncios.json  anuncios={len(out)}  cumplidos={n(lambda a:a['estado']=='cumplido')}  en ejecución={n(lambda a:a['estado']=='en_ejecucion')}  "
      f"sin localidad={n(lambda a:a['alcance']=='local' and not a['localidad'])}  con avisos de placa={n(lambda a:any(x in ' '.join(a['avisos']) for x in ('monto','gobernador','verbo','largo')))}  duplicados={len(avisos_glob)}")
