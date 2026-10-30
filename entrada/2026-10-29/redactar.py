"""Piezas redactadas a mano para el parte del 29/10/2026 (generales, periódicos y por tipo de obra).
Corre:  python entrada/2026-10-29/redactar.py   ->  escribe contenido.json
Datos: parte del 29/10 (61 obras, 599 puestos, 192 finalizadas) + histórico 19 al 29/10. Sin montos, sin "circuito",
sin barras, con "Barrio" antes de cada barrio, sin citas de funcionarios.
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

_n = [4]   # arranca en otra variante del párrafo de seguimiento

def gac(titulo, bajada, lead, secciones, cierre, i=None):
    i = _n[0]; _n[0] += 1
    partes = [titulo, "\n".join("• " + b for b in bajada), lead]
    for h, ps in secciones:
        partes.append(h); partes.extend(ps)
    if cierre: partes.append(cierre)
    h, p = seg(i); partes += [h, p, "Material de descarga: [pegar enlace]"]
    return "\n\n".join(partes)

G, PER = {}, {}

# ---------------------------------------------------------------- GENERALES
G["g_total"] = dict(
    titulos=["Córdoba tiene 61 obras en ejecución en al menos 31 barrios de la ciudad",
             "61 obras en marcha y 599 puestos de trabajo directos: así avanza la obra pública en Córdoba",
             "Calles, rampas, plazas y pavimento: las obras ya están en marcha en al menos 31 barrios"],
    ig="""🏗️ 61 OBRAS EN EJECUCIÓN EN LA CIUDAD

Hoy hay 61 obras en marcha en al menos 31 barrios de Córdoba: calles que se rehabilitan, rampas que se construyen, plazas que se renuevan y cuadras que se pavimentan. Detrás de cada una hay trabajo concreto: 599 puestos de trabajo directos.

👉 Seguí el avance de las obras de tu barrio.

#CórdobaMejora #HacerParaCrecer""",
    x="🏗️ Hoy hay 61 obras en marcha en al menos 31 barrios de Córdoba, con 599 puestos de trabajo directos. #CórdobaMejora #HacerParaCrecer",
    gac=gac("Córdoba tiene 61 obras en ejecución en al menos 31 barrios de la ciudad",
        ["Las obras generan 599 puestos de trabajo directos.",
         "Hay 31 frentes de reparación vial, 22 esquinas con rampas y 8 plazas en renovación.",
         "Ya se finalizaron 192 obras en la ciudad."],
        "El Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba, mantiene hoy 61 obras en ejecución en al menos 31 barrios de la ciudad, que generan 599 puestos de trabajo directos.",
        [("Una ciudad en obra",
          ["Los trabajos abarcan el mantenimiento de calles de tierra, el bacheo en frío y con asfalto, la rehabilitación con asfalto y con hormigón, la pavimentación, la construcción de rampas de accesibilidad y la renovación de plazas, de acuerdo con las características y necesidades de cada sector.",
           "Solo en reparación vial hay 31 frentes abiertos: 13 de rehabilitación y bacheo con hormigón, 6 de mantenimiento de calles, 5 de pavimentación, 4 de bacheo con asfalto, 2 de bacheo en frío y 1 de rehabilitación con asfalto, que se realiza de noche en el Barrio Centro."]),
         ("Más accesibilidad y más espacios verdes",
          ["Córdoba Accesible avanza con la colocación de 55 rampas en 22 esquinas, mientras que Nos vemos en la Plaza renueva 8 plazas: seis en el Barrio Poeta Lugones, una en el Barrio Villa Cabrera y la plaza Pedro Vivas, en el Barrio Talleres Este."]),
         ("Hacer para Crecer, obra a obra",
          ["Además de las obras en marcha, ya se finalizaron 192, lo que suma 253 obras entre terminadas y en ejecución. Es la forma concreta en que el orden en las cuentas se transforma en calles recuperadas, esquinas accesibles y plazas para los vecinos."])],
        "El modelo cordobés apuesta por el equilibrio fiscal como la herramienta para sostener la inversión en infraestructura de todos los cordobeses: cada obra en marcha es la prueba visible de esa decisión.", 0))

G["g_empleo"] = dict(
    titulos=["Las 61 obras en marcha generan 599 puestos de trabajo directos en Córdoba",
             "Obra pública que da trabajo: 599 puestos directos en las obras de la ciudad",
             "Hacer para Crecer: 599 puestos de trabajo directos en 61 obras en marcha"],
    ig="""👷 599 PUESTOS DE TRABAJO DIRECTOS

Cada calle que se rehabilita, cada rampa que se construye y cada plaza que se renueva tiene detrás a quienes la hacen posible: las 61 obras en marcha en la ciudad generan hoy 599 puestos de trabajo directos.

#CórdobaMejora #HacerParaCrecer""",
    x="👷 Las 61 obras en marcha en Córdoba generan 599 puestos de trabajo directos. #CórdobaMejora #HacerParaCrecer",
    gac=gac("Las 61 obras en marcha generan 599 puestos de trabajo directos en Córdoba",
        ["Las obras se reparten en al menos 31 barrios de la ciudad.", "Incluyen calles, rampas de accesibilidad, plazas y pavimentación."],
        "Las 61 obras que ejecutan hoy, de manera conjunta, el Gobierno de la Provincia y la Municipalidad de Córdoba generan 599 puestos de trabajo directos en la ciudad.",
        [("Obra pública y trabajo",
          ["El dato refleja la escala de la actividad en el territorio: 31 frentes de reparación vial, 22 esquinas con rampas de accesibilidad y 8 plazas en renovación, distribuidos en al menos 31 barrios. Cada frente de obra requiere equipos de trabajo en el territorio."]),
         ("Sostener la inversión",
          ["Mantener esta cantidad de obras en simultáneo es posible porque la inversión en infraestructura se sostiene en el tiempo, con las cuentas ordenadas, y se traduce en mejoras visibles para los barrios y en trabajo para quienes las construyen."])],
        "Es la lógica de Hacer para Crecer: con equilibrio fiscal se sostiene la inversión en infraestructura de todos los cordobeses y, con ella, el trabajo de quienes la hacen realidad.", 1))

