#!/usr/bin/env python3
"""Arma los archivos livianos para subir al Proyecto de Claude (cuenta Team).

Python estándar, sin librerías externas. NO modifica nada del proyecto: solo lee y escribe en la carpeta de salida.

Uso (desde cualquier lugar):
    python armar_para_proyecto.py                       # proyecto = carpeta que contiene a esta carpeta
    python armar_para_proyecto.py --proyecto RUTA --salida RUTA_SALIDA

Genera en <proyecto>/para_proyecto/subir/ :
    marca_resumen.md          resumen de marca (reemplaza SVG/PNG/fuentes)
    esquema_parte.md          esquema y reglas de los JSON del día
    muestra_parte.json        muestra representativa del parte más reciente
    historico_resumen.csv     una fila por día (conteos), reemplaza los partes completos
    dic_circuitos.csv         código de circuito -> nombre (uso interno, nunca en textos)
    dic_barrio_circuito.csv   tabla barrio -> código de circuito
    dic_pavimentacion.csv     datos oficiales de las memorias (cuadras, plazos)
    dic_rubros.csv            rubros del parte y cómo se nombran
    dic_campos_parte.csv      diccionario de campos de parte.json
    reglas_parte.md           copia de data/reglas_parte.md
    codigo_pipeline.md        tools/*.py + deploy (middleware, vercel.json) con secretos ocultos
    codigo_plantilla.md       tools/plantilla.html con secretos ocultos (opcional, es lo más pesado)
    notebooks_sin_outputs/    copia de cada .ipynb sin outputs (si hay)
Además imprime un aviso con los archivos del proyecto que parecen contener secretos (solo la ruta, nunca el valor).
"""
import argparse, csv, glob, json, os, re, sys

