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