G["g_accesible"] = dict(
    titulos=["Córdoba Accesible: avanza la colocación de 55 rampas en 22 esquinas de la ciudad",
             "Una Córdoba inclusiva, pensada para todos: 55 rampas en ejecución",
             "22 esquinas con rampas en marcha: así avanza Córdoba Accesible"],
    ig="""♿ CÓRDOBA ACCESIBLE: 55 RAMPAS EN EJECUCIÓN

Hoy se trabaja en 22 esquinas de la ciudad: 18 en la zona céntrica, con 42 rampas, y 4 sobre la Av. J. M. de Pueyrredón, con 13 más. Cada rampa es una esquina que deja de ser un obstáculo para quien se mueve en silla de ruedas, con un cochecito o con un bastón.

Una Córdoba inclusiva, pensada para todos, empieza por lo cotidiano: poder cruzar la calle con autonomía.

#CórdobaAccesible #HacerParaCrecer""",
    x="♿ Córdoba Accesible: hoy se ejecutan 55 rampas en 22 esquinas de la ciudad, 42 en la zona céntrica y 13 sobre la Av. J. M. de Pueyrredón. Una Córdoba inclusiva, pensada para todos. #CórdobaAccesible",
    gac=gac("Córdoba Accesible: avanza la colocación de 55 rampas en 22 esquinas de la ciudad",
        ["Se trabaja en 18 esquinas de la zona céntrica y en 4 de la Av. J. M. de Pueyrredón.",
         "El programa contempla 2.100 rampas en el ejido capitalino.",
         "Una Córdoba inclusiva, pensada para todos."],
        "En el marco del programa Córdoba Accesible, que impulsan el Gobierno de la Provincia y la Municipalidad de Córdoba, avanza hoy la colocación de 55 rampas en 22 esquinas de la ciudad.",
        [("Dónde se trabaja",
          ["En la zona céntrica hay 42 rampas distribuidas en 18 esquinas, entre ellas 12 de Octubre y San Martín, Lima y Salta, Oncativo y Salta, y Rincón y Rivadavia.",
           "Sobre la Av. J. M. de Pueyrredón se interviene en cuatro intersecciones, con La Pampa, Río Negro, Santa Cruz y Misiones, con 13 rampas en total, siete de ellas en la esquina con Río Negro."]),
         ("El programa",
          ["Córdoba Accesible prevé la instalación de 2.100 rampas en el ejido capitalino: 2.000 serán nuevas, de las cuales 1.317 se ubicarán en esquinas que hoy no cuentan con esta infraestructura, y otras 100 serán reparadas por daños menores. La meta es favorecer la autonomía, la movilidad y la integración de todos los vecinos en el espacio público."]),
         ("Accesibilidad en la vida cotidiana",
          ["Una rampa mejora el día a día de las personas con discapacidad, pero también el de las familias con niños pequeños y el de los adultos mayores. Por eso la accesibilidad es una inversión que alcanza a todos."])],
        "Sostener estas obras es posible porque el equilibrio fiscal permite mantener la inversión en infraestructura para todos los cordobeses, también para quienes más necesitan una ciudad accesible.", 2))

G["g_calle"] = dict(
    titulos=["Calle por Calle: 31 frentes de reparación vial en marcha en la ciudad",
             "Hormigón, asfalto y pavimento: así avanza la recuperación de calles en Córdoba",
             "Hacer para Crecer: 31 intervenciones para mejorar las calles de los barrios"],
    ig="""🛣️ CALLE POR CALLE: 31 FRENTES DE OBRA

La recuperación de calles no se detiene: hoy hay 31 frentes en marcha, con 13 de rehabilitación y bacheo con hormigón, 6 de mantenimiento de calles, 5 de pavimentación, 4 de bacheo con asfalto, 2 de bacheo en frío y 1 de rehabilitación con asfalto.

No todas las calles se resuelven igual, y por eso cada intervención se adapta a lo que necesita cada una. Todas apuntan a lo mismo: circular mejor.

#CallePorCalle #CórdobaMejora #HacerParaCrecer""",
    x="🛣️ Calle por Calle: hoy hay 31 frentes de reparación vial en marcha en la ciudad, entre hormigón, asfalto, mantenimiento y pavimentación. #CallePorCalle #CórdobaMejora",
    gac=gac("Calle por Calle: 31 frentes de reparación vial en marcha en la ciudad",
        ["Hay 13 frentes de rehabilitación y bacheo con hormigón, 6 de mantenimiento de calles y 4 de bacheo con asfalto.",
         "Cinco obras de pavimentación alcanzan 205 cuadras.",
         "Cada intervención se define según las necesidades de cada calle."],
        "El programa “Calle por Calle, Córdoba Mejora”, que lleva adelante el Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba, tiene hoy 31 frentes de obra en ejecución en la ciudad.",
        [("Una respuesta para cada calle",
          ["El programa incluye trabajos de pavimentación, rehabilitación integral de calzadas, reparación de sectores deteriorados mediante bacheo con asfalto u hormigón, de acuerdo con las características y necesidades de cada intervención, y mantenimiento de calles de tierra."]),
         ("Hormigón y asfalto",
          ["Entre los frentes con hormigón se destacan la Av. Patria y la calle Lima, en el Barrio Hogar Propio; Rosario de Santa Fe y Güemes, en el Barrio General Paz; Adolfo Alsina, en el Barrio Yofre Norte; y Río Negro, en el Barrio Rosedal, donde ya avanza una tercera etapa.",
           "En asfalto, la rehabilitación abarca la calle Sarmiento, en el Barrio Centro, con 515 metros lineales que se ejecutan en horario nocturno para reducir las molestias en la circulación. A eso se suman el bacheo en frío en el Barrio 24 de Septiembre y el Barrio Juan B. Justo, y el mantenimiento de calles de tierra en seis barrios, entre ellos el Barrio Recreo Norte, con 2.510 metros lineales."]),
         ("Pavimentación",
          ["Las cinco obras de pavimentación en marcha suman 205 cuadras en el Barrio Policial, el Barrio General Arenales, el Barrio 9 de Julio, el Barrio San Felipe y el Barrio Villa Rivadavia Anexo."])],
        "El equilibrio fiscal es lo que permite mantener abiertos, al mismo tiempo, 31 frentes de obra y sostener la inversión en infraestructura de todos los cordobeses.", 3))

