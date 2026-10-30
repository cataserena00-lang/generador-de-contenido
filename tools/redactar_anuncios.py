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
