"""Piezas redactadas a mano para el parte del 13/11/2026 (generales).
Corre:  python entrada/2026-11-13/redactar.py   ->  escribe contenido.json
Datos del parte: 110 obras en ejecución (el encabezado dice 112; el parte repite Plaza Benjamín Viel I y
Plaza Benjamín Viel II, y cada una se cuenta una sola vez), 960 puestos de trabajo directos, 43 barrios,
192 obras finalizadas (stock que se arrastra del 29/10). Por tipo: 51 esquinas con 119 rampas, 26 obras de
calzada en 24 barrios (515 metros lineales y 4.220 m²), 7 obras de pavimentación con 205 cuadras de proyecto,
25 plazas en 12 barrios y el alumbrado LED de Parque Liceo.
Periódicos: no se redactan. Solo hay partes del 12/11 y del 13/11, así que las ventanas de 7 y 10 días hábiles
siguen incompletas; el tablero lo avisa solo ("Faltan partes…").
Reglas: sin montos, sin "circuito" ni "seccional", sin barras, "Barrio" antes de cada barrio, sin citas
de funcionarios, planes con "prevé" o "contempla", X de hasta 280 caracteres.
"""
import json, os

LINK = "https://claude.ai/artifact/Xbxitst4ZDhQrsBjckBWRu"
HERE = os.path.dirname(os.path.abspath(__file__))

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

_n = [6]   # arranca en otra variante del párrafo de seguimiento que el parte anterior

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
        "Córdoba tiene 110 obras en ejecución en 43 barrios de la ciudad",
        "110 obras en marcha y 960 puestos de trabajo directos en la ciudad de Córdoba",
        "La obra pública avanza hoy en 43 barrios de Córdoba",
    ],
    ig="🏗️ 110 OBRAS EN EJECUCIÓN EN LA CIUDAD\n\n"
       "Hoy hay 110 obras en marcha en 43 barrios de Córdoba: calles que se rehabilitan, rampas que se construyen, "
       "plazas que se renuevan y cuadras que se pavimentan.\n\n"
       "Las obras generan 960 puestos de trabajo directos.\n\n"
       "Seguí el avance de las obras de tu barrio y compartí esta publicación con tus vecinos.\n\n"
       "#CórdobaMejora #CallePorCalle #HacerParaCrecer",
    x="🏗️ Hoy hay 110 obras en marcha en 43 barrios de Córdoba, con 960 puestos de trabajo directos. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Córdoba tiene 110 obras en ejecución en 43 barrios de la ciudad",
        ["Las obras generan 960 puestos de trabajo directos.",
         "Hay 26 frentes de reparación y rehabilitación de calzada en 24 barrios.",
         "Se trabaja en 51 esquinas para construir 119 rampas y en 25 plazas de 12 barrios."],
        f"{MUNI} mantiene hoy 110 obras en ejecución en 43 barrios de la ciudad de Córdoba. El plan combina "
        "mantenimiento y bacheo de calles, rehabilitación de calzada, pavimentación, accesibilidad y renovación de "
        "espacios públicos.",
        [("Qué se está haciendo",
          ["Las intervenciones sobre la calzada suman 26 obras en 24 barrios, con 515 metros lineales y 4.220 metros "
           "cuadrados informados en las memorias de cada frente de trabajo.",
           "En accesibilidad, se trabaja en 51 esquinas para construir 119 rampas.",
           "La pavimentación avanza en 7 barrios, con proyectos que contemplan 205 cuadras.",
           "La renovación de espacios públicos alcanza a 25 plazas de 12 barrios."]),
         ("El trabajo que generan las obras",
          ["Los frentes abiertos en la ciudad sostienen 960 puestos de trabajo directos."])],
        None),
)