G["g_cuadras"] = dict(
    titulos=["Cinco obras de pavimentación suman 205 cuadras en barrios de Córdoba",
             "Más calles con pavimento: avanzan obras en cinco barrios de la ciudad",
             "205 cuadras en obra: la pavimentación llega a cinco barrios"],
    ig="""🛣️ 205 CUADRAS EN OBRA

La pavimentación avanza en cinco barrios de la ciudad: Barrio General Arenales (70 cuadras), Barrio Villa Rivadavia Anexo (56), Barrio 9 de Julio (36), Barrio San Felipe (24) y Barrio Policial (19).

Más cuadras con pavimento significan mejor desagüe, mejor circulación y veredas definidas. Son parte del plan que prevé 1.100 nuevas cuadras en distintos barrios.

#CallePorCalle #HacerParaCrecer""",
    x="🛣️ La pavimentación avanza en cinco barrios de Córdoba y alcanza 205 cuadras: Barrio General Arenales, Barrio Villa Rivadavia Anexo, Barrio 9 de Julio, Barrio San Felipe y Barrio Policial. #CallePorCalle #HacerParaCrecer",
    gac=gac("Cinco obras de pavimentación suman 205 cuadras en barrios de Córdoba",
        ["Se pavimentan 70 cuadras en el Barrio General Arenales y 56 en el Barrio Villa Rivadavia Anexo.",
         "Las obras forman parte del plan de 1.100 nuevas cuadras de pavimento.",
         "Mejoran el desagüe, la circulación y la consolidación de cada barrio."],
        "Las cinco obras de pavimentación que ejecutan el Gobierno de la Provincia y la Municipalidad de Córdoba, en el marco de “Calle por Calle, Córdoba Mejora”, alcanzan 205 cuadras en distintos barrios de la ciudad.",
        [("Obra por obra",
          ["En el Barrio General Arenales se pavimentan 70 cuadras; en el Barrio Villa Rivadavia Anexo, 56; en el Barrio 9 de Julio, 36; en el Barrio San Felipe, 24; y en el Barrio Policial, 19, donde en primera instancia se prevé pavimentar esas cuadras y luego sumar 60 más.",
           "Los plazos de ejecución son de 150 días calendario para las obras del Barrio Policial y del Barrio San Felipe, y de 210 días para las del Barrio General Arenales, el Barrio Villa Rivadavia Anexo y el Barrio 9 de Julio."]),
         ("Qué cambia con el pavimento",
          ["Según las memorias de cada proyecto, las obras buscan mejorar el drenaje superficial de las aguas pluviales y el tránsito vehicular y peatonal, reducir los costos de mantenimiento de las calles de firme natural y dejar materializadas las líneas de vereda, con una mayor consolidación de la urbanización existente."]),
         ("Un plan de mayor escala",
          ["Estas obras se suman al plan que prevé incorporar 1.100 nuevas cuadras de pavimento en distintos barrios de la ciudad."])],
        "Pavimentar cinco barrios a la vez es posible porque el equilibrio fiscal permite sostener la inversión en infraestructura de todos los cordobeses.", 0))

G["g_plazas"] = dict(
    titulos=["Nos vemos en la Plaza: 8 plazas se renuevan en tres barrios de Córdoba",
             "Seis plazas del Barrio Poeta Lugones se renuevan: espacios verdes para jugar y encontrarse",
             "Más plazas, más encuentro: avanza la renovación de espacios verdes en la ciudad"],
    ig="""🌳 8 PLAZAS EN RENOVACIÓN

Seis plazas del Barrio Poeta Lugones, una del Barrio Villa Cabrera y la plaza Pedro Vivas, del Barrio Talleres Este, se renuevan en estos días. Son lugares para el encuentro, el juego y el deporte, donde los chicos pueden estar seguros y compartir tiempo al aire libre.

Nos vemos en la Plaza, Córdoba Mejora.

#NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer""",
    x="🌳 Nos vemos en la Plaza: hoy se renuevan 8 plazas en tres barrios de Córdoba. Espacios verdes para el encuentro, el juego y el deporte. #NosVemosEnLaPlaza #CórdobaMejora",
    gac=gac("Nos vemos en la Plaza: 8 plazas se renuevan en tres barrios de Córdoba",
        ["Seis plazas del Barrio Poeta Lugones, una del Barrio Villa Cabrera y una del Barrio Talleres Este.",
         "Espacios seguros para jugar, hacer deporte y encontrarse.",
         "Más verde y más vida de barrio."],
        "El programa “Nos vemos en la Plaza, Córdoba Mejora”, que impulsan el Gobierno de la Provincia y la Municipalidad de Córdoba, renueva hoy ocho plazas en tres barrios de la ciudad.",
        [("Dónde se trabaja",
          ["En el Barrio Poeta Lugones se interviene en las plazas Manuel José Castilla, Baravino, Gálvez, Carolina Vocos Catturelli, Carlota Achaval de Tagle y Quiroga Malvina Rosa. A ellas se suman la plaza Pedro Luis Galeano, en el Barrio Villa Cabrera, y la plaza Pedro Vivas, en el Barrio Talleres Este."]),
         ("La plaza Pedro Vivas",
          ["La puesta en valor de este espacio verde, que se ejecuta de manera conjunta con EPEC, contempla la renovación de senderos, rampas de acceso para un ingreso inclusivo, mobiliario urbano, un patio de las infancias con juegos clásicos y adaptados, postas gimnásticas y la parquización de los espacios verdes."]),
         ("Por qué importan las plazas",
          ["Las plazas son pulmones verdes que aportan sostenibilidad y valor ambiental a la ciudad, y a la vez el lugar donde los vecinos se conocen y se encuentran. Son espacios seguros para el juego, el deporte y la recreación, una alternativa a los entornos de riesgo para chicos y adolescentes."])],
        "Con las cuentas en orden, la inversión en espacios públicos se mantiene y llega a todos los cordobeses: también a la plaza del barrio.", 1))