LISTADO = [["1", "14A", "ARGUELLO NORTE", "19970", "07/04/2026"], ["1", "5D", "MALDONADO", "12190", "07/04/2026"], ["1", "5F", "RENACIMIENTO", "5009", "07/04/2026"], ["1", "4F", "CIUDAD OBISPO ANGELELLI", "3630", "07/04/2026"], ["1", "13J", "VILLA AZALAIS", "32084", "08/04/2026"], ["1", "12D", "JOSE IGNACIO DIAZ", "28158", "08/04/2026"], ["1", "11A", "ALTO ALBERDI", "23106", "09/04/2026"], ["1", "12F", "JOSE HERNANDEZ", "20634", "09/04/2026"], ["1", "13G", "PARQUE LICEO", "20477", "09/04/2026"], ["1", "8B", "PUEYRREDON", "19663", "09/04/2026"], ["2", "14J", "URCA", "7580", "10/04/2026"], ["2", "14D", "CERRO DE LAS ROSAS", "5985", "10/04/2026"], ["2", "14L", "VILLA BELGRANO", "4953", "10/04/2026"], ["2", "11L", "COUNTRYS DEL OESTE", "3122", "10/04/2026"], ["2", "12B", "COLON", "22043", "17/04/2026"], ["2", "10", "BELLA VISTA", "18147", "17/04/2026"], ["2", "5C", "EMPALME", "17999", "17/04/2026"], ["2", "13H", "PATRICIOS", "17398", "20/04/2026"], ["2", "11I", "RESIDENCIAL SAN ROQUE", "16775", "20/04/2026"], ["2", "13A", "AYACUCHO", "16091", "20/04/2026"], ["3", "5G", "SAN VICENTE", "15015", "21/04/2026"], ["3", "5", "ALTAMIRA", "13498", "21/04/2026"], ["3", "9C", "LOS PARAISOS", "13491", "21/04/2026"], ["3", "13C", "GENERAL BUSTOS", "13212", "22/04/2026"], ["3", "10F", "MATIENZO", "13148", "22/04/2026"], ["3", "7G", "PANAMERICANO", "12848", "22/04/2026"], ["3", "12H", "LOS CERVECEROS", "12793", "22/04/2026"], ["3", "10J", "SANTA ISABEL", "12361", "22/04/2026"], ["3", "11K", "VILLA GRAL URQUIZA", "11954", "23/04/2026"], ["3", "12G", "ITUZAINGO", "11478", "23/04/2026"], ["4", "12", "AVELLANEDA", "10141", "23/04/2026"], ["4", "14G", "LOS BOULEVARES", "9874", "23/04/2026"], ["4", "8C", "VILLA LOS PINOS", "8237", "14/07/2026"], ["4", "9B", "LAS MARGARITAS", "7582", "14/07/2026"], ["4", "7A", "GUIÑAZU", "6915", "14/07/2026"], ["4", "9A", "LA FRANCE", "4738", "14/07/2026"], ["4", "8A", "PALMAR", "4287", "14/07/2026"], ["4", "4E", "NUESTRO HOGAR III", "3407", "14/07/2026"], ["4", "4D", "VILLA EUCARISTICA", "3337", "14/07/2026"], ["4", "5B", "DEAN FUNES", "1807", "14/07/2026"], ["5", "6F", "YAPEYU", "8149", "15/07/2026"], ["5", "5I", "COLINAS DEL SUR", "5343", "15/07/2026"], ["5", "5E", "VILLA BUSTOS", "4213", "15/07/2026"], ["5", "6E", "LA FLORESTA SUD", "2776", "15/07/2026"], ["5", "9F", "SAN MARTIN", "14847", "17/07/2026"], ["5", "10B", "CIUDADELA", "11744", "17/07/2026"], ["5", "9D", "POETA LUGONES", "9264", "17/07/2026"], ["5", "9G", "VILLA CABRERA", "5530", "17/07/2026"], ["5", "10A", "CABILDO", "5137", "17/07/2026"], ["5", "10G", "OBSERVATORIO", "20821", "18/07/2026"], ["6", "10E", "ESTACION FLORES", "15037", "18/07/2026"], ["6", "10C", "COMERCIAL", "7478", "18/07/2026"], ["6", "10K", "VICOR", "7199", "18/07/2026"], ["6", "11B", "DON BOSCO", "7097", "18/07/2026"], ["6", "11D", "LOS NARANJOS", "12296", "19/07/2026"], ["6", "11H", "QUEBRADA LAS ROSAS", "6926", "19/07/2026"], ["6", "12A", "CARCANO", "6238", "19/07/2026"], ["6", "12C", "CORONEL OLMEDO", "4808", "19/07/2026"], ["6", "13I", "SAN JORGE", "5738", "20/07/2026"], ["6", "12E", "FERREYRA", "5418", "20/07/2026"], ["7", "13D", "JARDIN ARENALES", "3021", "20/07/2026"], ["7", "12I", "CIUDAD DE MIS SUEÑOS", "2893", "20/07/2026"], ["7", "13N", "YOFRE", "7319", "21/07/2026"], ["7", "14F", "GRANJA DE FUNES", "6845", "21/07/2026"], ["7", "14E", "CERRO NORTE", "6712", "21/07/2026"], ["7", "14H", "MERCANTIL", "5989", "22/07/2026"], ["7", "14Q", "VILLA WARCALDE", "1407", "22/07/2026"], ["7", "6C", "GRAL PAZ", "12404", "27/07/2026"], ["7", "7D", "COFICO", "9905", "27/07/2026"], ["7", "6D", "JUNIORS", "6692", "27/07/2026"], ["7", "9E", "PROVIDENCIA", "5048", "27/07/2026"], ["7", "3", "SECCIONAL TERCERA", "20258", "01/09/2026"], ["7", "14O", "VILLA 9 DE JULIO", "8114", "14/10/2026"]]  # filas (grupo, codigo, nombre, padrón, última encuesta); salen de "Listados por grupo/*.pdf"

