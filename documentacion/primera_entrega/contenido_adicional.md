# Alcance y portada de la primera entrega

**Proyecto:** CyberQuest: Defensa Digital.

**Institución:** Institución Universitaria Antonio José Camacho.

**Programa y curso:** Ingeniería de Sistemas, tercer semestre, Programación III.

**Docente:** José Alejandro Martínez Pérez, según la guía original.

**Autor principal provisional:** Jorge Enrique Rentería Mosquera. Integrantes adicionales y grupo: por completar. La guía solicita participación del equipo; confirmar modalidad autorizada.

**Fecha de preparación:** 30 de octubre de 2026. Sustentación: 12 de noviembre, durante la clase, máximo 10 minutos, según la imagen. Se asume el año del curso, pues la imagen no lo especifica.

Esta entrega presenta el análisis y diseño. El código disponible se utiliza como prototipo de apoyo; no reemplaza las evidencias de investigación ni el tablero Kanban real.

## Correspondencia con los seis productos

| Producto solicitado | Material incluido | Estado |
|---|---|---|
| Análisis y ODS | Análisis, público, objetivos y relación con ODS 4 | Borrador; validar problema local |
| GDD inicial | Narrativa, personajes, niveles, reglas y recursos | Preparado para revisión |
| Storyboard o bosquejo | Secuencia de ocho escenas con acciones y transiciones | Preparado |
| Mockups | Menú, nivel y retroalimentación; archivos SVG | Preparados; evaluar con usuarios |
| Diseño algorítmico | Pseudocódigo, flujo, datos y conceptos usados | Preparado |
| Evidencia Kanban | CSV de tarjetas y guía de captura | Tablero y evidencia real pendientes |

# Propuesta de solución y aprendizaje

## Pregunta de diseño

¿Cómo facilitar que estudiantes del entorno universitario practiquen la identificación de mensajes sospechosos y decisiones de protección digital mediante una aventura breve y comprensible?

## Propuesta de valor

CyberQuest conecta situaciones cotidianas de seguridad digital con una ciudad ficticia que el jugador ayuda a proteger. Examinar señales, elegir acciones y recibir consecuencias sobre energía y progreso ofrece una oportunidad de practicar sin exponer cuentas ni datos reales. A diferencia de una lista aislada de preguntas, cada decisión forma parte de una misión con continuidad narrativa.

## Público y alcance

Público propuesto: estudiantes universitarios y jóvenes usuarios de correo y plataformas digitales. Contexto de validación propuesto: compañeros del curso en la Institución Universitaria Antonio José Camacho; falta confirmar participantes y recoger evidencia. No se requiere conocimiento previo de ciberseguridad.

El juego no solicita claves reales, no abre enlaces de amenazas y no simula ataques contra terceros. Representa incidentes con textos ficticios. La versión local no guarda progreso al cerrar.

## Objetivos de aprendizaje observables

| Objetivo | Actividad | Cómo se observará |
|---|---|---|
| Identificar señales de un mensaje sospechoso | Examinar remitente, dominio y urgencia en el nivel 1 | El participante identifica señales y explica por qué verifica por otro canal |
| Distinguir protección débil y más segura de cuentas | Clave única y multifactor en el nivel 2 | Selección de medidas y explicación con sus palabras |
| Elegir una respuesta prudente ante una alerta | Evitar descargas y seguir protocolo en el nivel 3 | Describe cómo reportar sin agravar el incidente |
| Integrar las medidas aprendidas | Tres situaciones en el nivel 4 | Justifica decisiones de verificación, acceso y reporte |

Los puntos reflejan decisiones de la partida. No demuestran por sí solos que hubo aprendizaje; se requiere observar y consultar a los participantes.

## Relación principal con ODS 4

La meta 4.4 aborda competencias relevantes de jóvenes y adultos; el indicador 4.4.1 se refiere a habilidades TIC. CyberQuest propone practicar decisiones de protección digital, por lo que su alineación educativa se fundamenta en esa orientación. No se afirma que el juego mida el indicador oficial ni que su impacto esté demostrado. Fuente: Naciones Unidas, https://sdgs.un.org/goals/goal4 (consulta: 30 de octubre de 2026).