G["g_acum"] = dict(
    titulos=["Calle por Calle prevé 1.100 nuevas cuadras de pavimento y Córdoba Accesible, 2.100 rampas",
             "Dos planes que transforman los barrios: 1.100 cuadras de pavimento y 2.100 rampas",
             "1.100 cuadras y 2.100 rampas: la escala de la obra pública que se proyecta en Córdoba"],
    ig="""🏗️ 1.100 CUADRAS Y 2.100 RAMPAS

El plan Calle por Calle, Córdoba Mejora prevé incorporar 1.100 nuevas cuadras de pavimento en distintos barrios de la ciudad, y Córdoba Accesible contempla la instalación de 2.100 rampas en el ejido capitalino.

Hoy esas metas ya tienen obras en marcha: cinco pavimentaciones que alcanzan 205 cuadras y 55 rampas en ejecución.

#CallePorCalle #CórdobaAccesible #HacerParaCrecer""",
    x="🏗️ Calle por Calle prevé 1.100 nuevas cuadras de pavimento y Córdoba Accesible, 2.100 rampas. Hoy ya hay 205 cuadras en obra y 55 rampas en ejecución. #CallePorCalle #CórdobaAccesible",
    gac=gac("Calle por Calle prevé 1.100 nuevas cuadras de pavimento y Córdoba Accesible, 2.100 rampas",
        ["Hoy hay 205 cuadras en obra y 55 rampas en ejecución.", "Dos planes para mejorar la circulación y la accesibilidad en los barrios."],
        "Dos programas del Gobierno de la Provincia y la Municipalidad de Córdoba marcan la escala de la obra pública que se proyecta para la ciudad: “Calle por Calle, Córdoba Mejora”, que prevé 1.100 nuevas cuadras de pavimento, y Córdoba Accesible, que contempla 2.100 rampas.",
        [("De la meta a la obra",
          ["Esas metas ya empezaron a materializarse: hoy se ejecutan cinco obras de pavimentación que alcanzan 205 cuadras y 55 rampas en 22 esquinas de la ciudad."]),
         ("Dos formas de mejorar lo cotidiano",
          ["Pavimentar permite mejorar el desagüe, el tránsito y la conexión de los barrios. Construir rampas permite que cada vecino se mueva con autonomía por el espacio público. Dos obras distintas con un mismo objetivo: una ciudad más cómoda y más inclusiva."])],
        "Planificar 1.100 cuadras y 2.100 rampas solo es posible con equilibrio fiscal: es lo que permite sostener la inversión en infraestructura para todos los cordobeses.", 2))

G["g_fin"] = dict(
    titulos=["Córdoba suma 192 obras finalizadas y 61 en ejecución",
             "A ocho obras de llegar a las 200 finalizadas: la obra pública sigue su marcha",
             "Más de 150 obras finalizadas y 61 en marcha: así avanza la ciudad"],
    ig="""✅ 192 OBRAS FINALIZADAS

El balance de la obra pública en Córdoba tiene dos columnas: 192 obras ya terminadas y 61 que hoy están en marcha, en al menos 31 barrios. En total, 253 obras que mejoran las calles, las esquinas y los espacios verdes de la ciudad.

Faltan 8 para llegar a las 200 finalizadas.

#CórdobaMejora #HacerParaCrecer""",
    x="✅ Córdoba suma 192 obras finalizadas y 61 en ejecución: 253 obras en total. Faltan 8 para llegar a las 200 terminadas. #CórdobaMejora #HacerParaCrecer",
    gac=gac("Córdoba suma 192 obras finalizadas y 61 en ejecución",
        ["En total son 253 obras entre terminadas y en marcha.", "Faltan 8 para llegar a las 200 obras finalizadas."],
        "El Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba, ya finalizó 192 obras en la ciudad y mantiene otras 61 en ejecución, en al menos 31 barrios.",
        [("Lo que ya se terminó y lo que sigue",
          ["Las obras en marcha incluyen 31 frentes de reparación vial, 22 esquinas con rampas de accesibilidad y 8 plazas en renovación. Se suman a las 192 que ya fueron finalizadas."]),
         ("Hacia las 200 obras",
          ["La ciudad está a ocho obras de alcanzar las 200 finalizadas, un número que resume el trabajo sostenido de los equipos en los barrios."])],
        "Hacer para Crecer es continuidad: obras que se terminan, obras que empiezan y un equilibrio fiscal que permite sostener la inversión en infraestructura de todos los cordobeses.", 3))

G["g_fiscal"] = dict(
    titulos=["El modelo cordobés se ve en la calle: 61 obras en marcha con las cuentas en orden",
             "Equilibrio fiscal para invertir: la obra pública como prueba de gestión",
             "Orden en las cuentas, obra en los barrios: Hacer para Crecer"],
    ig="""🏛️ CUENTAS EN ORDEN, OBRA A LA VISTA

El equilibrio fiscal no es una cifra en un papel: es una calle rehabilitada, una esquina con rampa, una plaza que se renueva. Hoy hay 61 obras en marcha en al menos 31 barrios de Córdoba.

#CórdobaMejora #HacerParaCrecer""",
    x="🏛️ El equilibrio fiscal se ve en la calle: 61 obras en marcha en al menos 31 barrios de Córdoba. #HacerParaCrecer",
    gac=gac("El modelo cordobés se ve en la calle: 61 obras en marcha con las cuentas en orden",
        ["Hay 61 obras en ejecución en al menos 31 barrios de la ciudad.", "Incluyen 55 rampas, 205 cuadras de pavimento y 8 plazas en renovación.", "Hacer para Crecer: el equilibrio fiscal se convierte en obra."],
        "A través de 61 obras en ejecución, el Gobierno de la Provincia y la Municipalidad de Córdoba muestran cómo el equilibrio fiscal se traduce en infraestructura para la vida cotidiana de los vecinos.",
        [("Prioridades claras",
          ["El modelo cordobés prioriza el equilibrio fiscal orientado a la inversión en infraestructura y no el ajuste ciego. Esa decisión permite sostener, de manera simultánea, la rehabilitación de calles, la construcción de rampas de accesibilidad, la pavimentación de barrios enteros y la renovación de plazas."]),
         ("La prueba, a la vista",
          ["Las obras en marcha son el resultado concreto de esa orientación: 599 puestos de trabajo directos, 55 rampas en 22 esquinas, 205 cuadras de pavimento y 8 plazas que se renuevan para el encuentro y el juego."])],
        "El equilibrio fiscal no es un fin en sí mismo: es el medio para mantener la inversión en infraestructura de todos los cordobeses.", 1))

