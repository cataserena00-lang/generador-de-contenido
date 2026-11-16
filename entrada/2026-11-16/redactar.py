"""Piezas redactadas a mano para el parte del 16/11/2026 (generales).
Corre:  python entrada/2026-11-16/redactar.py   ->  escribe contenido.json
Las cifras NO se escriben a mano: se calculan desde parte.json (mismo criterio que el tablero), así que si cambia
el conteo (por ejemplo, Plaza Hípica una o dos veces) basta con volver a correr parse_lista.py y este archivo.
Datos del parte: 110 obras publicables (el encabezado dice 111: el parte repite "Plaza Hípica" con el mismo documento,
y por la regla de deduplicar plazas por nombre se cuenta una vez), 971 puestos de trabajo directos. Bacheo en frío sin obras hoy.
Finalizadas: 281, del parte de finalizadas del 16/11 (finalizadas.txt). El desglose por tipo se cuenta de ese archivo:
no incluye pavimentación ni plazas, así que los textos de finalizadas no las nombran.
Pavimentación: 7 obras; 5 tienen memoria descriptiva (205 cuadras). Cooperativa Los Andes y El Renuevo y Ampliación
General Artigas no tienen memoria cargada: no suman cuadras.
Periódicos: no se redactan. En la ventana de 7 días hábiles solo están los partes del 12/11 y del 16/11; el tablero
lo avisa solo ("Faltan partes…").
Reglas: sin montos, sin "circuito" ni "seccional", sin barras, "Barrio" antes de cada barrio, sin citas
de funcionarios, planes con "prevé" o "contempla", X de hasta 280 caracteres.
"""
import json, os, re, unicodedata

LINK = "https://claude.ai/artifact/Xbxitst4ZDhQrsBjckBWRu"
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "parte.json"), encoding="utf-8"))