ODS 9 se conserva como vínculo secundario y contextual con innovación tecnológica. Crear un programa académico no demuestra por sí solo avance en sus metas; para esta primera entrega se prioriza ODS 4, que tiene una relación más directa con el aprendizaje propuesto. Fuente: Naciones Unidas, https://sdgs.un.org/goals/goal9 (consulta: 30 de octubre de 2026).

# Storyboard · recorrido de una partida

| Viñeta | Qué ve el jugador | Acción y consecuencia | Siguiente pantalla |
|---|---|---|---|
| 1. Bienvenida | Ciudad cálida en pixel art, guardián, nombre y reglas | Escribe nombre válido y comienza; si está vacío se solicita corregir | Menú de misiones |
| 2. Elegir sector | Cuatro misiones; solo la primera disponible | Abre el sector 1; las siguientes permanecen bloqueadas | Nivel 1 |
| 3. Incidente | Ada recibe un aviso de bloqueo urgente | Lee el contexto y solicita examinar evidencia | Mismo nivel con pista visible |
| 4. Investigar | Remitente, dominio y petición sospechosos | Compara dos acciones posibles; no hay límite de tiempo | Decisión |
| 5. Consecuencia segura | Mensaje de defensa reforzada, confeti y sonido | +100 XP; energía sin cambios; lee la explicación | Continuar a otra escena |
| 6. Consecuencia riesgosa | Alerta textual y visual con sonido distinto | −50 XP sin bajar de 0 y −1 energía; si llega a 0 habrá derrota | Continuar o resultado final |
| 7. Sector completado | Mapa con nueva misión disponible | Recupera 1 energía hasta máximo 3; se conserva el progreso | Siguiente misión |
| 8. Cierre | Victoria tras cuatro sectores o derrota sin energía | Revisa puntuación y temas a repasar; puede iniciar otra partida | Bienvenida |

## Experiencia de usuario y decisiones visuales

Fondo crema, paneles melocotón, texto oscuro y acentos terracota. La ciudad y el personaje utilizan bloques de pixel art dibujados con código. El estilo cálido fue solicitado por el autor durante el desarrollo; no se atribuye a pruebas con usuarios.

Las acciones tienen textos explícitos. El orden de las opciones se mezcla para evitar memorizar posiciones. Las consecuencias se explican por escrito y con recursos visuales; los sonidos se pueden silenciar. La ventana permite desplazamiento vertical. Los mockups representan estados del juego, no botones funcionales ni capturas de la aplicación.

## Criterios de aceptación de los mockups

La ambientación debe abarcar la ventana completa, con decoración temática en el fondo y ambos laterales, panel central legible y controles del mismo tema. El diseño debe seguir siendo claro al reducir la ventana; los textos se ajustan al ancho disponible. Los SVG por misión representan esta composición completa.

Actualización visual del 3 de noviembre de 2026: se incluyen mockup_mision_1.svg a mockup_mision_4.svg y cuatro SVG de retroalimentación correspondientes. Las ambientaciones son cielo claro, selva, cielo al atardecer e infierno fantástico. Los nombres generales mockup_nivel.svg y mockup_retroalimentacion.svg representan la primera misión. Todos utilizan las mismas paletas y bloques de paisaje que la interfaz; son diseños, no capturas de ejecución.

Menú: identifica las cuatro misiones, su estado, puntos y energía. Nivel: muestra contexto, pista y acciones diferenciadas. Retroalimentación: explica la decisión, refleja recursos y permite continuar. La evaluación de legibilidad y comprensión con compañeros está pendiente.

# Anexos de investigación y evaluación

## Registro de empatía pendiente

Realizar 3–5 consultas breves como alcance propuesto, sin recopilar claves, nombres de cuentas ni detalles sensibles. Preguntar por señales de desconfianza, reacción ante solicitudes de códigos y respuesta ante alertas. La participación debe ser voluntaria.