# ---------------------------------------------------------------- PERIÓDICOS (general)
PER["p_7"] = dict(
    titulo="Lectura semanal", eje="calle",
    titulos=["En la última semana se ejecutaron 105 obras en la ciudad de Córdoba",
             "En la última semana, en promedio, hubo 59 obras en ejecución por día en Córdoba",
             "Obra pública sostenida: 595 puestos de trabajo directos por día, en promedio, en la última semana",
             "Ya se finalizaron más de 150 obras en la ciudad"],
    ig="""📊 LA SEMANA EN OBRAS

En la última semana, el Gobierno de la Provincia y la Municipalidad de Córdoba ejecutaron 105 obras distintas en la ciudad, con un promedio de 59 obras en marcha por día y 595 puestos de trabajo directos diarios.

El detalle: 23 esquinas con rampas, 20 frentes de rehabilitación y bacheo con hormigón, 16 de bacheo en frío, 14 plazas y 5 pavimentaciones, entre otras intervenciones.

#CórdobaMejora #HacerParaCrecer""",
    x="📊 En la última semana se ejecutaron 105 obras en Córdoba, con 59 obras en marcha por día y 595 puestos de trabajo directos diarios, en promedio. #CórdobaMejora #HacerParaCrecer",
    placa=dict(kicker="Lectura semanal", valor="105", etiqueta="Obras en la última semana", sub="59 en ejecución por día, en promedio"),
    gac=gac("En la última semana se ejecutaron 105 obras en la ciudad de Córdoba",
        ["En promedio, hubo 59 obras en ejecución por día.", "Las obras generaron 595 puestos de trabajo directos por día, en promedio.", "Se trabajó en rampas, plazas, calles y pavimentación en toda la ciudad."],
        "Entre el 23 y el 29 de octubre, el Gobierno de la Provincia y la Municipalidad de Córdoba ejecutaron 105 obras distintas en la ciudad, con un promedio de 59 obras en marcha por día.",
        [("Qué se hizo en la semana",
          ["La actividad estuvo repartida en todos los frentes: 23 esquinas con rampas de accesibilidad, 20 intervenciones de rehabilitación y bacheo con hormigón, 16 de bacheo en frío, 14 plazas, 14 de mantenimiento de calles, 10 de bacheo con asfalto, 3 de rehabilitación con asfalto y 5 obras de pavimentación."]),
         ("Trabajo en el territorio",
          ["En promedio, cada día de la semana las obras generaron 595 puestos de trabajo directos, un indicador de la presencia sostenida del Estado en los barrios."])],
        "Hacer para Crecer es constancia: una semana tras otra, las cuentas en orden permiten que la inversión en infraestructura de todos los cordobeses no se detenga.", 0))

PER["p_10"] = dict(
    titulo="Lectura a 10 días", eje="calle",
    titulos=["En los últimos 10 días se ejecutaron 133 obras en la ciudad de Córdoba",
             "En diez días, 23 frentes de bacheo en frío y 18 de bacheo con asfalto: así se recuperan las calles",
             "En los últimos 10 días, en promedio, las obras generaron 607 puestos de trabajo directos por día"],
    ig="""📊 DIEZ DÍAS DE OBRA PÚBLICA

Entre el 20 y el 29 de octubre se ejecutaron 133 obras distintas en la ciudad, con un promedio de 59 obras en marcha por día y 607 puestos de trabajo directos diarios.

En esos diez días, el bacheo en frío llegó a 23 frentes y el bacheo con asfalto a 18, mientras que las rampas pasaron de 9 a 22 esquinas en ejecución.

#CórdobaMejora #HacerParaCrecer""",
    x="📊 En diez días se ejecutaron 133 obras en Córdoba: 23 frentes de bacheo en frío, 18 de bacheo con asfalto y rampas en 22 esquinas. 607 puestos de trabajo directos por día. #HacerParaCrecer",
    placa=dict(kicker="Lectura a 10 días", valor="133", etiqueta="Obras en los últimos 10 días", sub="607 puestos de trabajo directos por día, en promedio"),
    gac=gac("En los últimos 10 días se ejecutaron 133 obras en la ciudad de Córdoba",
        ["En promedio, hubo 59 obras en ejecución por día.", "Los puestos de trabajo directos promediaron 607 por día.", "Las rampas pasaron de 9 a 22 esquinas en ejecución."],
        "Entre el 20 y el 29 de octubre, el Gobierno de la Provincia y la Municipalidad de Córdoba ejecutaron 133 obras distintas en la ciudad, con un promedio de 59 obras en marcha por día y 607 puestos de trabajo directos diarios.",
        [("Calles recuperadas",
          ["La reparación vial concentró buena parte de la actividad: 23 frentes de bacheo en frío, 18 de bacheo con asfalto, 22 de rehabilitación y bacheo con hormigón, 17 de mantenimiento de calles y 8 de rehabilitación con asfalto, además de 5 obras de pavimentación."]),
         ("Accesibilidad y espacios verdes",
          ["En el mismo período, Córdoba Accesible pasó de 9 esquinas con rampas en ejecución, el 20 de octubre, a 22 esquinas en el parte de hoy. Por su parte, Nos vemos en la Plaza trabajó en 17 plazas de nueve barrios."]),
         ("Hacer para Crecer, día a día",
          ["Lo que aparece en estos números no es un hecho aislado sino una forma de gestionar: planificar la obra, sostenerla en el tiempo y mostrarla."])],
        "El equilibrio fiscal es lo que permite que diez días de trabajo se conviertan en calles, esquinas y plazas distintas para todos los cordobeses.", 1))

# ---------------------------------------------------------------- POR TIPO DE OBRA
PER["p_7_plazas"] = dict(
    titulo="Lectura semanal · Plazas", eje="plaza",
    titulos=["Nos vemos en la Plaza: en la última semana se trabajó en 14 plazas de siete barrios de Córdoba",
             "Espacios verdes en obra: 14 plazas en renovación durante la última semana",
             "Plazas para el encuentro y el juego: así avanzó la renovación en la última semana"],
    ig="""🌳 LAS PLAZAS DE LA SEMANA

En la última semana, Nos vemos en la Plaza trabajó en 14 plazas de siete barrios de Córdoba, con ocho plazas en obra hoy. El Barrio Poeta Lugones concentra la mayor intervención, con ocho plazas, y hubo trabajos en el Barrio Alta Córdoba, el Barrio Centro América, el Barrio Los Plátanos, el Barrio Parque Jorge Newbery, el Barrio Talleres Este y el Barrio Villa Cabrera.

Plazas para jugar, hacer deporte y encontrarse, cerca de casa.

#NosVemosEnLaPlaza #CórdobaMejora""",
    x="🌳 En la última semana, Nos vemos en la Plaza trabajó en 14 plazas de siete barrios de Córdoba: espacios verdes para el encuentro, el juego y el deporte. #NosVemosEnLaPlaza #CórdobaMejora",
    placa=dict(kicker="Nos vemos en la Plaza", valor="14", etiqueta="Plazas en obra en la última semana", sub="En siete barrios de la ciudad"),
    gac=gac("Nos vemos en la Plaza: en la última semana se trabajó en 14 plazas de siete barrios de Córdoba",
        ["Ocho plazas del Barrio Poeta Lugones estuvieron en obra.", "Hoy hay ocho plazas en renovación en la ciudad.", "Espacios seguros para el juego, el deporte y el encuentro."],
        "Entre el 23 y el 29 de octubre, el programa “Nos vemos en la Plaza, Córdoba Mejora”, que impulsan el Gobierno de la Provincia y la Municipalidad de Córdoba, trabajó en 14 plazas distribuidas en siete barrios de la ciudad.",
        [("Un mapa de plazas en obra",
          ["La mayor concentración está en el Barrio Poeta Lugones, con ocho plazas. Además hubo trabajos en una plaza de cada uno de estos barrios: Barrio Alta Córdoba, Barrio Centro América, Barrio Los Plátanos, Barrio Parque Jorge Newbery, Barrio Talleres Este y Barrio Villa Cabrera."]),
         ("Más verde, más encuentro",
          ["Las plazas son espacios verdes que suman sostenibilidad y valor ambiental, y donde los vecinos se encuentran, juegan y hacen deporte. Son lugares seguros para los chicos, una alternativa a los entornos de riesgo, y por eso cada obra de renovación importa más allá del barrio donde se hace."])],
        "Hacer para Crecer también pasa por la plaza de la esquina: con equilibrio fiscal, la inversión en espacios públicos llega a todos los cordobeses.", 2))