# ---------------------------------------------------------------- cifras del día (mismo criterio que la plantilla)
def norm(s): return re.sub(r"\s+", " ", "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()).strip()
ALIAS = {"Gral. Arenales": "General Arenales", "Gral. Paz": "General Paz", "Gral Paz": "General Paz", "Talleres (E)": "Talleres Este", "Ombu": "Ombú"}
def barrios(o):
    raw = o["barrio"] or (o["sector"] if o["tipo"] in ("mant", "pav") else None)
    return [ALIAS.get(b.strip(), b.strip()) for b in raw.split("/")] if raw else []
def nb(obras): return len({norm(b) for o in obras for b in barrios(o)})
def nf(n): return f"{n:,}".replace(",", ".")

R = [o for o in P["obras"] if not o["grupo"] and o["estado"] == "ejecucion"]
de = lambda *t: [o for o in R if o["tipo"] in t]
OBRAS, BARRIOS, PUESTOS, FIN = len(R), nb(R), nf(P["puestos"]), P["finalizadas"]
CALZ = de("mant", "frio", "bacheo", "rehab", "hormigon"); N_CALZ, B_CALZ = len(CALZ), nb(CALZ)
ML = sum(o["metricas"].get("ml", 0) for o in CALZ); M2 = sum(o["metricas"].get("m2", 0) for o in CALZ)
RAMP = de("rampas"); ESQ, RAMPAS = len(RAMP), sum(o["rampas"] for o in RAMP)
CENT = [o for o in RAMP if o["circuito"] == "1"]; OTRAS = [o for o in RAMP if o["circuito"] != "1"]
SALUD = [o for o in RAMP if "centro de salud" in norm(o["via"])]
PAV = de("pav"); B_PAV = nb(PAV); PAV_MEMO = [o for o in PAV if o["metricas"].get("cuadras")]; CUADRAS = sum(o["metricas"]["cuadras"] for o in PAV_MEMO)
PLAZ = de("plaza"); N_PLAZ, B_PLAZ = len(PLAZ), nb(PLAZ)
N_MANT, B_MANT = len(de("mant")), nb(de("mant"))
N_BACH, N_REHAB, N_HORM = len(de("bacheo")), len(de("rehab")), len(de("hormigon"))
assert len(de("frio")) == 0          # hoy no hay bacheo en frío: los textos no lo nombran
for k, v in dict(obras=OBRAS, barrios=BARRIOS, puestos=PUESTOS, fin=FIN, calzada=N_CALZ, b_calzada=B_CALZ, ml=ML, m2=M2, esquinas=ESQ,
                 rampas=RAMPAS, centro=(len(CENT), sum(o["rampas"] for o in CENT)), otras=(len(OTRAS), sum(o["rampas"] for o in OTRAS)),
                 salud=len(SALUD), pav=len(PAV), pav_memo=len(PAV_MEMO), cuadras=CUADRAS, plazas=N_PLAZ, b_plazas=B_PLAZ).items():
    print(f"  {k}: {v}")
N_CENT, R_CENT = len(CENT), sum(o["rampas"] for o in CENT)
N_OTR, R_OTR = len(OTRAS), sum(o["rampas"] for o in OTRAS)
# ---------------------------------------------------------------- finalizadas por tipo (parte de finalizadas del día)
def finalizadas():
    t = open(os.path.join(HERE, "finalizadas.txt"), encoding="utf-8").read()
    sec, c, rampas = None, {}, 0
    for l in t.splitlines():
        u = l.strip().upper()
        for k, v in (("MANTENIMIENTO", "mant"), ("RAMPAS", "rampas"), ("REHABILITACIÓN CON ASFALTO", "rehab"), ("BACHEO CON ASFALTO", "bacheo"), ("REHABILITACIÓN Y BACHEO", "hormigon")):
            if u.startswith(k): sec = v
        if sec and re.match(r"^\d+\.\s", l.strip()):
            c[sec] = c.get(sec, 0) + 1
            m = re.search(r"·\s*(\d+)\s*rampa", l); rampas += int(m.group(1)) if m else 0
    total = int(re.search(r"Finalizadas:\s*(\d+)", t).group(1))
    assert sum(c.values()) == total == FIN, (c, total, FIN)        # la lista, el encabezado y data/finalizadas.json coinciden
    return c, rampas
FC, FRAMP = finalizadas()
print("  finalizadas por tipo:", FC, "rampas:", FRAMP)
FIN_DET = (f"{FC['bacheo']} de bacheo con asfalto, {FC['mant']} de mantenimiento de calles de tierra, {FC['hormigon']} de "
           f"rehabilitación y bacheo con hormigón, {FC['rampas']} de accesibilidad, con {FRAMP} rampas, y {FC['rehab']} de "
           "rehabilitación con asfalto")
PALABRA = {2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete"}

def seg(i):  # párrafo de "Seguimiento diario", redactado distinto en cada pieza
    t = [
        ("Seguimiento diario de las obras en la ciudad de Córdoba",
         f"A través de una herramienta digital, {LINK}, los vecinos pueden consultar, de manera sencilla y con actualización diaria, el estado de las obras que se ejecutan en distintos sectores de la ciudad, tanto las que están en marcha como las que ya fueron finalizadas."),
        ("Cómo seguir las obras día a día",
         f"El avance de cada intervención puede consultarse en línea, con datos que se actualizan todos los días, en {LINK}. La herramienta reúne las obras en ejecución y las terminadas en los distintos barrios de la ciudad."),
        ("Las obras, al alcance de todos",
         f"Quienes quieran saber qué se hace en su zona pueden ingresar a {LINK}: allí se publica, con actualización diaria, el estado de las obras de Córdoba, tanto las que avanzan como las que ya se completaron."),
        ("Información abierta sobre las obras",
         f"La ciudad cuenta con una herramienta digital de consulta pública, {LINK}, que muestra día a día el estado de las obras, en marcha y finalizadas, en los distintos sectores de Córdoba."),
        ("Seguimiento diario de las obras",
         f"¿Qué se está haciendo hoy en tu barrio? La respuesta está en {LINK}, una herramienta digital que se actualiza todos los días y muestra el estado de las obras de la ciudad, tanto las que están en marcha como las ya finalizadas."),
        ("Consulta pública de las obras",
         f"El estado de cada obra puede verse en cualquier momento en {LINK}. La información se actualiza a diario e incluye las intervenciones que avanzan y las que ya concluyeron en los distintos sectores de Córdoba."),
        ("Las obras de la ciudad, en una sola herramienta",
         f"Mantenerse informado es sencillo: en {LINK} se concentra, con actualización diaria, el seguimiento de las obras en ejecución y finalizadas en la ciudad de Córdoba."),
        ("Obras en marcha y obras terminadas, a un clic",
         f"Con una herramienta digital de acceso abierto, {LINK}, cualquier vecino puede revisar día a día cómo avanzan las obras de su sector y cuáles ya fueron finalizadas."),
        ("Seguimiento para todos los vecinos",
         f"Para facilitar el seguimiento ciudadano, la herramienta {LINK} permite consultar, con actualización diaria, el estado de las obras de la ciudad, en marcha y finalizadas."),
    ]
    return t[i % len(t)]

_n = [5]   # arranca en otra variante del párrafo de seguimiento que el parte anterior (12/11 arrancó en 2)

def gac(titulo, bajada, lead, secciones, cierre):
    i = _n[0]; _n[0] += 1
    partes = [titulo, "\n".join("• " + b for b in bajada), lead]
    for h, ps in secciones:
        partes.append(h); partes.extend(ps)
    if cierre: partes.append(cierre)
    h, p = seg(i); partes += [h, p, "Material de descarga: [pegar enlace]"]
    return "\n\n".join(partes)

G = {}
MUNI = "El Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba,"

# ---------------------------------------------------------------- 1. el día en números
G["g_total"] = dict(
    titulos=[
        f"Córdoba tiene {OBRAS} obras en ejecución en {BARRIOS} barrios de la ciudad",
        f"{OBRAS} obras en marcha y {PUESTOS} puestos de trabajo directos en la ciudad de Córdoba",
        f"La obra pública avanza hoy en {BARRIOS} barrios de Córdoba",
    ],
    ig=f"🏗️ {OBRAS} OBRAS EN EJECUCIÓN EN LA CIUDAD\n\n"
       f"Hoy hay {OBRAS} obras en marcha en {BARRIOS} barrios de Córdoba: calles que se reparan y rehabilitan, esquinas que "
       "suman rampas, plazas que se renuevan y cuadras que se pavimentan.\n\n"
       f"Los frentes de obra generan {PUESTOS} puestos de trabajo directos.\n\n"
       "Conocé cómo avanzan las obras de tu barrio y compartí esta publicación con tus vecinos.\n\n"
       "#CórdobaMejora #CallePorCalle #HacerParaCrecer",
    x=f"🏗️ Córdoba tiene hoy {OBRAS} obras en marcha en {BARRIOS} barrios, con {PUESTOS} puestos de trabajo directos. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        f"Córdoba tiene {OBRAS} obras en ejecución en {BARRIOS} barrios de la ciudad",
        [f"Las obras generan {PUESTOS} puestos de trabajo directos.",
         f"Hay {N_CALZ} frentes de reparación y rehabilitación de calzada en {B_CALZ} barrios.",
         f"Se trabaja en {ESQ} esquinas para construir {RAMPAS} rampas y en {N_PLAZ} plazas de {B_PLAZ} barrios."],
        f"{MUNI} mantiene hoy {OBRAS} obras en ejecución en {BARRIOS} barrios de la ciudad de Córdoba. Los trabajos "
        "abarcan el mantenimiento y la rehabilitación de calles, la pavimentación, la accesibilidad y la renovación de "
        "espacios públicos.",
        [("Qué se está haciendo",
          [f"Las intervenciones sobre la calzada suman {N_CALZ} obras en {B_CALZ} barrios. Las memorias de los frentes "
           f"que informan magnitudes suman {nf(M2)} metros cuadrados y {nf(ML)} metros lineales de calzada.",
           f"En accesibilidad, se trabaja en {ESQ} esquinas para construir {RAMPAS} rampas.",
           f"La pavimentación avanza con {len(PAV)} obras en {B_PAV} barrios.",
           f"La renovación de espacios públicos alcanza a {N_PLAZ} plazas de {B_PLAZ} barrios."]),
         ("El trabajo que generan las obras",
          [f"Los frentes abiertos en la ciudad sostienen {PUESTOS} puestos de trabajo directos."])],
        None),
)

# ---------------------------------------------------------------- 2. empleo
G["g_empleo"] = dict(
    titulos=[
        f"La obra pública sostiene {PUESTOS} puestos de trabajo directos en la ciudad de Córdoba",
        f"{PUESTOS} trabajadores en los frentes de obra de Córdoba",
        "Las obras de la ciudad, una fuente de trabajo para los cordobeses",
    ],
    ig=f"👷 {PUESTOS} PUESTOS DE TRABAJO DIRECTOS\n\n"
       f"Las {OBRAS} obras que hoy avanzan en {BARRIOS} barrios de Córdoba sostienen {PUESTOS} puestos de trabajo directos: "
       "cuadrillas que reparan calles, construyen rampas, pavimentan cuadras y renuevan plazas.\n\n"
       "Compartí esta publicación y seguí cómo avanzan las obras en la ciudad.\n\n"
       "#CórdobaMejora #HacerParaCrecer",
    x=f"👷 {PUESTOS} puestos de trabajo directos sostienen hoy las {OBRAS} obras en marcha en la ciudad de Córdoba. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        f"La obra pública sostiene {PUESTOS} puestos de trabajo directos en la ciudad de Córdoba",
        [f"Son {OBRAS} obras en ejecución en {BARRIOS} barrios.",
         "El trabajo se reparte entre los frentes de calzada, accesibilidad, pavimentación y plazas."],
        f"{MUNI} informa que las {OBRAS} obras en ejecución en la ciudad sostienen hoy {PUESTOS} puestos de trabajo "
        "directos.",
        [("Trabajo en cada frente",
          ["Los puestos se distribuyen entre las cuadrillas de mantenimiento y bacheo, los equipos de rehabilitación "
           "de calzada, las obras de pavimentación, la construcción de rampas y la renovación de plazas."]),
         ("Inversión que se traduce en empleo",
          ["La continuidad de los frentes de obra se apoya en el orden de las cuentas públicas, que permite sostener "
           "la inversión en infraestructura."])],
        None),
)

