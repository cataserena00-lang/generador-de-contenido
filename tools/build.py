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
        # Las obras completas de cada día (sin docs ni fotos) alimentan la vista semanal por zona: cada obra se muestra con los datos de su último parte.
        hist.append(dict(fecha=d, enEjecucion=len(act), finalizadas=None, puestos=j["puestos"], ids=[o["id"] for o in act],
                         obras=[{k: v for k, v in o.items() if k != "doc_orig"} for o in j["obras"] if o.get("estado", "ejecucion") == "ejecucion"]))

data = dict(parte=parte, circuitos=circuitos, fiscal=fiscal, contenido=contenido, hist=hist, assets=dict(svg=svg, fotos=fotos, docs=docs))
html = rd(os.path.join(ROOT, "tools", "plantilla.html"))
html = html.replace("/*__FONTS__*/", fuentes).replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
dst = os.path.join(OUT, "tablero.html")
open(dst, "w", encoding="utf-8").write(html)
pub = os.path.join(ROOT, "deploy")  # copia lista para publicar (ver deploy/LEEME.md)
os.makedirs(pub, exist_ok=True)
open(os.path.join(pub, "index.html"), "w", encoding="utf-8").write(html)
print(f"{dst}  {os.path.getsize(dst)/1e6:.1f} MB  obras={len(parte['obras'])}  con foto={sum(1 for o in parte['obras'] if fotos.get(o.get('doc')))}")