PER["p_10_plazas"] = dict(
    titulo="Lectura a 10 días · Plazas", eje="plaza",
    titulos=["En diez días, Nos vemos en la Plaza llegó a 17 plazas de nueve barrios de Córdoba",
             "Diez días de renovación: 17 plazas y nueve barrios con obras de espacios verdes",
             "Más plazas, más barrio: así avanzó Nos vemos en la Plaza en los últimos 10 días"],
    ig="""🌳 DIEZ DÍAS DE PLAZAS

Entre el 20 y el 29 de octubre, la renovación de espacios verdes alcanzó 17 plazas en nueve barrios de la ciudad, con entre seis y nueve plazas en obra cada día. Hoy son ocho: seis en el Barrio Poeta Lugones, una en el Barrio Villa Cabrera y la plaza Pedro Vivas, en el Barrio Talleres Este.

Una plaza renovada es un barrio que se encuentra.

#NosVemosEnLaPlaza #CórdobaMejora #HacerParaCrecer""",
    x="🌳 En diez días, Nos vemos en la Plaza trabajó en 17 plazas de nueve barrios de Córdoba. Hoy hay ocho en obra. Espacios verdes para el encuentro y el juego. #NosVemosEnLaPlaza #CórdobaMejora",
    placa=dict(kicker="Nos vemos en la Plaza", valor="17", etiqueta="Plazas en obra en 10 días", sub="En nueve barrios de la ciudad"),
    gac=gac("En diez días, Nos vemos en la Plaza llegó a 17 plazas de nueve barrios de Córdoba",
        ["Hoy hay ocho plazas en renovación.", "La plaza Pedro Vivas incluye patio de las infancias, postas gimnásticas y parquización.", "Más espacios verdes seguros para los vecinos."],
        "Entre el 20 y el 29 de octubre, el Gobierno de la Provincia y la Municipalidad de Córdoba sostuvieron obras de renovación en 17 plazas de nueve barrios de la ciudad, en el marco del programa “Nos vemos en la Plaza, Córdoba Mejora”.",
        [("Diez días, nueve barrios",
          ["El trabajo se repartió por toda la ciudad: Barrio Poeta Lugones, Barrio Centro América, Barrio Alta Córdoba, Barrio Colinas del Cerro, Barrio Industrial Oeste, Barrio Los Plátanos, Barrio Parque Jorge Newbery, Barrio Talleres Este y Barrio Villa Cabrera, todos con obras en sus plazas durante el período."]),
         ("Una plaza, muchas mejoras",
          ["En la plaza Pedro Vivas, del Barrio Talleres Este, la puesta en valor que se ejecuta junto con EPEC incluye renovación de senderos, rampas de acceso, mobiliario urbano, un patio de las infancias con juegos clásicos y adaptados, postas gimnásticas y parquización."]),
         ("El valor de lo público",
          ["Una plaza renovada mejora el ambiente del barrio, ofrece un lugar seguro para el juego y el deporte, y fortalece la vida comunitaria. Por eso el programa apunta a que cada vecino tenga un espacio verde cerca de su casa."])],
        "Sostener esta cantidad de plazas en obra durante diez días seguidos es posible gracias al equilibrio fiscal, que mantiene la inversión en espacios públicos para todos los cordobeses.", 3))

PER["p_7_rampas"] = dict(
    titulo="Lectura semanal · Rampas", eje="accesible",
    titulos=["Córdoba Accesible: en la última semana se sumaron cinco esquinas con rampas en la ciudad",
             "De 18 a 22 esquinas con rampas en ejecución en una semana: así avanza Córdoba Accesible",
             "Una Córdoba inclusiva, pensada para todos: más esquinas accesibles en la última semana"],
    ig="""♿ LAS RAMPAS DE LA SEMANA

En la última semana, Córdoba Accesible trabajó en 23 esquinas de la ciudad. Las esquinas con obra en ejecución pasaron de 18 a 22 y hoy hay 55 rampas en marcha.

Se sumaron Montevideo e Hipólito Yrigoyen, Rincón y Rivadavia, Domingo F. Sarmiento y Blvd. Guzmán, Caseros y Av. Marcelo T. de Alvear, y La Tablada y San Martín. Una Córdoba inclusiva, pensada para todos, esquina por esquina.

#CórdobaAccesible #HacerParaCrecer""",
    x="♿ En la última semana, Córdoba Accesible trabajó en 23 esquinas: las que están en obra pasaron de 18 a 22 y hoy hay 55 rampas en ejecución. Una Córdoba inclusiva, pensada para todos. #CórdobaAccesible",
    placa=dict(kicker="Córdoba Accesible", valor="23", etiqueta="Esquinas con rampas en la última semana", sub="De 18 a 22 esquinas en ejecución"),
    gac=gac("Córdoba Accesible: en la última semana se sumaron cinco esquinas con rampas en la ciudad",
        ["Las esquinas en ejecución pasaron de 18 a 22.", "Hoy hay 55 rampas en obra.", "El programa contempla 2.100 rampas en el ejido capitalino."],
        "Entre el 23 y el 29 de octubre, el programa Córdoba Accesible, que impulsan el Gobierno de la Provincia y la Municipalidad de Córdoba, trabajó en 23 esquinas de la ciudad y sumó cinco nuevas intervenciones a las que ya estaban en marcha.",
        [("Más esquinas en obra",
          ["En el parte del 23 de octubre figuraban 18 esquinas en ejecución; hoy son 22. Las incorporaciones son Montevideo e Hipólito Yrigoyen, Rincón y Rivadavia, Domingo F. Sarmiento y Blvd. Guzmán, Caseros y Av. Marcelo T. de Alvear, y La Tablada y San Martín, todas en la zona céntrica.",
           "Hoy se trabaja en 18 esquinas de la zona céntrica, con 42 rampas, y en 4 de la Av. J. M. de Pueyrredón, con 13."]),
         ("Un programa para toda la ciudad",
          ["Córdoba Accesible prevé instalar 2.100 rampas en el ejido capitalino, de las cuales 1.317 estarán en esquinas que hoy no tienen esta infraestructura, para favorecer la autonomía, la movilidad y la integración de todos los vecinos."])],
        "Una ciudad más accesible es una ciudad pensada para todos, y se construye con inversión sostenida: el equilibrio fiscal permite mantenerla para todos los cordobeses.", 0))