# ---------------------------------------------------------------- 3. accesibilidad
G["g_accesible"] = dict(
    titulos=[
        f"Córdoba Accesible: {RAMPAS} rampas en ejecución en {ESQ} esquinas de la ciudad",
        f"Más accesibilidad: {ESQ} esquinas en obra para sumar {RAMPAS} rampas",
        "Rampas en la zona céntrica y en centros de salud de la ciudad",
    ],
    ig=f"♿ {RAMPAS} RAMPAS EN EJECUCIÓN\n\n"
       f"Córdoba Accesible avanza en {ESQ} esquinas de la ciudad, donde se construyen {RAMPAS} rampas. Además de la zona "
       f"céntrica, hay esquinas en obra en otros sectores y en {PALABRA[len(SALUD)]} centros de salud.\n\n"
       "Cada rampa es una barrera menos para quienes se mueven en silla de ruedas, con bastón o con un cochecito.\n\n"
       "#CórdobaAccesible #HacerParaCrecer",
    x=f"♿ Córdoba Accesible avanza con {RAMPAS} rampas en {ESQ} esquinas de la ciudad, incluidos {PALABRA[len(SALUD)]} centros de "
      "salud. #CórdobaAccesible #HacerParaCrecer",
    gac=gac(
        f"Córdoba Accesible: {RAMPAS} rampas en ejecución en {ESQ} esquinas de la ciudad",
        [f"En la zona céntrica se trabaja en {N_CENT} esquinas, con {R_CENT} rampas.",
         f"Otras {N_OTR} esquinas suman {R_OTR} rampas, entre ellas las de {PALABRA[len(SALUD)]} centros de salud.",
         f"El programa prevé {nf(P['programaRampas']['total'])} rampas en toda la ciudad."],
        f"{MUNI} ejecuta obras de accesibilidad en {ESQ} esquinas de la ciudad, donde se construyen {RAMPAS} rampas en "
        "el marco del programa Córdoba Accesible.",
        [("Dónde se trabaja",
          [f"La zona céntrica concentra {N_CENT} esquinas en obra, con {R_CENT} rampas. Las otras {N_OTR} esquinas, con "
           f"{R_OTR} rampas, están en distintos sectores de la ciudad, e incluyen los accesos de {PALABRA[len(SALUD)]} "
           "centros de salud.",
           "Cada esquina se interviene como una obra, con la cantidad de rampas que requiere su geometría."]),
         ("Un programa para toda la ciudad",
          [f"El programa contempla {nf(P['programaRampas']['total'])} rampas en total: "
           f"{nf(P['programaRampas']['nuevas'])} nuevas y {P['programaRampas']['reparadas']} reparaciones. De las nuevas, "
           f"{nf(P['programaRampas']['en_esquinas_sin_rampa'])} corresponden a esquinas que hoy no tienen ninguna rampa.",
           "El objetivo es que las personas con movilidad reducida puedan desplazarse con autonomía por la ciudad."])],
        None),
)

