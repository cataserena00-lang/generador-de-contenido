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
total_mb = os.path.getsize(dst) / 1e6
print(f"{dst}  {total_mb:.1f} MB  obras={len(parte['obras'])}  con foto={sum(1 for o in parte['obras'] if fotos.get(o.get('doc')))}")
print(f"galería (deploy/{GAL_OUT}/, archivos sueltos): {gal_mb:.1f} MB · " + (", ".join(f"{k}={len(v)}" for k, v in gal.items()) or "sin carpetas en assets/galeria") + f" · tablero total {total_mb:.1f} MB")
if total_mb > 10:
    print(f"AVISO: el tablero pesa {total_mb:.1f} MB (> 10 MB). Alternativa: servir la galería como archivos sueltos en deploy/galeria/.")