PER["p_10_rampas"] = dict(
    titulo="Lectura a 10 días · Rampas", eje="accesible",
    titulos=["En diez días, las rampas en ejecución se duplicaron: de 26 a 55 en Córdoba",
             "Córdoba Accesible: de 9 a 22 esquinas con rampas en diez días",
             "Una Córdoba inclusiva, pensada para todos: así creció el programa de rampas en los últimos 10 días"],
    ig="""♿ DIEZ DÍAS DE RAMPAS

El 20 de octubre había 9 esquinas con 26 rampas en ejecución; en el parte de hoy son 22 esquinas con 55 rampas. En diez días, Córdoba Accesible duplicó su ritmo de trabajo.

Rampas en la zona céntrica y sobre la Av. J. M. de Pueyrredón, para que moverse por la ciudad sea más fácil para todos.

#CórdobaAccesible #HacerParaCrecer""",
    x="♿ En diez días, Córdoba Accesible pasó de 9 a 22 esquinas en obra y de 26 a 55 rampas en ejecución. Una Córdoba inclusiva, pensada para todos. #CórdobaAccesible #HacerParaCrecer",
    placa=dict(kicker="Córdoba Accesible", valor="55", etiqueta="Rampas en ejecución hoy", sub="Eran 26 hace diez días"),
    gac=gac("En diez días, las rampas en ejecución se duplicaron: de 26 a 55 en Córdoba",
        ["Las esquinas en obra pasaron de 9 a 22.", "Hoy hay 42 rampas en la zona céntrica y 13 en la Av. J. M. de Pueyrredón.", "Una Córdoba inclusiva, pensada para todos."],
        "En diez días, el programa Córdoba Accesible, que lleva adelante el Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba, duplicó la cantidad de rampas en ejecución: pasó de 26, el 20 de octubre, a 55 en el parte de hoy.",
        [("El crecimiento, esquina por esquina",
          ["Las esquinas con obra pasaron de 9 a 22 y se extendieron más allá de los primeros puntos de trabajo. Hoy hay 18 esquinas en la zona céntrica y 4 en la Av. J. M. de Pueyrredón, donde la esquina con Río Negro concentra 7 rampas."]),
         ("De qué se trata el programa",
          ["Córdoba Accesible contempla 2.100 rampas en el ejido capitalino: 2.000 nuevas, 1.317 de ellas en esquinas sin esta infraestructura, y 100 reparaciones. Cada rampa es una puerta abierta para las personas con discapacidad, las familias con cochecitos y los adultos mayores."])],
        "Acelerar las obras sin descuidar las cuentas es parte de una forma de gobernar: con equilibrio fiscal, la inversión en infraestructura mejora la vida de todos los cordobeses.", 1))

PER["p_7_pav"] = dict(
    titulo="Lectura semanal · Pavimentación", eje="calle",
    titulos=["Pavimentación en Córdoba: cinco obras suman 205 cuadras en la última semana",
             "Cinco barrios con pavimento en marcha: así avanzó la última semana",
             "Más cuadras pavimentadas para los barrios: 205 cuadras en obra"],
    ig="""🛣️ PAVIMENTACIÓN DE LA SEMANA

En la última semana siguieron en marcha las cinco obras de pavimentación de la ciudad, que suman 205 cuadras: Barrio General Arenales (70), Barrio Villa Rivadavia Anexo (56), Barrio 9 de Julio (36), Barrio San Felipe (24) y Barrio Policial (19).

Cada cuadra pavimentada mejora el desagüe, la circulación y la vida del barrio.

#CallePorCalle #HacerParaCrecer""",
    x="🛣️ Siguen en marcha cinco obras de pavimentación en Córdoba, con 205 cuadras: Barrio General Arenales, Barrio Villa Rivadavia Anexo, Barrio 9 de Julio, Barrio San Felipe y Barrio Policial. #CallePorCalle",
    placa=dict(kicker="Calle por Calle", valor="205", etiqueta="Cuadras de pavimento en obra", sub="Cinco obras en cinco barrios"),
    gac=gac("Pavimentación en Córdoba: cinco obras suman 205 cuadras en la última semana",
        ["Las obras están en cinco barrios de la ciudad.", "Los plazos van de 150 a 210 días calendario.", "Forman parte del plan de 1.100 nuevas cuadras de pavimento."],
        "Durante la última semana, el Gobierno de la Provincia y la Municipalidad de Córdoba mantuvieron en marcha cinco obras de pavimentación que, en conjunto, alcanzan 205 cuadras en distintos barrios de la ciudad.",
        [("Las cinco obras",
          ["El Barrio General Arenales, con 70 cuadras, es la de mayor extensión; le siguen el Barrio Villa Rivadavia Anexo, con 56; el Barrio 9 de Julio, con 36; el Barrio San Felipe, con 24; y el Barrio Policial, con 19, donde se prevé luego sumar 60 más."]),
         ("Para qué sirve el pavimento",
          ["Según las memorias de las obras, el pavimento mejora el drenaje superficial de las aguas pluviales y el tránsito vehicular y peatonal, reduce los costos de mantenimiento de las calles de firme natural y deja materializadas las líneas de vereda."])],
        "Pavimentar barrios enteros es una inversión que dura décadas, y el equilibrio fiscal es lo que permite sostenerla para todos los cordobeses.", 2))