# ---------------------------------------------------------------- 4. calzada
G["g_calle"] = dict(
    titulos=[
        f"Calle por Calle: {N_CALZ} obras de calzada en ejecución en {B_CALZ} barrios",
        f"Mantenimiento, bacheo y rehabilitación de calles avanzan en {B_CALZ} barrios de Córdoba",
        f"{N_CALZ} frentes de obra para mejorar la circulación en la ciudad",
    ],
    ig=f"🛣️ {N_CALZ} OBRAS DE CALZADA EN MARCHA\n\n"
       f"Calle por Calle avanza hoy en {B_CALZ} barrios de Córdoba, con {N_CALZ} frentes de mantenimiento de calles, bacheo "
       "con asfalto, rehabilitación con asfalto y rehabilitación y bacheo con hormigón.\n\n"
       f"Las memorias de obra informan {nf(M2)} metros cuadrados y {nf(ML)} metros lineales de calzada intervenida.\n\n"
       "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    x=f"🛣️ Calle por Calle: {N_CALZ} obras de calzada avanzan hoy en {B_CALZ} barrios de Córdoba. "
      "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        f"Calle por Calle: {N_CALZ} obras de calzada en ejecución en {B_CALZ} barrios",
        ["Las intervenciones incluyen mantenimiento, bacheo y rehabilitación de calzada.",
         f"Las memorias informan {nf(M2)} metros cuadrados y {nf(ML)} metros lineales intervenidos."],
        f"{MUNI} ejecuta {N_CALZ} obras de calzada en {B_CALZ} barrios de la ciudad de Córdoba. Los frentes abarcan "
        "mantenimiento de calles, bacheo con asfalto, rehabilitación con asfalto y rehabilitación y bacheo con "
        "hormigón.",
        [("Dónde se trabaja",
          [f"Las cuadrillas de mantenimiento trabajan en {B_MANT} barrios. El bacheo con asfalto suma {N_BACH} frentes, "
           f"la rehabilitación con asfalto {N_REHAB} y la rehabilitación y bacheo con hormigón, {N_HORM}.",
           "Las magnitudes de cada obra salen de las memorias descriptivas de los equipos técnicos; donde no hay "
           "dato, el texto no lleva magnitud."]),
         ("Calles en mejores condiciones",
          ["Las tareas recuperan la calzada y mejoran la circulación de vecinos, transporte y servicios en cada "
           "sector de la ciudad."])],
        None),
)