# ---------------------------------------------------------------- 2. empleo
G["g_empleo"] = dict(
    titulos=[
        "Las obras en ejecución sostienen 960 puestos de trabajo directos en Córdoba",
        "960 puestos de trabajo directos en los frentes de obra de la ciudad",
        "La obra pública como motor de trabajo en la ciudad de Córdoba",
    ],
    ig="👷 960 PUESTOS DE TRABAJO DIRECTOS\n\n"
       "Detrás de cada calle que se repara, de cada rampa y de cada plaza que se renueva hay trabajo cordobés: "
       "las 110 obras en ejecución sostienen hoy 960 puestos de trabajo directos en la ciudad.\n\n"
       "Compartí esta publicación y seguí cómo avanza la obra en tu barrio.\n\n"
       "#CórdobaMejora #HacerParaCrecer",
    x="👷 Las 110 obras en ejecución en la ciudad de Córdoba sostienen hoy 960 puestos de trabajo directos. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Las obras en ejecución sostienen 960 puestos de trabajo directos en Córdoba",
        ["Son 110 obras en marcha en 43 barrios de la ciudad.",
         "El trabajo alcanza a los frentes de calzada, accesibilidad, pavimentación y plazas."],
        f"{MUNI} informa que las obras que se ejecutan en la ciudad sostienen hoy 960 puestos de trabajo directos. "
        "La cifra corresponde a los 110 frentes abiertos en 43 barrios.",
        [("Trabajo en cada frente de obra",
          ["Los puestos se distribuyen entre las cuadrillas de mantenimiento y bacheo, los equipos de rehabilitación "
           "de calzada, las obras de pavimentación, la construcción de rampas y la renovación de plazas."]),
         ("Una inversión que se sostiene",
          ["El ritmo de las obras se apoya en el orden de las cuentas públicas, que permite sostener la inversión en "
           "infraestructura sin interrupciones."])],
        None),
)

# ---------------------------------------------------------------- 3. accesibilidad
G["g_accesible"] = dict(
    titulos=[
        "Córdoba construye 119 rampas en 51 esquinas de la ciudad",
        "Accesibilidad: 51 esquinas en obra para sumar 119 rampas",
        "Más rampas para una ciudad que se mueve sin barreras",
    ],
    ig="♿ 116 RAMPAS EN EJECUCIÓN\n\n"
       "Hay 51 esquinas en obra en la ciudad de Córdoba para construir 119 rampas. Cada esquina intervenida es una "
       "barrera menos para quienes se mueven en silla de ruedas, con bastón o con un cochecito.\n\n"
       "Una Córdoba inclusiva, pensada para todos.\n\n"
       "#CórdobaAccesible #HacerParaCrecer",
    x="♿ Hay 51 esquinas en obra en Córdoba para construir 119 rampas. Una ciudad que se mueve sin barreras. "
      "#CórdobaAccesible #HacerParaCrecer",
    gac=gac(
        "Córdoba construye 119 rampas en 51 esquinas de la ciudad",
        ["Las obras de accesibilidad alcanzan hoy a 51 esquinas.",
         "El programa Córdoba Accesible prevé 2.100 rampas en toda la ciudad."],
        f"{MUNI} ejecuta obras de accesibilidad en 51 esquinas de la ciudad, donde se construyen 119 rampas. "
        "Las intervenciones forman parte del programa Córdoba Accesible.",
        [("Un programa para toda la ciudad",
          ["El programa contempla 2.100 rampas en total: 2.000 nuevas y 100 reparaciones. De las nuevas, 1.317 "
           "corresponden a esquinas que hoy no tienen ninguna rampa.",
           "Cada esquina se interviene como una obra, con la cantidad de rampas que requiere su geometría."]),
         ("Accesibilidad como política pública",
          ["Las rampas se suman a las veredas, los cruces y los espacios públicos adaptados, con el objetivo de que "
           "las personas con movilidad reducida puedan desplazarse con autonomía por la ciudad."])],
        None),
)