PER["p_10_pav"] = dict(
    titulo="Lectura a 10 días · Pavimentación", eje="calle",
    titulos=["En diez días de obra, la pavimentación sostiene 205 cuadras en cinco barrios de Córdoba",
             "Calle por Calle: cinco pavimentaciones en marcha que forman parte del plan de 1.100 cuadras",
             "Pavimento que transforma barrios: lo que se hizo en los últimos 10 días"],
    ig="""🛣️ DIEZ DÍAS DE PAVIMENTO

Entre el 20 y el 29 de octubre se sostuvieron cinco obras de pavimentación en la ciudad: 205 cuadras en el Barrio General Arenales, el Barrio Villa Rivadavia Anexo, el Barrio 9 de Julio, el Barrio San Felipe y el Barrio Policial.

Son un paso hacia las 1.100 nuevas cuadras de pavimento que prevé Calle por Calle.

#CallePorCalle #CórdobaMejora""",
    x="🛣️ En diez días se sostuvieron cinco obras de pavimentación en Córdoba, con 205 cuadras en cinco barrios. Forman parte del plan de 1.100 nuevas cuadras de pavimento. #CallePorCalle #CórdobaMejora",
    placa=dict(kicker="Calle por Calle", valor="205", etiqueta="Cuadras de pavimento en 10 días", sub="Plan de 1.100 nuevas cuadras"),
    gac=gac("En diez días de obra, la pavimentación sostiene 205 cuadras en cinco barrios de Córdoba",
        ["Cinco obras en cinco barrios, de manera continua.", "El plan prevé 1.100 nuevas cuadras de pavimento.", "Los plazos de ejecución son de 150 y 210 días calendario."],
        "Entre el 20 y el 29 de octubre, el Gobierno de la Provincia, en conjunto con la Municipalidad de Córdoba, sostuvo en marcha cinco obras de pavimentación que alcanzan 205 cuadras, dentro del plan de “Calle por Calle, Córdoba Mejora” que prevé 1.100 nuevas cuadras en la ciudad.",
        [("Un frente que no se detuvo",
          ["Las obras del Barrio General Arenales, el Barrio Villa Rivadavia Anexo, el Barrio 9 de Julio, el Barrio San Felipe y el Barrio Policial aparecieron de manera sostenida en los partes del período, un reflejo de la continuidad de los trabajos."]),
         ("Plazos y alcance",
          ["Las obras del Barrio Policial y del Barrio San Felipe tienen un plazo de 150 días calendario; las del Barrio General Arenales, el Barrio Villa Rivadavia Anexo y el Barrio 9 de Julio, de 210 días. En el Barrio Policial se prevé, además, sumar 60 cuadras luego de las 19 iniciales."]),
         ("Más que una calle",
          ["La pavimentación no solo permite circular mejor: ordena el desagüe, define las veredas y consolida la urbanización, y con ello mejora la calidad de vida de los vecinos."])],
        "Hacer para Crecer es planificar a largo plazo y sostener cada obra hasta el final: con equilibrio fiscal, la inversión en infraestructura es de todos los cordobeses.", 3))


# ---- frase política corta (IG: un renglón; X: una frase breve) ----
POL = {
  "g_total":     ("Con equilibrio fiscal, Córdoba sostiene la inversión en infraestructura para todos los cordobeses.", "Cuentas en orden, obra para todos."),
  "g_empleo":    ("Con equilibrio fiscal se sostiene la inversión en infraestructura de todos los cordobeses y, con ella, el trabajo.", "Obra pública y trabajo, con equilibrio fiscal."),
  "g_accesible": ("El equilibrio fiscal permite mantener la inversión en infraestructura para todos los cordobeses.", "Equilibrio fiscal: obra para todos."),
  "g_calle":     ("Con las cuentas en orden, la obra pública llega a todos los cordobeses.", "Con equilibrio fiscal, la obra sigue."),
  "g_cuadras":   ("Equilibrio fiscal que se convierte en pavimento para todos los cordobeses.", "Equilibrio fiscal que se hace obra."),
  "g_plazas":    ("Con equilibrio fiscal, la inversión en espacios públicos llega a todos los cordobeses.", "Cuentas en orden, plazas para todos."),
  "g_acum":      ("Con equilibrio fiscal es posible planificar la infraestructura de todos los cordobeses.", "Equilibrio fiscal: obras que se planifican."),
  "g_fin":       ("Obras terminadas con un equilibrio fiscal que sostiene la inversión de todos los cordobeses.", "Cuentas en orden, obra que se termina."),
  "g_fiscal":    ("El modelo cordobés apuesta por el equilibrio fiscal para sostener la inversión en infraestructura de todos los cordobeses.", "Equilibrio fiscal para sostener la infraestructura de todos."),
  "p_7":         ("El equilibrio fiscal sostiene, semana a semana, la inversión en infraestructura de todos los cordobeses.", "Equilibrio fiscal que sostiene la obra."),
  "p_10":        ("Con equilibrio fiscal, la inversión en infraestructura de todos los cordobeses no se frena.", "Cuentas en orden, obra que no se frena."),
  "p_7_plazas":  ("Con las cuentas en orden, la inversión en espacios públicos llega a todos los cordobeses.", "Cuentas en orden, plazas para todos."),
  "p_10_plazas": ("El equilibrio fiscal sostiene la inversión en espacios verdes para todos los cordobeses.", "Equilibrio fiscal que se hace plaza."),
  "p_7_rampas":  ("Con equilibrio fiscal, la accesibilidad llega a todos los cordobeses.", "Equilibrio fiscal: accesibilidad para todos."),
  "p_10_rampas": ("El equilibrio fiscal permite acelerar las obras sin frenar la inversión de todos los cordobeses.", "Cuentas en orden, rampas para todos."),
  "p_7_pav":     ("Equilibrio fiscal para sostener el pavimento de todos los cordobeses.", "Equilibrio fiscal que se hace pavimento."),
  "p_10_pav":    ("Con equilibrio fiscal, la pavimentación de todos los cordobeses sigue su curso.", "Cuentas en orden, calles para todos."),
}
def meter(pieza, ig_line, x_line):
    ig = pieza["ig"]; i = ig.rfind("\n\n#"); pieza["ig"] = ig[:i] + "\n\n" + ig_line + ig[i:]
    x = pieza["x"]; j = x.find(" #"); cand = x[:j] + " " + x_line + x[j:]
    if len(cand) <= 280: pieza["x"] = cand
for k, (a, b) in POL.items():
    meter((G if k.startswith("g_") else PER)[k], a, b)

json.dump(dict(generales=G, periodicos=PER), open(os.path.join(HERE, "contenido.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("generales:", len(G), "periodicos:", len(PER))