# ---------------------------------------------------------------- 5. pavimentación
G["g_cuadras"] = dict(
    titulos=[
        f"La pavimentación avanza en {B_PAV} barrios de Córdoba",
        f"{PALABRA[len(PAV)].capitalize()} obras de pavimentación en marcha en la ciudad",
        "Calles de tierra que pasan a ser calles pavimentadas",
    ],
    ig=f"🚧 PAVIMENTACIÓN EN {B_PAV} BARRIOS\n\n"
       f"Las {len(PAV)} obras de pavimentación avanzan en {B_PAV} barrios de la ciudad de Córdoba. Los {PALABRA[len(PAV_MEMO)]} "
       f"proyectos con memoria descriptiva contemplan {CUADRAS} cuadras.\n\n"
       "Seguí el avance de las obras de tu barrio.\n\n"
       "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    x=f"🚧 La pavimentación avanza en {B_PAV} barrios de Córdoba: calles de tierra que pasan a ser calles pavimentadas. "
      "#CallePorCalle #HacerParaCrecer",
    gac=gac(
        f"La pavimentación avanza en {B_PAV} barrios de Córdoba",
        [f"Hay {len(PAV)} obras de pavimentación en ejecución.",
         f"Los {PALABRA[len(PAV_MEMO)]} proyectos con memoria descriptiva contemplan {CUADRAS} cuadras."],
        f"{MUNI} ejecuta {len(PAV)} obras de pavimentación en {B_PAV} barrios de la ciudad de Córdoba.",
        [("Qué significa pavimentar un barrio",
          ["La pavimentación cambia la vida diaria de quienes circulan por calles de tierra: mejora el acceso del "
           "transporte y de los servicios de emergencia, ordena el escurrimiento del agua y reduce el polvo.",
           f"Las {CUADRAS} cuadras informadas corresponden al proyecto de las obras con memoria descriptiva y no al "
           "avance alcanzado."]),
         ("Un plan de largo alcance",
          ["El plan de pavimentación prevé 1.100 cuadras en toda la ciudad."])],
        None),
)