| Código anónimo | Fecha | Situación consultada | Respuesta o dificultad observada | Necesidad deducida |
|---|---|---|---|---|
| P01 | Por completar | Por completar | Por completar tras la actividad | Por completar |
| P02 | Por completar | Por completar | Por completar tras la actividad | Por completar |
| P03 | Por completar | Por completar | Por completar tras la actividad | Por completar |

Después de recoger evidencia: agrupar dificultades repetidas, seleccionar las más relevantes y revisar la pregunta de diseño. Separar las respuestas textuales de las interpretaciones del equipo.

## Evaluación de mockups pendiente

Pedir a un compañero que identifique dónde empieza, cómo examina una pista y qué cambia tras una decisión. Registrar si lo entiende sin explicación adicional y qué términos generan confusión.

| Fecha / participante | Tarea | Dificultad observada o comentario | Cambio propuesto | Verificación posterior |
|---|---|---|---|---|
| Por completar | Encontrar primera misión | Pendiente de observación | Por decidir | Pendiente |
| Por completar | Explicar pérdida de energía | Pendiente de observación | Por decidir | Pendiente |

# Gestión Kanban y evidencias

Se prepara un CSV para trasladar tarjetas a un tablero digital. No se ha creado ni consultado un tablero externo durante la preparación de este paquete.

Columnas: LISTA GENERAL DE ACTIVIDADES, POR HACER, EN PROCESO, EN REVISIÓN y TERMINADO. Cada tarjeta debe contener descripción, responsable, plazo, prioridad, evidencia y estado. Las fechas del CSV son una planificación propuesta para llegar al 12 de noviembre; ajustarlas al calendario y al equipo real.

## Evidencia que debe incorporarse

| Evidencia | Contenido requerido | Estado |
|---|---|---|
| Enlace del tablero | URL accesible al docente | Por completar |
| Captura general | Columnas, tarjetas y avance legibles, con fecha | Pendiente |
| Detalle de una tarjeta | Responsable, fecha, descripción, prioridad y evidencia | Pendiente |
| Historial o actividad | Movimientos y aportes reales del equipo | Pendiente |

No mover todas las tareas a TERMINADO para simular seguimiento. Registrar el estado real desde la creación del tablero; los documentos preparados deben pasar por revisión antes de aceptarse.

# Sustentación · guion de máximo 10 minutos

| Tiempo | Contenido | Evidencia a mostrar |
|---|---|---|
| 0:00–1:15 | Problema, contexto y público | Análisis y hallazgos reales si ya se recogieron |
| 1:15–2:00 | Objetivos educativos, propuesta y ODS 4 | Objetivos y justificación |
| 2:00–3:15 | Cinco fases de Design Thinking | Consultas, alternativas y evaluación; señalar lo pendiente |
| 3:15–4:45 | GDD: historia, cuatro niveles y reglas | Tabla de niveles y recursos |
| 4:45–6:15 | Storyboard y tres mockups | Secuencia de incidente, decisión y consecuencia |
| 6:15–7:45 | Solución algorítmica | Pseudocódigo de decidir y continuar; listas y métodos |
| 7:45–8:45 | Kanban y avance | Enlace, capturas y tarjetas reales |
| 8:45–9:30 | Conclusiones y próximos pasos | Pendientes y mejoras; reservar 30 segundos de margen |

Asignar bloques a todos los integrantes antes de ensayar. No reemplazar la presentación de análisis y diseño por una demostración extensa del código.

## Declaración de herramientas y fuentes

Se utilizó asistencia de Codex para redactar borradores, organizar documentos y generar código y diseños. El autor y su equipo deben revisar el contenido, comprenderlo y declarar su uso de acuerdo con las orientaciones del profesor. Los sprites y mockups son dibujos generados con código. No se presentan estadísticas ni testimonios inventados.

Fuentes del encargo: PDF de proyecto de aula de Programación III e imagen “Avance proyecto PROGRAMACIÓN”, suministrados por el estudiante. El documento de contexto CyberQuest se utiliza como propuesta de diseño, no como sustituto de la guía del docente.
