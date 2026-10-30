# GENERADOR DE CONTENIDO · Prensa, Gobierno de la Provincia de Córdoba

## Qué es y hacia dónde va
Herramienta de prensa que convierte información oficial del día en contenido listo para usar: copys de Instagram, textos para X (máx. 280), texto de placa editable, gacetillas, placas PNG (1:1, 4:5, 9:16) y lecturas periódicas. Hoy funciona con un solo módulo, OBRAS (el parte diario de la Municipalidad de Córdoba). Va a crecer en módulos de otros temas y a servir a toda la provincia. Cada módulo se suma sin romper los anteriores.

## Regla innegociable
Nunca inventar datos: montos, cifras, metros, plazos, empleo, nombres, citas. Si falta un dato, el texto no lo lleva y se marca en el Chequeo de calidad. Ante una duda que pueda salir cara, preguntar antes.

## Cómo está organizado el conocimiento
- Estas instrucciones: reglas que valen para TODOS los módulos.
- `modulo_<tema>.md`: flujo diario, reglas de datos, errores resueltos y pendientes de cada módulo. Hoy existe `modulo_obras.md`.
- Por módulo: `esquema_<tema>.md`, `muestra_<tema>.json` y diccionarios `dic_<tema>_*.csv`.
- Transversales: `marca_resumen.md` y `codigo_pipeline.md` (más `codigo_plantilla.md`, opcional).
- Ante cualquier tarea, primero ubicar el módulo y leer su archivo. No pedir de nuevo lo que ya está subido. Para un cambio de código, entregar el archivo o fragmento completo a reemplazar.

## Reglas transversales de redacción
- Jamás las palabras "circuito" ni "seccional" en un texto publicable: hablar de barrios, siempre con "Barrio" delante ("Barrio X y Barrio Y"). Los códigos internos sirven solo para agrupar.
- Sin montos ni signos de pesos. Sin "/" (usar "y"; los links quedan). Sin números sueltos: cada cifra con su sustantivo.
- Orden institucional: "Gobierno de la Provincia en conjunto con la Municipalidad de Córdoba" cuando corresponda.
- Tono de prensa.cba.gov.ar: claro, oficial, sin adjetivación excesiva.
- Mensaje político: el modelo cordobés, Hacer para Crecer, con equilibrio fiscal se sostiene la inversión en infraestructura de todos los cordobeses. Cada copy de IG y X lleva UNA línea corta, variada: no repetir la misma frase en todos lados. Las definiciones largas de programa van solo en gacetillas.
- Los planes y metas se dicen "prevé" o "contempla"; solo lo ejecutado se dice en pasado o presente.
- Textos de X: nunca cortados; se resume el mensaje, no se trunca la frase.
- Lo redactado a mano en el día (generales, periódicos, por tipo) varía entre días y entre piezas; lo automático rota variantes.

## Marca y estilo visual
Poppins; colores, pies y logos por eje en `marca_resumen.md`. Placas con 3 diseños de foto (Círculo, Marco, Completa), "Sugerido" por calidad de foto y "Sin foto"; historias 9:16 con zona segura. Título del tablero: GENERADOR DE CONTENIDO. Pestaña "Chequeo de calidad" en gris, a la derecha. Toda la marca sale de la paleta y los SVG del repo, nunca de memoria.

## Cómo agregar un módulo nuevo (checklist)
1. Definir con el equipo: tema, fuente de datos (quién la manda y con qué formato), frecuencia, formatos de salida y reglas propias.
2. Pedir 2 o 3 ejemplos reales y armar `esquema_<tema>.md` y `muestra_<tema>.json`.
3. Reutilizar el pipeline (lista → parse → datos → contenido → build → Chequeo de calidad). Un parser por fuente, una plantilla por familia de piezas. Lo común no se copia: se comparte.
4. Escribir `modulo_<tema>.md` con la misma estructura que `modulo_obras.md`.
5. Sumar al Chequeo de calidad las reglas nuevas del módulo, probar con datos reales y mostrar antes de publicar.
6. Agregar el módulo a la tabla de estado de abajo.

## Alcance provincial: decisiones abiertas
Antes de sumar otras áreas o municipios, definir con el equipo: qué organismos y marcas entran, cómo se identifica la zona o jurisdicción de cada contenido, si cada área tiene su paleta y logos, quién valida los datos y cómo se cargan las fuentes de cada área. No suponer: preguntar.

## Estado de módulos
| Módulo | Estado | Archivo |
|---|---|---|
| Obras (parte diario) | En uso | modulo_obras.md |
| Por seccional | Primera versión eliminada, a definir | modulo_obras.md |
| Otros temas | A definir | — |

## Publicación
Repo privado `cataserena00-lang/generador-de-contenido` en GitHub y proyecto de Vercel con el mismo nombre. Se sube `deploy/index.html` por la web de GitHub y Vercel despliega solo. Acceso por Basic Auth (middleware; variables TABLERO_USUARIO y TABLERO_CLAVE en Vercel). Verificar: despliegue Ready y el sitio responde 401 sin credenciales. Nunca publicar sin un "sí" explícito del equipo. Nunca escribir claves, tokens ni usuarios en archivos, chats ni documentos del Proyecto.

## Trabajo en equipo
- Un solo responsable del deploy: quien tiene las cuentas de GitHub y Vercel. La otra persona deja el build listo y avisa; no publica.
- No trabajar dos personas sobre el mismo día, parte o módulo a la vez: avisar al empezar y al cerrar.
- Traspaso corto al cerrar cada tarea (5 líneas): qué se hizo, qué queda pendiente, archivos tocados, estado (borrador, build listo o publicado) y dudas abiertas.
- Cambios de código: uno por vez, con el motivo. Git: nada destructivo (reset --hard, push --force, checkout o clean sobre cambios ajenos, borrar ramas); solo commits nuevos.
- No tocar otros proyectos de la carpeta (tablero, planificador, viviendas).
- Al cerrar cada tarea, actualizar el estado y los pendientes en `modulo_<tema>.md`.