# ---------------------------------------------------------------- 6. plazas
G["g_plazas"] = dict(
    titulos=[
        f"Nos vemos en la Plaza: {N_PLAZ} espacios públicos en renovación en {B_PLAZ} barrios",
        f"La renovación de plazas llega a {B_PLAZ} barrios de Córdoba",
        f"{N_PLAZ} plazas en obra para el encuentro de los vecinos",
    ],
    ig=f"🌳 {N_PLAZ} PLAZAS EN RENOVACIÓN\n\n"
       f"Hay {N_PLAZ} plazas y plazoletas en obra en {B_PLAZ} barrios de Córdoba, para que vuelvan a ser punto de encuentro "
       "de los vecinos.\n\n"
       "Nos vemos en la Plaza.\n\n"
       "#NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer",
    x=f"🌳 Nos vemos en la Plaza: {N_PLAZ} plazas y plazoletas en renovación en {B_PLAZ} barrios de Córdoba. "
      "#NosVemosEnLaPlaza #HacerParaCrecer",
    gac=gac(
        f"Nos vemos en la Plaza: {N_PLAZ} espacios públicos en renovación en {B_PLAZ} barrios",
        ["Las obras alcanzan a plazas y plazoletas de distintos sectores de la ciudad.",
         "Parte de las intervenciones se ejecutan junto a la Empresa Provincial de Energía de Córdoba."],
        f"{MUNI} renueva {N_PLAZ} plazas y plazoletas en {B_PLAZ} barrios de la ciudad de Córdoba.",
        [("Espacios públicos para el encuentro",
          ["La renovación busca que cada plaza vuelva a funcionar como lugar de encuentro del barrio.",
           "Varias de las intervenciones se ejecutan junto a la Empresa Provincial de Energía de Córdoba."]),
         ("En distintos sectores de la ciudad",
          ["Las obras llegan a barrios del norte, del sur, del este y del oeste de Córdoba, y también al centro de la "
           "ciudad."])],
        None),
)