# ---------------------------------------------------------------- 4. calzada
G["g_calle"] = dict(
    titulos=[
        "Hay 26 obras de calzada en ejecución en 24 barrios de Córdoba",
        "Calle por calle: 26 frentes de reparación y rehabilitación en la ciudad",
        "Bacheo, mantenimiento y rehabilitación avanzan en 24 barrios de Córdoba",
    ],
    ig="🛣️ 28 OBRAS DE CALZADA EN MARCHA\n\n"
       "El plan Calle por Calle avanza hoy en 24 barrios de Córdoba, con 26 frentes de mantenimiento, bacheo en frío, "
       "bacheo con asfalto, rehabilitación con asfalto y rehabilitación con hormigón.\n\n"
       "Las memorias de obra informan 515 metros lineales y 4.220 metros cuadrados de calzada intervenida.\n\n"
       "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    x="🛣️ Calle por Calle avanza hoy con 26 obras de calzada en 24 barrios de Córdoba. "
      "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Hay 26 obras de calzada en ejecución en 24 barrios de Córdoba",
        ["Las intervenciones incluyen mantenimiento, bacheo y rehabilitación de calzada.",
         "Las memorias informan 515 metros lineales y 4.220 metros cuadrados intervenidos."],
        f"{MUNI} ejecuta 26 obras de calzada en 24 barrios de la ciudad de Córdoba. Los frentes abarcan "
        "mantenimiento de calles, bacheo en frío, bacheo con asfalto, rehabilitación con asfalto y rehabilitación y "
        "bacheo con hormigón.",
        [("Dónde se trabaja",
          ["Las cuadrillas de mantenimiento trabajan en 7 barrios y las de bacheo en frío, en 2. El bacheo con "
           "asfalto suma 6 frentes, la rehabilitación con asfalto 1 y la rehabilitación y bacheo con hormigón, 10.",
           "Las magnitudes de cada obra salen de las memorias descriptivas de los equipos técnicos; donde no hay "
           "dato, el texto no lleva magnitud."]),
         ("Un plan que recorre la ciudad",
          ["Calle por Calle ordena las intervenciones barrio por barrio, de modo que el mantenimiento y la "
           "rehabilitación lleguen a todos los sectores de Córdoba."])],
        None),
)

# ---------------------------------------------------------------- 5. pavimentación
G["g_cuadras"] = dict(
    titulos=[
        "La pavimentación avanza en 7 barrios de Córdoba",
        "Siete obras de pavimentación en marcha, con proyectos que contemplan 205 cuadras",
        "Más cuadras de asfalto para los barrios de Córdoba",
    ],
    ig="🚧 PAVIMENTACIÓN EN 7 BARRIOS\n\n"
       "Las obras de pavimentación avanzan en 7 barrios de la ciudad de Córdoba. Los proyectos en ejecución "
       "contemplan 205 cuadras de calles nuevas para vecinos que hoy circulan por tierra.\n\n"
       "Compartí esta publicación y seguí cómo avanza la obra en tu barrio.\n\n"
       "#CallePorCalle #CórdobaMejora #HacerParaCrecer",
    x="🚧 La pavimentación avanza en 7 barrios de Córdoba, con proyectos que contemplan 205 cuadras. "
      "#CallePorCalle #HacerParaCrecer",
    gac=gac(
        "La pavimentación avanza en 7 barrios de Córdoba",
        ["Los proyectos en ejecución contemplan 205 cuadras.",
         "Las cuadras y los plazos surgen de las memorias descriptivas de cada obra."],
        f"{MUNI} ejecuta obras de pavimentación en 7 barrios de la ciudad de Córdoba. Los proyectos contemplan, en "
        "conjunto, 205 cuadras.",
        [("Qué significa pavimentar un barrio",
          ["La pavimentación cambia la vida diaria de quienes circulan por calles de tierra: mejora el acceso del "
           "transporte y de los servicios de emergencia, ordena el escurrimiento del agua y reduce el polvo.",
           "Las cuadras y los plazos informados corresponden al proyecto de cada obra y no al avance alcanzado."]),
         ("Un plan de largo alcance",
          ["El plan de pavimentación prevé 1.100 cuadras en toda la ciudad."])],
        None),
)

# ---------------------------------------------------------------- 6. plazas
G["g_plazas"] = dict(
    titulos=[
        "Hay 25 plazas en renovación en 12 barrios de Córdoba",
        "Nos vemos en la Plaza: 21 espacios públicos en obra",
        "La renovación de plazas alcanza a 12 barrios de la ciudad",
    ],
    ig="🌳 21 PLAZAS EN RENOVACIÓN\n\n"
       "Hay 25 plazas en obra en 12 barrios de Córdoba: juegos, luminarias, bancos, senderos y espacios verdes que "
       "vuelven a ser punto de encuentro para los vecinos.\n\n"
       "Nos vemos en la Plaza.\n\n"
       "#NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer",
    x="🌳 Hay 25 plazas en renovación en 12 barrios de la ciudad de Córdoba. "
      "#NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Hay 25 plazas en renovación en 12 barrios de Córdoba",
        ["Las obras alcanzan a plazas y plazoletas de distintos sectores de la ciudad.",
         "Parte de las intervenciones se ejecutan junto a la Empresa Provincial de Energía de Córdoba."],
        f"{MUNI} renueva 25 plazas en 12 barrios de la ciudad de Córdoba. Los trabajos comprenden la puesta en valor "
        "integral de los espacios públicos.",
        [("Qué incluye la renovación",
          ["Las obras contemplan sendas, iluminación, equipamiento, juegos y espacios verdes, de manera que cada "
           "plaza vuelva a funcionar como lugar de encuentro del barrio.",
           "Varias de las intervenciones se ejecutan junto a la Empresa Provincial de Energía de Córdoba."]),
         ("Espacios públicos en todos los sectores",
          ["La renovación llega a barrios del norte, del sur, del este y del oeste de la ciudad, con el criterio de "
           "que cada vecino tenga una plaza cuidada cerca de su casa."])],
        None),
)