# ---------------------------------------------------------------- secretos
PATRONES = [
    (re.compile(r"""(?i)\b(token|password|passwd|pwd|clave|secret|api[_-]?key|authorization)(["']?\s*[:=]\s*)(["'])([^"'\n]{6,})\3"""), r"\1\2\3***OCULTO***\3"),
    (re.compile(r"https://script\.google\.com/macros/s/[A-Za-z0-9_\-]+"), "https://script.google.com/macros/s/***OCULTO***"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b"), "***OCULTO***"),
    (re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b|\bAKIA[0-9A-Z]{16}\b|\bAKfy[A-Za-z0-9_\-]{20,}\b"), "***OCULTO***"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._\-]{20,}"), "Bearer ***OCULTO***"),
    (re.compile(r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{32,}\b"), "***OCULTO***"),
]
SOSPECHA = re.compile(r"(?i)(token|password|passwd|clave|secret|api[_-]?key)\s*[:=|]\s*[`'\"]?[A-Za-z0-9/_\-+.]{12,}|https://script\.google\.com/macros/s/|\bgh[pousr]_[A-Za-z0-9]{20,}|\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{40,}\b")

def ocultar(texto):
    n = 0
    for rx, rep in PATRONES:
        texto, k = rx.subn(rep, texto)
        n += k
    return texto, n

# ---------------------------------------------------------------- utilidades
def leer(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()

def jleer(p, defecto=None):
    try:
        return json.loads(leer(p))
    except Exception:
        return defecto

def escribir(p, texto):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)

def escribir_csv(p, cabecera, filas):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8-sig", newline="") as f:    # utf-8-sig: Excel abre bien las tildes
        w = csv.writer(f, delimiter=";")
        w.writerow(cabecera); w.writerows(filas)

def dias(proyecto):
    base = os.path.join(proyecto, "entrada")
    if not os.path.isdir(base):
        return []
    return sorted(d for d in os.listdir(base) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) and os.path.exists(os.path.join(base, d, "parte.json")))

# ---------------------------------------------------------------- piezas
RUBROS = [
    ("mant", "Mantenimiento de calles", "calle", "Calles de tierra: la línea del parte es el barrio", "mantenimiento de calles"),
    ("frio", "Bacheo en frío", "calle", "Bacheo en frío: la línea del parte es el barrio", "bacheo en frío"),
    ("rampas", "Rampas", "accesible", "Una esquina = UNA obra (con N rampas). Sin barrio. Placas: 'Rampas en ejecución'", "rampas"),
    ("bacheo", "Bacheo con asfalto", "calle", "Calle y entre-calles; barrio explícito", "bacheo con asfalto"),
    ("rehab", "Rehabilitación con asfalto", "calle", "Puede ser nocturno", "rehabilitación con asfalto"),
    ("hormigon", "Rehabilitación y bacheo con hormigón", "calle", "Puede tener nota de etapa (3.ª etapa)", "rehabilitación y bacheo con hormigón"),
    ("pav", "Pavimentación", "calle", "Cuadras y plazo salen de las memorias (data/memorias.json), barrio de la memoria si el parte no lo trae", "pavimentación"),
    ("plaza", "Plazas", "plaza", "Se deduplica por nombre dentro del día; alias en la plantilla (ALIAS) y en parse_lista.py (PLAZA_ALIAS)", "plazas en renovación"),
]
CAMPOS = [
    ("fecha", "texto AAAA-MM-DD", "Día del parte", "2026-10-29"),
    ("fecha_texto", "texto", "Fecha escrita para el encabezado", "jueves 29 de octubre de 2026"),
    ("enEjecucion", "entero", "Obras en ejecución según el encabezado del parte (control contra los ítems leídos)", "61"),
    ("puestos", "entero", "Puestos de trabajo directos del día (dato de toda la ciudad)", "599"),
    ("finalizadas", "entero o null", "STOCK acumulado de obras finalizadas (no es del día); se usa solo para acumulados", "192"),
    ("acumulados", "objeto", "Metas de plan: cuadras_pavimentadas 1100 y rampas_programa 2100. Son planes: se dice 'prevé' o 'contempla'", ""),
    ("programaRampas", "objeto", "Del doc del programa: total 2100, nuevas 2000, en_esquinas_sin_rampa 1317, reparadas 100", ""),
    ("avisos", "lista de texto", "Contradicciones parte vs. docs y códigos sin circuito; se muestran en 'Chequeo de calidad'", ""),
    ("obras[].id", "texto", "<tipo>_<slug de la calle o sector> (+ slug de entre-calles si hay duplicado)", "hormigon_av-patria"),
    ("obras[].tipo", "texto", "mant, frio, rampas, bacheo, rehab, hormigon, pav, plaza", "hormigon"),
    ("obras[].circuito", "texto", "Código del parte (número + letra opcional). Dato interno: nunca se publica", "6"),
    ("obras[].via / entre", "texto o null", "Calle y entre-calles (bacheo, rehab, hormigón, rampas, plazas)", "Av. Patria / Av. 24 de Septiembre y Armenia"),
    ("obras[].sector", "texto o null", "Nombre del sector en mant, frio y pav", "Policial Etapa II"),
    ("obras[].barrio", "texto o null", "Barrio; en los textos siempre con el prefijo 'Barrio'", "Hogar Propio"),
    ("obras[].rampas", "entero o null", "Cantidad de rampas de la esquina (o del grupo)", "4"),
    ("obras[].doc", "texto o null", "Clave del Google Doc de la obra (fotos y texto en entrada/_cache)", "av_patria"),
    ("obras[].grupo", "booleano", "true = resumen de rampas (zona céntrica o Pueyrredón); no cuenta como obra", "false"),
    ("obras[].estado", "texto", "ejecucion o terminada", "ejecucion"),
    ("obras[].nota", "lista", "Nocturno, 3.ª etapa, 2.ª intervención, o 'N rampas'", ""),
    ("obras[].barrio_inferido / circ_inferido", "texto / booleano", "Marcas de que el dato no vino en el parte", ""),
    ("obras[].metricas", "objeto", "driveUrl, m2, ml, cuadras, plazo, nocturno, esquinas. Si no hay dato, el texto no lleva magnitud", ""),
    ("contenido.json", "objeto", "Piezas redactadas a mano del día: generales{id:{titulos,ig,x,gac,placa}} y periodicos{id:{titulo,eje,titulos,ig,x,placa,gac}}", ""),
]

MARCA_FIJO = """# Resumen de marca (reemplaza SVG, PNG y fuentes del repo)

Fuente de colores: `assets/marca/paleta.json`, extraída de los carteles .ai (valores de relleno exactos).
Los archivos gráficos (SVG/PNG, fuentes Poppins) viven en el repo y los usa `tools/build.py`; **no hace falta subirlos**.

## Tres ejes de comunicación
| Eje | Nombre en texto | Pie de placa | Hashtags | Emoji |
|---|---|---|---|---|
| calle | Calle por Calle, Córdoba Mejora | #17233d (marino) | #CallePorCalle #CórdobaMejora #HacerParaCrecer | 🛣️ |
| accesible | Córdoba Accesible | #09467f (azul) | #CórdobaAccesible #HacerParaCrecer | ♿ |
| plaza | Nos vemos en la Plaza, Córdoba Mejora | #09467f (azul), con logo extra EPEC | #NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer | 🌳 |

Lema general: **Hacer para Crecer**. Encuadre: "Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba".
Accesible: "Una Córdoba inclusiva, pensada para todos" (siempre "Rampas en ejecución", nunca "nuevas").

## Tipografía
Poppins: ExtraBold/Black para títulos y cifras, SemiBold/Bold para etiquetas. Licencia OFL.

## Formatos de placa (canvas, se bajan como PNG)
- Feed 1:1 = 1080×1080; Feed 4:5 = 1080×1350 (recomendado); Stories/Reels 9:16 = 1080×1920.
- Historia 9:16: zona segura, ~14 % libre arriba y el pie termina al 88,5 % del alto (contenido centrado, relleno amarillo arriba y azul abajo en el eje accesible).
- Pie de placa: franja de color del eje con la tira de logos institucionales; wordmark del eje arriba.

## Diseños con foto
- Círculo, Marco, Foto completa y Sin foto. "Sugerido" elige por la foto: chica (<720 px) o borrosa (nitidez <800) → Círculo; vertical y nítida → Completa; horizontal y nítida → rotativo.
- El texto de la placa se edita en pantalla y la placa se redibuja.
- Placa: [título] [dato/valor] [lugar] [barrio]; sin montos; barrio con la palabra "Barrio".

"""

def marca_md(proyecto):
    pal = jleer(os.path.join(proyecto, "assets", "marca", "paleta.json"), {})
    inf = jleer(os.path.join(proyecto, "assets", "marca", "_info.json"), {})
    t = MARCA_FIJO + "## Paleta por eje (de paleta.json)\n"
    for eje, v in (pal.get("ejes") or {}).items():
        t += f"\n**{eje}** — {v.get('nombre', '')}\n" + "".join(f"- {k}: `{x}`\n" for k, x in v.items() if k != "nombre")
    if inf:
        t += "\n## Medidas de los carteles originales (de _info.json)\n| Eje | Cartel (pt) | Color del pie | Alto del pie | Relación de la tira de logos |\n|---|---|---|---|---|\n"
        for eje, v in inf.items():
            t += f"| {eje} | {v.get('poster_pt', [''])[0]}×{v.get('poster_pt', ['', ''])[1]} | {v.get('footer_bg', '')} | {v.get('footer_h_ratio', '')} | {v.get('logos_aspect', '')} |\n"
    t += "\n## Qué hay en el repo (no subir)\n"
    mar = os.path.join(proyecto, "assets", "marca")
    if os.path.isdir(mar):
        t += "`assets/marca/`: " + ", ".join(sorted({os.path.splitext(f)[0] for f in os.listdir(mar)})) + ".\n"
    return t

def muestra(proyecto):
    ds = dias(proyecto)
    if not ds:
        return None, None
    p = jleer(os.path.join(proyecto, "entrada", ds[-1], "parte.json"), {})
    obras = p.get("obras", [])
    pick, vistos = [], set()
    for o in obras:
        k = (o.get("tipo"), bool(o.get("grupo")))
        if k not in vistos:
            vistos.add(k); pick.append(o)
    cortas = dict(p, obras=pick, avisos=(p.get("avisos") or [])[:3], _nota=f"MUESTRA: {len(pick)} de {len(obras)} obras del parte {ds[-1]} (una por tipo, más un grupo de rampas)")
    return cortas, ds[-1]

def historico(proyecto):
    filas = []
    for d in dias(proyecto):
        p = jleer(os.path.join(proyecto, "entrada", d, "parte.json"), {})
        act = [o for o in p.get("obras", []) if not o.get("grupo") and o.get("estado", "ejecucion") == "ejecucion"]
        c = {}
        for o in act:
            c[o.get("tipo")] = c.get(o.get("tipo"), 0) + 1
        filas.append([d, len(act), p.get("enEjecucion", ""), p.get("puestos", ""), p.get("finalizadas", "")] + [c.get(r[0], 0) for r in RUBROS] + [sum(o.get("rampas") or 0 for o in act if o.get("tipo") == "rampas")])
    return ["fecha", "obras_items", "encabezado_en_ejecucion", "puestos", "finalizadas"] + [r[0] for r in RUBROS] + ["rampas_total"], filas

def concatenar(titulo, rutas, proyecto, resumen):
    partes, total = [f"# {titulo}\n\nCódigo fuente concatenado. Los secretos están ocultos como `***OCULTO***`.\n"], 0
    for r in rutas:
        if not os.path.isfile(r):
            continue
        rel = os.path.relpath(r, proyecto).replace("\\", "/")
        txt, n = ocultar(leer(r))
        total += n
        lenguaje = {"py": "python", "js": "javascript", "json": "json", "html": "html", "md": "markdown"}.get(rel.rsplit(".", 1)[-1], "")
        partes.append(f"\n## {rel}\n\n~~~~{lenguaje}\n{txt.rstrip()}\n~~~~\n")
        resumen.append((rel, len(txt), n))
    return "".join(partes), total

def sin_outputs(ruta_nb, destino):
    nb = jleer(ruta_nb)
    if not nb:
        return False
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code":
            c["outputs"] = []; c["execution_count"] = None
        c.get("metadata", {}).pop("collapsed", None)
    escribir(destino, json.dumps(nb, ensure_ascii=False, indent=1))
    return True

def buscar_secretos(proyecto):
    saltear = ("node_modules", ".git", "_cache", os.sep + "salida", "para_proyecto", ".next")
    hallados = []
    for raiz, dirs, archivos in os.walk(proyecto):
        if any(s in raiz for s in saltear):
            dirs[:] = []; continue
        for a in archivos:
            ext = a.rsplit(".", 1)[-1].lower() if "." in a else ""
            r = os.path.join(raiz, a)
            if ext in ("md", "txt", "env", "json", "js", "py", "html", "csv", "yml", "yaml", "local") or a.startswith(".env"):
                try:
                    if os.path.getsize(r) < 400_000 and SOSPECHA.search(leer(r)):
                        hallados.append(os.path.relpath(r, proyecto))
                except OSError:
                    pass
    return hallados

# ---------------------------------------------------------------- principal
def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proyecto", default=os.path.dirname(aqui))
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    proy = os.path.abspath(a.proyecto)
    out = os.path.abspath(a.salida or os.path.join(proy, "para_proyecto", "subir"))
    print(f"Proyecto: {proy}\nSalida:   {out}\n")
    hechos = []

    escribir(os.path.join(out, "marca_resumen.md"), marca_md(proy)); hechos.append("marca_resumen.md")

    m, d = muestra(proy)
    if m:
        escribir(os.path.join(out, "muestra_parte.json"), json.dumps(m, ensure_ascii=False, indent=1)); hechos.append(f"muestra_parte.json (parte {d})")
    esq = "# Esquema de los datos del día\n\nVer `dic_campos_parte.csv`. Cada día: `entrada/<fecha>/lista.txt` (pegado del parte) → `parte.json` → `contenido.json` (redactado a mano) → `salida/<fecha>/tablero.html`.\n\n## Reglas de datos\n- No se inventa ningún dato: lo que falta queda fuera del texto.\n- Una esquina con varias rampas es UNA obra. `finalizadas` es un stock acumulado.\n- 1.100 cuadras y 2.100 rampas son planes ('prevé', 'contempla').\n- El circuito es dato interno; los textos hablan de barrios.\n\n## Campos\n" + "".join(f"- `{c[0]}` ({c[1]}): {c[2]}" + (f". Ej.: {c[3]}" if c[3] else "") + "\n" for c in CAMPOS)
    escribir(os.path.join(out, "esquema_parte.md"), esq); hechos.append("esquema_parte.md")

    cab, filas = historico(proy)
    if filas:
        escribir_csv(os.path.join(out, "historico_resumen.csv"), cab, filas); hechos.append(f"historico_resumen.csv ({len(filas)} días)")

    nombres = (jleer(os.path.join(proy, "data", "circuitos.json"), {}) or {}).get("circuitos", {})
    lst = {r[1]: r for r in LISTADO}
    codigos = sorted(set(nombres) | set(lst), key=lambda c: (int(re.match(r"\d+", c).group()), c))
    escribir_csv(os.path.join(out, "dic_circuitos.csv"), ["codigo", "nombre_validado", "nombre_listado", "grupo", "padron", "ultima_encuesta"],
                 [[c, nombres.get(c, ""), (lst.get(c) or ["", "", ""])[2].title() if c in lst else "", (lst.get(c) or [""])[0], (lst.get(c) or ["", "", "", ""])[3], (lst.get(c) or ["", "", "", "", ""])[4]] for c in codigos])
    hechos.append(f"dic_circuitos.csv ({len(codigos)} códigos)")

    bc = jleer(os.path.join(proy, "data", "barrio_circuito.json"), {}) or {}
    escribir_csv(os.path.join(out, "dic_barrio_circuito.csv"), ["barrio_normalizado", "codigo_circuito"], sorted(bc.items())); hechos.append("dic_barrio_circuito.csv")

    mem = jleer(os.path.join(proy, "data", "memorias.json"), {}) or {}
    escribir_csv(os.path.join(out, "dic_pavimentacion.csv"), ["clave", "sector", "barrio", "circuito", "cuadras", "plazo_dias"],
                 [[k, v.get("sector"), v.get("barrio"), v.get("circuito"), v.get("cuadras"), v.get("plazo")] for k, v in mem.items() if not k.startswith("_") and isinstance(v, dict)]); hechos.append("dic_pavimentacion.csv")

    escribir_csv(os.path.join(out, "dic_rubros.csv"), ["clave", "rubro", "eje", "regla", "como_se_nombra_en_texto"], RUBROS); hechos.append("dic_rubros.csv")
    escribir_csv(os.path.join(out, "dic_campos_parte.csv"), ["campo", "tipo", "descripcion", "ejemplo"], CAMPOS); hechos.append("dic_campos_parte.csv")

    rp = os.path.join(proy, "data", "reglas_parte.md")
    if os.path.isfile(rp):
        escribir(os.path.join(out, "reglas_parte.md"), leer(rp)); hechos.append("reglas_parte.md")

    res = []
    pipeline = sorted(glob.glob(os.path.join(proy, "tools", "*.py"))) + [os.path.join(proy, "deploy", n) for n in ("middleware.js", "vercel.json")] + [os.path.join(proy, ".claude", "launch.json")]
    t1, n1 = concatenar("Código del pipeline (Python y deploy)", pipeline, proy, res)
    escribir(os.path.join(out, "codigo_pipeline.md"), t1); hechos.append(f"codigo_pipeline.md ({len(t1) // 1024} KB)")
    t2, n2 = concatenar("Plantilla del tablero (HTML, CSS y JavaScript)", [os.path.join(proy, "tools", "plantilla.html")], proy, res)
    if "## tools/plantilla.html" in t2:
        escribir(os.path.join(out, "codigo_plantilla.md"), t2); hechos.append(f"codigo_plantilla.md ({len(t2) // 1024} KB, opcional)")

    nbs = [os.path.join(r, f) for r, ds_, fs in os.walk(proy) for f in fs if f.endswith(".ipynb") and "node_modules" not in r and "para_proyecto" not in r and ".ipynb_checkpoints" not in r]
    for nb in nbs:
        if sin_outputs(nb, os.path.join(out, "notebooks_sin_outputs", os.path.basename(nb))):
            hechos.append("notebooks_sin_outputs/" + os.path.basename(nb))
    if not nbs:
        hechos.append("(no hay notebooks .ipynb en el proyecto)")

    print("Generados:"); [print("  -", h) for h in hechos]
    print(f"\nSecretos ocultados en el código concatenado: {n1 + n2} coincidencias")
    for rel, largo, n in res:
        if n:
            print(f"  - {rel}: {n} valores ocultados")
    sec = buscar_secretos(proy)
    if sec:
        print("\nAVISO: estos archivos del proyecto parecen contener secretos. NO los subas al Proyecto de Claude ni al repo (se muestran solo las rutas):")
        for s in sec:
            print("  !", s)
    else:
        print("\nNo se detectaron archivos con secretos.")

if __name__ == "__main__":
    main()