# ---------------------------------------------------------------- 7. planes
G["g_acum"] = dict(
    titulos=[
        "Pavimento y accesibilidad: los planes que ordenan la obra pública en Córdoba",
        "Córdoba prevé 1.100 cuadras de pavimento y 2.100 rampas para toda la ciudad",
        "Dos planes de largo alcance para la infraestructura de la ciudad",
    ],
    ig="📍 LOS PLANES QUE ORDENAN LA OBRA\n\n"
       "El plan de pavimentación prevé 1.100 cuadras para toda la ciudad de Córdoba y el programa Córdoba Accesible "
       "contempla 2.100 rampas: 2.000 nuevas y 100 reparaciones.\n\n"
       "Cada obra que se abre en un barrio forma parte de esa planificación.\n\n"
       "#CórdobaMejora #CórdobaAccesible #HacerParaCrecer",
    x="📍 Córdoba prevé 1.100 cuadras de pavimento y el programa Córdoba Accesible contempla 2.100 rampas para toda la "
      "ciudad. #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Pavimento y accesibilidad: los planes que ordenan la obra pública en Córdoba",
        ["El plan de pavimentación prevé 1.100 cuadras.",
         "El programa Córdoba Accesible contempla 2.100 rampas: 2.000 nuevas y 100 reparaciones."],
        f"{MUNI} organiza la obra pública de la ciudad en torno a dos planes de largo alcance: la pavimentación de "
        "1.100 cuadras y la construcción de 2.100 rampas.",
        [("Pavimentación",
          ["El plan prevé 1.100 cuadras en barrios que hoy no tienen asfalto."]),
         ("Accesibilidad",
          ["El programa Córdoba Accesible contempla 2.100 rampas: 2.000 nuevas y 100 reparaciones. De las nuevas, "
           "1.317 corresponden a esquinas que hoy no cuentan con ninguna rampa."]),
         ("Metas y avance",
          ["Las cifras de los planes corresponden a las metas previstas y no al avance alcanzado. El estado de cada "
           "obra se informa, día a día, en el seguimiento público."])],
        None),
)

# ---------------------------------------------------------------- 8. finalizadas
G["g_fin"] = dict(
    titulos=[
        f"Córdoba suma {FIN} obras finalizadas",
        f"{FIN} obras terminadas en calles y esquinas de la ciudad de Córdoba",
        f"{FIN} obras finalizadas y otras {OBRAS} en ejecución en Córdoba",
    ],
    ig=f"✅ {FIN} OBRAS FINALIZADAS\n\n"
       f"La ciudad de Córdoba suma {FIN} obras finalizadas: {FIN_DET}.\n\n"
       f"Y hoy hay otras {OBRAS} obras en ejecución en {BARRIOS} barrios.\n\n"
       "#CórdobaMejora #CallePorCalle #HacerParaCrecer",
    x=f"✅ Córdoba suma {FIN} obras finalizadas y hoy tiene otras {OBRAS} en ejecución en {BARRIOS} barrios. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        f"Córdoba suma {FIN} obras finalizadas",
        [f"{FC['bacheo']} obras de bacheo con asfalto y {FC['mant']} de mantenimiento de calles de tierra.",
         f"{FC['hormigon']} obras de rehabilitación y bacheo con hormigón y {FC['rehab']} de rehabilitación con asfalto.",
         f"{FC['rampas']} obras de accesibilidad, con {FRAMP} rampas.",
         f"En paralelo, hay {OBRAS} obras en ejecución en {BARRIOS} barrios."],
        f"{MUNI} informa que la ciudad suma {FIN} obras finalizadas. El número corresponde al total alcanzado hasta "
        "la fecha.",
        [("Qué se terminó",
          [f"Las obras finalizadas comprenden {FIN_DET}."]),
         ("La obra continúa",
          [f"Mientras se suman obras finalizadas, hay {OBRAS} frentes abiertos en {BARRIOS} barrios, con {PUESTOS} "
           "puestos de trabajo directos."])],
        None),
)

# ---------------------------------------------------------------- 9. equilibrio fiscal
G["g_fiscal"] = dict(
    titulos=[
        "Con equilibrio fiscal, la obra pública sigue en marcha en la ciudad de Córdoba",
        "El orden de las cuentas, convertido en obras para los barrios",
        "Cuentas en orden para sostener la infraestructura de Córdoba",
    ],
    ig="📊 CUENTAS EN ORDEN, OBRA EN MARCHA\n\n"
       f"Hoy hay {OBRAS} obras en ejecución en {BARRIOS} barrios de Córdoba y {PUESTOS} puestos de trabajo directos. "
       "El equilibrio fiscal es lo que permite sostener ese ritmo de inversión en infraestructura.\n\n"
       "#CórdobaMejora #HacerParaCrecer",
    x=f"📊 Con las cuentas en orden, Córdoba sostiene {OBRAS} obras en ejecución y {PUESTOS} puestos de trabajo directos. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Con equilibrio fiscal, la obra pública sigue en marcha en la ciudad de Córdoba",
        [f"Hay {OBRAS} obras en ejecución en {BARRIOS} barrios.",
         f"Las obras generan {PUESTOS} puestos de trabajo directos.",
         f"La ciudad acumula {FIN} obras finalizadas."],
        f"{MUNI} sostiene un plan de obra pública que hoy alcanza {OBRAS} frentes en {BARRIOS} barrios de la ciudad. "
        "La continuidad de ese plan se apoya en el equilibrio fiscal.",
        [("Previsibilidad para planificar",
          ["El orden de las cuentas públicas permite programar las obras y sostener los frentes abiertos en los "
           "barrios."]),
         ("Obra en todos los frentes",
          ["El plan abarca mantenimiento y rehabilitación de calzada, pavimentación, accesibilidad y renovación de "
           "plazas."])],
        None),
)