# ---------------------------------------------------------------- 7. planes
G["g_acum"] = dict(
    titulos=[
        "Córdoba prevé 1.100 cuadras de pavimento y 2.100 rampas para toda la ciudad",
        "Los planes de pavimentación y accesibilidad que ordenan la obra pública en Córdoba",
        "Una hoja de ruta para la infraestructura de la ciudad",
    ],
    ig="📍 LOS PLANES QUE ORDENAN LA OBRA\n\n"
       "El plan de pavimentación prevé 1.100 cuadras para toda la ciudad de Córdoba y el programa Córdoba Accesible "
       "contempla 2.100 rampas: 2.000 nuevas y 100 reparaciones.\n\n"
       "Cada obra que se abre forma parte de esa hoja de ruta.\n\n"
       "#CórdobaMejora #CórdobaAccesible #HacerParaCrecer",
    x="📍 El plan de pavimentación prevé 1.100 cuadras y el programa Córdoba Accesible contempla 2.100 rampas para "
      "toda la ciudad. #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Córdoba prevé 1.100 cuadras de pavimento y 2.100 rampas para toda la ciudad",
        ["El plan de pavimentación prevé 1.100 cuadras.",
         "El programa Córdoba Accesible contempla 2.100 rampas: 2.000 nuevas y 100 reparaciones."],
        f"{MUNI} ordena la obra pública de la ciudad en torno a dos planes de largo alcance: la pavimentación de "
        "1.100 cuadras y la construcción de 2.100 rampas.",
        [("Pavimentación",
          ["El plan prevé 1.100 cuadras en los barrios que hoy no tienen asfalto. Cada obra que se inicia descuenta "
           "cuadras de esa meta."]),
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
        "Córdoba acumula 192 obras finalizadas en la ciudad",
        "192 obras terminadas: el resultado de un plan que se sostiene",
        "Las obras que ya cambiaron la vida de los barrios",
    ],
    ig="✅ 192 OBRAS FINALIZADAS\n\n"
       "Además de las 110 obras en ejecución, la ciudad de Córdoba acumula 192 obras finalizadas: calles "
       "rehabilitadas, cuadras pavimentadas, rampas construidas y plazas que ya volvieron a abrir.\n\n"
       "Lo que se termina también se cuenta.\n\n"
       "#CórdobaMejora #CallePorCalle #HacerParaCrecer",
    x="✅ La ciudad de Córdoba acumula 192 obras finalizadas, además de las 110 que están hoy en ejecución. "
      "#CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "Córdoba acumula 192 obras finalizadas en la ciudad",
        ["El acumulado alcanza a calles, rampas, pavimento y plazas.",
         "En paralelo, hay 110 obras en ejecución en 43 barrios."],
        f"{MUNI} informa que la ciudad acumula 192 obras finalizadas. El número corresponde al total alcanzado hasta "
        "la fecha e incluye intervenciones de todos los frentes del plan.",
        [("Obras que ya están en uso",
          ["Las obras terminadas abarcan calzadas rehabilitadas, cuadras pavimentadas, esquinas con rampas nuevas y "
           "plazas puestas en valor, distribuidas en distintos sectores de la ciudad."]),
         ("El plan continúa",
          ["Mientras se suman obras finalizadas, hay 110 frentes abiertos en 43 barrios, con 960 puestos de trabajo "
           "directos."])],
        None),
)

