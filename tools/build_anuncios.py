"""Arma salida/anuncios/<fecha>/tablero_anuncios.html (autocontenido) a partir de entrada/anuncios/<fecha>/anuncios.json.

Uso:  python tools/build_anuncios.py 2026-10-30
Lee:  entrada/anuncios/<fecha>/anuncios.json, entrada/anuncios/<fecha>/contenido.json (opcional: textos editados a mano),
      data/dic_departamentos.csv, assets/marca/gobierno-color.svg, assets/marca/cinta-tricolor.svg, assets/fuentes/*.ttf
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
svg = {k: rd(os.path.join(ROOT, "assets", "marca", k + ".svg")) for k in ("gobierno-color", "cinta-tricolor")}

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
print(f"{dst}  {os.path.getsize(dst)/1e6:.1f} MB  anuncios={datos['total']}")