# ---------------------------------------------------------------- línea política, una por pieza y variada (distinta de la del 12/11)
POL = {
  "g_total":     ("El equilibrio fiscal hace posible que la obra pública llegue a todos los cordobeses.", "Equilibrio fiscal, obra en cada barrio."),
  "g_empleo":    ("Con las cuentas en orden, la inversión en infraestructura también es trabajo para los cordobeses.", "Cuentas ordenadas, más trabajo."),
  "g_accesible": ("Con equilibrio fiscal, Córdoba invierte en una ciudad accesible para todos los cordobeses.", "Cuentas en orden, ciudad accesible."),
  "g_calle":     ("El equilibrio fiscal sostiene la inversión en las calles de todos los cordobeses.", "Equilibrio fiscal, calles mejores."),
  "g_cuadras":   ("Las cuentas en orden permiten llevar pavimento a los barrios de todos los cordobeses.", "Con cuentas en orden, pavimento."),
  "g_plazas":    ("Con equilibrio fiscal, los espacios públicos de todos los cordobeses se renuevan.", "Equilibrio fiscal que se hace plaza."),
  "g_acum":      ("Planificar a largo plazo la infraestructura de todos los cordobeses es posible con las cuentas en orden.", "Cuentas en orden para planificar."),
  "g_fin":       ("Cada obra terminada muestra que el equilibrio fiscal sostiene la inversión de todos los cordobeses.", "Equilibrio fiscal que se ve."),
  "g_fiscal":    ("El modelo cordobés elige el equilibrio fiscal para sostener la inversión en infraestructura de todos los cordobeses.", "Orden fiscal, obra para todos."),
}
# ---------------------------------------------------------------- placas: las cifras de la placa coinciden con las del texto
G["g_calle"]["placa"] = dict(valor=str(N_CALZ), etiqueta="Obras de calzada en ejecución", sub=f"En {B_CALZ} barrios de la ciudad", extra="")
G["g_plazas"]["placa"] = dict(valor=str(N_PLAZ), etiqueta="Plazas en renovación", sub=f"En {B_PLAZ} barrios de la ciudad", extra="")

def meter(pieza, ig_line, x_line):
    ig = pieza["ig"]; i = ig.rfind("\n\n#"); pieza["ig"] = ig[:i] + "\n\n" + ig_line + ig[i:]
    x = pieza["x"]; j = x.find(" #"); cand = x[:j] + " " + x_line + x[j:]
    if len(cand) <= 280: pieza["x"] = cand
for k, (a, b) in POL.items():
    meter(G[k], a, b)

json.dump(dict(generales=G, periodicos={}), open(os.path.join(HERE, "contenido.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("generales:", len(G), "periodicos: 0 (en la ventana solo están los partes del 12/11 y del 16/11)")
for k, v in G.items():
    assert len(v["x"]) <= 280, (k, len(v["x"]))
    assert POL[k][1] in v["x"] or "cuentas en orden" in v["x"].lower(), ("sin línea política en X", k)
    assert POL[k][0] in v["ig"], ("sin línea política en IG", k)
    for t in [v["ig"], v["x"], v["gac"]] + v["titulos"]:
        assert "/" not in t.replace(LINK, ""), k
        assert not re.search(r"circuito|seccional|\$", t, re.I), k
print("X más largo:", max(len(v["x"]) for v in G.values()), "caracteres")