# ---------------------------------------------------------------- 9. equilibrio fiscal
G["g_fiscal"] = dict(
    titulos=[
        "El equilibrio fiscal sostiene la obra pública en la ciudad de Córdoba",
        "Cuentas en orden para que la obra no se detenga",
        "Un modelo que convierte el orden de las cuentas en infraestructura",
    ],
    ig="📊 CUENTAS EN ORDEN, OBRA QUE NO SE DETIENE\n\n"
       "Hoy hay 110 obras en ejecución en 43 barrios de Córdoba y 960 puestos de trabajo directos. Ese ritmo es "
       "posible porque el orden de las cuentas públicas permite sostener la inversión en infraestructura.\n\n"
       "#CórdobaMejora #HacerParaCrecer",
    x="📊 110 obras en ejecución y 960 puestos de trabajo directos en Córdoba: el orden de las cuentas sostiene la "
      "obra. #CórdobaMejora #HacerParaCrecer",
    gac=gac(
        "El equilibrio fiscal sostiene la obra pública en la ciudad de Córdoba",
        ["Hay 110 obras en ejecución en 43 barrios.",
         "Las obras generan 960 puestos de trabajo directos.",
         "La ciudad acumula 192 obras finalizadas."],
        f"{MUNI} sostiene un plan de obra pública que hoy alcanza 110 frentes en 43 barrios de la ciudad. La "
        "continuidad de ese plan se apoya en el equilibrio fiscal.",
        [("Previsibilidad para planificar",
          ["El orden de las cuentas públicas permite programar las obras, sostener los frentes abiertos y cumplir "
           "los plazos comprometidos con los vecinos."]),
         ("Obra en todos los frentes",
          ["El plan abarca mantenimiento y rehabilitación de calzada, pavimentación, accesibilidad y renovación de "
           "plazas."])],
        None),
)

# ---------------------------------------------------------------- línea política, una por pieza y variada
POL = {
  "g_total":     ("Con equilibrio fiscal, Córdoba sostiene la inversión en infraestructura de todos los cordobeses.", "Cuentas en orden, obra para todos."),
  "g_empleo":    ("El equilibrio fiscal sostiene la obra y el trabajo de todos los cordobeses.", "Cuentas en orden, trabajo cordobés."),
  "g_accesible": ("Con las cuentas en orden, la accesibilidad llega a todos los cordobeses.", "Equilibrio fiscal: una ciudad para todos."),
  "g_calle":     ("El orden de las cuentas permite que la obra llegue calle por calle a todos los cordobeses.", "Con equilibrio fiscal, la obra sigue."),
  "g_cuadras":   ("Con equilibrio fiscal, el pavimento llega a los barrios de todos los cordobeses.", "Equilibrio fiscal que se hace pavimento."),
  "g_plazas":    ("El equilibrio fiscal sostiene la inversión en espacios públicos para todos los cordobeses.", "Cuentas en orden, plazas para todos."),
  "g_acum":      ("Planificar la infraestructura de todos los cordobeses es posible con equilibrio fiscal.", "Equilibrio fiscal: obras que se planifican."),
  "g_fin":       ("Obras terminadas con un equilibrio fiscal que sostiene la inversión de todos los cordobeses.", "Cuentas en orden, obra que se termina."),
  "g_fiscal":    ("El modelo cordobés apuesta por el equilibrio fiscal para sostener la inversión en infraestructura de todos los cordobeses.", "Equilibrio fiscal para sostener la infraestructura de todos."),
}
def meter(pieza, ig_line, x_line):
    ig = pieza["ig"]; i = ig.rfind("\n\n#"); pieza["ig"] = ig[:i] + "\n\n" + ig_line + ig[i:]
    x = pieza["x"]; j = x.find(" #"); cand = x[:j] + " " + x_line + x[j:]
    if len(cand) <= 280: pieza["x"] = cand
for k, (a, b) in POL.items():
    meter(G[k], a, b)

json.dump(dict(generales=G, periodicos={}), open(os.path.join(HERE, "contenido.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("generales:", len(G), "periodicos: 0 (ventanas de 7 y 10 dias habiles incompletas)")
for k, v in G.items():
    assert len(v["x"]) <= 280, (k, len(v["x"]))
    assert "/" not in v["x"].replace("https://", "").replace("//", ""), k
print("X más largo:", max(len(v["x"]) for v in G.values()), "caracteres")
