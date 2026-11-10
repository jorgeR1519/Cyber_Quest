# CyberQuest: Los guardianes del escudo

## Primera parte · Análisis y diseño

**Autor:** Jorge Enrique Rentería Mosquera · Trabajo individual.

**Institución:** Institución Universitaria Antonio José Camacho.

**Programa:** Ingeniería de Sistemas · Tercer semestre · Programación III.

**Docente:** José Alejandro Martínez Pérez. **Grupo:** por completar por el autor.

**Corte del avance:** 10 de noviembre de 2026. **Presentación prevista por el autor:** 11 de noviembre de 2026. La pieza original del docente indica el 12 de noviembre; se conserva esta diferencia para no alterar la fuente.

**Alcance:** esta entrega presenta los seis productos de análisis y diseño. El prototipo 2D se utiliza para demostrar la viabilidad de las decisiones. Las consultas a participantes externos todavía no se han realizado.

## Índice de productos y evidencias

| Producto requerido | Dónde se encuentra | Estado |
|---|---|---|
| Análisis y relación con ODS | Sección 1 e instrumento de investigación | Documento preparado; evidencia local externa pendiente |
| GDD inicial | Secciones 2 y 3 | Preparado y relacionado con el prototipo actual |
| Storyboard o bosquejo | Sección 4 y storyboard.svg | Preparado |
| Mockups: menú, nivel y retroalimentación | Sección 5, archivos SVG y capturas de prototipo | Preparados |
| Diseño algorítmico | Sección 6, pseudocódigo y diagramas SVG | Preparado y contrastado con el código |
| Evidencia Kanban | Sección 7 y exportación del tablero real | Consultada y actualizada; actividad verificable en Notion |

# 1. Análisis de la problemática y ODS

## Contexto y formulación

El contexto propuesto es la comunidad de estudiantes que utiliza correo, plataformas académicas y servicios digitales. Se plantea como hipótesis que algunas personas pueden tener dificultades para reconocer mensajes fraudulentos, proteger cuentas y responder de forma prudente ante alertas.

El problema aún no está medido en esta población: no se dispone de estadísticas locales, encuestas contestadas ni entrevistas con participantes externos. Los riesgos que motivan el proyecto son la exposición a engaños, acceso indebido a cuentas y pérdida de información. Se presentan como riesgos del contexto de uso, no como incidentes confirmados en la institución.

**Pregunta de diseño:** ¿cómo facilitar que estudiantes practiquen acciones de protección digital mediante una aventura 2D comprensible, donde explorar, inspeccionar y actuar produzca consecuencias visibles?

## Público objetivo

Estudiantes universitarios y jóvenes usuarios de servicios digitales, sin exigir conocimiento previo de ciberseguridad. La validación prevista se hará con compañeros voluntarios y respuestas anónimas. La muestra propuesta de 3–5 personas sirve para identificar problemas iniciales de comprensión; no permite generalizar a toda la institución.

## Justificación y propuesta de valor

Una aventura permite ensayar acciones sin usar cuentas reales. El jugador reconoce pistas dentro de objetos, los transporta, activa mecanismos y recibe consecuencias. La historia une las prácticas de seguridad con el cuidado de una ciudad ficticia. El aprendizaje se propone desde la acción y la reflexión, y deberá evaluarse con personas antes de afirmar que resulta efectivo.

## Objetivo general

Diseñar una aventura educativa 2D que permita practicar verificación de mensajes, protección de cuentas y respuesta básica ante incidentes mediante cuatro misiones con personajes y objetivos espaciales.

## Objetivos específicos

1. Identificar necesidades mediante consultas voluntarias y registro de hallazgos reales.
2. Relacionar cada contenido educativo con una acción del mundo y su consecuencia.
3. Diseñar narrativa, personajes, niveles, interfaz y reglas coherentes.
4. Representar y comprobar los algoritmos de movimiento, interacción y progresión.
5. Evaluar claridad y dificultad, registrar mejoras y gestionar tareas en Kanban.

## Relación con ODS 4

El proyecto se alinea principalmente con el **ODS 4: Educación de calidad**, en especial con la orientación de la meta 4.4 sobre competencias relevantes y del indicador 4.4.1 sobre habilidades TIC. La contribución propuesta es ofrecer práctica educativa de decisiones de protección digital. No se afirma que el videojuego mida el indicador oficial ni que haya demostrado impacto en la meta.

La relación se fundamenta en la fuente institucional de Naciones Unidas: https://sdgs.un.org/goals/goal4. ODS 9 se considera un vínculo secundario con el uso de tecnología; no es necesario para justificar la entrega y no se le atribuye impacto medido.

# 2. Definición de la solución y Design Thinking

## Alternativas y selección

| Alternativa considerada | Ventajas | Limitaciones y decisión |
|---|---|---|
| Cuestionario narrativo | Fácil de construir y explicar | El docente solicitó un juego tradicional; se conserva como antecedente |
| Aventura 2D vista desde arriba | Personaje controlable, exploración, objetos, colisiones y narrativa | Seleccionada por su relación con el encargo y su viabilidad |
| Aventura 3D | Mayor representación espacial | Exige más recursos de modelado y programación que el alcance disponible |

La solución elegida es una aventura 2D con Python y Pygame CE. Se priorizan mapas pequeños, sprites propios, objetivos claros y cuatro sistemas de misión. La elección es una decisión de alcance técnico; no es el resultado de una encuesta realizada.

## Evidencia de las cinco fases

| Fase | Qué se hizo o preparó | Evidencia real y límite |
|---|---|---|
| Empatizar | Identificar público, hipótesis y dificultades comunicadas por el autor | Comentarios del autor sobre orientación y dificultad; consultas externas pendientes |
| Definir | Formular problema, público, objetivos y alcance de aventura | Este informe y GDD; contrastar el problema local después de consultar |
| Idear | Comparar cuestionario, aventura 2D y 3D | Comparación anterior; cambio solicitado tras observación docente comunicada por el estudiante |
| Prototipar | Construir mapas, personaje, inventario, diálogos y objetivos | Código, mockups SVG y capturas del renderizador |
| Evaluar | Probar reglas y atender comentarios del autor | 19 pruebas automatizadas y prueba gráfica; evaluación con jugadores externos pendiente |

## Retroalimentación real que produjo cambios

| Evidencia registrada en la conversación | Cambio de diseño | Límite |
|---|---|---|
| El autor indicó que no entendía qué hacer dentro del juego | Tutorial, identificación del guardián, siguiente paso, destino resaltado y ruta parcial | Retroalimentación del autor |
| El autor indicó que los monstruos solo se movían de izquierda a derecha | Detección, alerta, persecución, memoria, cobertura y regreso | Retroalimentación del autor |
| El autor pidió Fácil, Medio y Difícil | Selector previo y configuración centralizada por modo | Preferencia de diseño del autor |
| El autor comunicó que el docente exigía juego tradicional 2D o 3D | Sustitución del cuestionario por exploración con movimiento y personajes | Indicación docente comunicada por el autor |

Estos son comentarios del propio autor del proyecto, no una investigación independiente con varias personas. La encuesta y el protocolo de prueba incluidos al final deben aplicarse para ampliar la validación.

# 3. GDD inicial · Diseño de la experiencia

## Identidad

**Nombre:** CyberQuest: Los guardianes del escudo. **Género:** aventura educativa 2D vista desde arriba. **Plataforma:** escritorio con teclado. **Tecnología:** Python y Pygame CE 2.5.8. **Estética:** pixel art dibujado con código, paletas cálidas y ambientación por distrito.

## Historia y personajes

Sombra está apagando las defensas de una ciudad digital. El guardián comienza en las islas de Ada, busca nuevas llaves en la selva de Leo, ayuda a Iris a contener estaciones comprometidas y entra en una fortaleza de lava para rescatar habitantes y reactivar el escudo.

| Personaje | Función en la aventura |
|---|---|
| Guardián de sombrero rojo | Personaje controlado por el jugador |
| Ada | Guía inicial y ayuda contextual por radio |
| Leo | Custodio de las llaves de la selva |
| Iris | Técnica que coordina la contención y el reporte |
| Noa, Sol y Teo | Habitantes que se rescatan en la fortaleza |
| Sombra y centinelas | Amenazas móviles que detectan y persiguen |

## Escenarios, objetivos y aprendizaje

| Distrito | Objetivo jugable | Acciones y relación educativa |
|---|---|---|
| Cielo: El correo de las nubes | Entregar tres paquetes de forma segura | Inspeccionar remitente y dominio, recoger un paquete por vez y llevarlo al correo oficial o a cuarentena |
| Selva: Las llaves de la selva | Renovar dos defensas de una cuenta | Recoger tres fragmentos, forjar una llave única y activar segundo factor con un sello de recuperación |
| Atardecer: Estaciones al atardecer | Contener y reportar | Desconectar tres estaciones y llegar al soporte para entregar el reporte |
| Lava: El corazón de Sombra | Rescatar y activar el núcleo | Recoger cristales, alimentar tres balizas, rescatar habitantes y completar el escudo |

## Mecánicas y reglas

El personaje se mueve con WASD o flechas y colisiona con paredes. E/Enter permite hablar, recoger, entregar y activar; F inspecciona objetos o el paquete transportado. Espacio activa un impulso breve con recarga. H consume una llamada a Ada. T abre una guía gratuita. Esc pausa y R solicita reinicio con confirmación.

Antes de activar objetivos se habla con el personaje del refugio. Los objetos y mecanismos exigen requisitos concretos: inspeccionar antes de entregar, reunir fragmentos antes de forjar, completar estaciones antes de reportar y activar una baliza antes de rescatar. Los portales verifican los objetivos completos. No hay botones de respuestas.

El mapa usa 26 × 17 casillas de 32 píxeles. El personaje ocupa un rectángulo de colisión de 20 × 24 píxeles. La vista lógica es de 1200 × 800 y se escala con la ventana. El diario conserva el siguiente paso, progreso, mochila y controles. Las marcas doradas indican una ruta parcial que evita obstáculos fijos; el jugador debe esquivar las amenazas móviles.

## Recursos, premios y penalizaciones

Recoger fragmentos, sellos y cristales concede 25 XP. Entregas, mecanismos, estaciones, reportes, balizas y rescates conceden 100 XP. Completar un distrito concede 200 XP. Máximo de la campaña sin daño: 2475 XP. Cada objeto concede su recompensa una sola vez.

Recibir daño resta una energía y hasta 20 XP, sin bajar de cero, y devuelve al guardián al refugio conservando objetos. Existe protección temporal para evitar pérdidas consecutivas inmediatas. Las frutas recuperan una energía hasta el máximo y no se consumen si este ya está completo. La pausa y los diálogos detienen las amenazas. Reiniciar restaura el estado de entrada al distrito, incluidas llamadas y puntos.

## Tres modos estructurados

| Parámetro | Fácil | Medio | Difícil |
|---|---|---|---|
| Energía inicial/máxima | 7 | 5 | 3 |
| Radio por partida | 5 llamadas | 3 llamadas | 1 llamada |
| Recuperación al terminar distrito | Hasta 2 | Hasta 1 | Ninguna |
| Velocidad enemiga respecto a base | 75 % | 100 % | 118 % |
| Alcance de detección respecto a base | 80 % | 100 % | 115 % |
| Advertencia antes de persecución | 0,90 s | 0,55 s | 0,35 s |
| Memoria tras perder visión | 1,4 s | 2,2 s | 3,2 s |
| Recarga del impulso | 0,9 s | 1,2 s | 1,6 s |

El modo se elige antes de empezar y se mantiene durante la campaña. Medio está seleccionado inicialmente. Los contenidos, objetivos, premios, refugio y guía gratuita se mantienen en los tres. La velocidad base de persecución aumenta por distrito: 128, 145, 160 y 178 píxeles por segundo, multiplicados por el modo elegido. El guardián camina a 165.

## Enemigos y progresión

Los centinelas patrullan, detectan al guardián por distancia y visión, muestran una advertencia y persiguen. Las paredes bloquean su visión y su movimiento. Si pierden el rastro buscan la última posición y vuelven a su zona. El refugio inicial queda protegido. La fortaleza exige usar cobertura e impulso con mayor atención.

**Victoria:** completar los cuatro distritos y activar el núcleo. **Derrota:** energía cero; se puede reintentar el distrito o iniciar otra partida. El progreso permanece solo durante la sesión, sin guardado en disco.

# 4. Storyboard y flujo de navegación

| Viñeta | Qué aparece | Acción del jugador | Consecuencia |
|---|---|---|---|
| 1 | Menú con cuatro mundos y tres dificultades | Seleccionar modo, escribir nombre y comenzar | Crear partida |
| 2 | Introducción y guía inicial | Avanzar textos con E/Enter | Identificar personaje y controles |
| 3 | Refugio de Ada | Moverse y hablar con E | Activar misión y siguiente paso |
| 4 | Paquete en el mapa | Usar F, leer evidencia y recoger con E | Registrar inspección y transportar |
| 5 | Camino con paredes y centinelas | Rodear obstáculos, usar cobertura e impulso | Alcanzar la terminal o recibir daño |
| 6 | Terminal de correo/cuarentena | Entregar con E | Mostrar consecuencia, XP y progreso |
| 7 | Portal abierto y nuevos mundos | Completar requisitos y cruzar | Nuevas mecánicas y progresión |
| 8 | Núcleo final o energía agotada | Activar escudo o reintentar | Victoria o derrota con cierre narrativo |

La lámina storyboard.svg y el diagrama flujo_navegacion.svg representan visualmente esta secuencia.

# 5. Mockups de la interfaz

El mínimo de la guía se cubre con **menú principal, nivel jugable y retroalimentación**. Se adjuntan SVG del menú con selector de dificultad, mapa con personaje e inventario, diálogos y una lámina específica de retroalimentación posterior a una entrega.

Los mockups son representaciones de diseño. Las capturas PNG se obtuvieron del renderizador real en estados preparados para documentación; no se presentan como una sesión de evaluación con participantes. La lámina de retroalimentación explica la entrega correcta y muestra el resultado dentro del mundo.

Criterios: controles visibles, objetivo persistente, texto legible, estado de energía claro, consecuencias por escrito y orientación que no dependa exclusivamente del sonido. La música relajante y los efectos originales pueden silenciarse.

# 6. Diseño de la solución algorítmica

## Descomposición y conceptos de Programación III

| Concepto | Necesidad concreta | Evidencia de código |
|---|---|---|
| Variables y tipos | Posición, energía, XP y estado | motor.py |
| Secuencias | Validar una interacción antes de premiar | Juego.interactuar |
| Condicionales | Requisitos, colisiones, victoria y derrota | motor.py |
| Ciclos | Actualizar enemigos y dibujar objetos | motor.py; aventura.py |
| Ciclos anidados | Recorrer casillas y píxeles del personaje | Aplicacion.dibujar_mundo y personaje |
| Listas y arreglos | Mapas, objetos y centinelas | mundos.py |
| Diccionarios y conjuntos | Atributos de objetos y objetivos completados | mundos.py; motor.py |
| Funciones y métodos | Reutilizar movimiento, visión y guía | motor.py; inteligencia.py |
| Validaciones | Nombres, alcance de interacción y requisitos | Juego.__init__, cercano e interactuar |

Reconocimiento de patrones: los niveles comparten refugio, personaje guía, objetos, objetivo y portal. Abstracción: riesgos digitales se representan mediante paquetes, llaves y estaciones sin ejecutar ataques reales. El problema se descompone en datos del mundo, reglas, presentación, inteligencia, audio y validación.

## Entrada – Proceso – Salida

| Entrada | Proceso | Salida |
|---|---|---|
| Nombre y dificultad | Validar y cargar configuración | Partida y recursos iniciales |
| Dirección y tiempo de frame | Normalizar, mover por subpasos y comprobar paredes | Posición válida |
| E cerca de un objeto | Validar distancia, pared y requisitos | Diálogo, inventario o progreso |
| F | Consultar evidencia del objeto o paquete | Inspección registrada |
| Contacto con amenaza | Comprobar protección y aplicar daño | Energía, puntos y retorno al refugio |
| Objetivos completos y portal | Verificar progreso | Siguiente distrito o victoria |

## Pseudocódigo del ciclo principal

```text
INICIAR menú, ventana y audio
MIENTRAS la aplicación esté abierta:
    LEER eventos de cierre, teclado y botones
    SI hay partida y no hay diálogo ni pausa:
        ACTUALIZAR temporizadores
        MOVER jugador evitando paredes
        ACTUALIZAR visión, rutas y estados de centinelas
        DETECTAR daño por contacto y peligros
    PROCESAR mensajes, efectos y animaciones
    DIBUJAR mundo, personaje, objetos, diario y diálogos
    PRESENTAR imagen escalada a la ventana
CERRAR audio y ventana
```

## Pseudocódigo de interacción y progreso

```text
SI hay diálogo: avanzar texto y terminar
BUSCAR objeto cercano sin pared intermedia
SI no existe: indicar que debe acercarse
SI es personaje: registrar conversación y mostrar instrucciones
SI es mecanismo: comprobar recursos y objetivos previos
SI es entrega: exigir inspección y destino correcto
SI es portal:
    SI faltan objetivos: explicar qué falta
    SI están completos: registrar distrito y avanzar o ganar
MARCAR objeto completado y conceder premio una sola vez
```

## Movimiento, persecución y guía

El movimiento se divide en subpasos de hasta cinco píxeles y se valida por eje para no atravesar paredes. La diagonal se normaliza. La visión enemiga usa distancia e intersección del segmento hacia el jugador con paredes. Los enemigos tienen estados explícitos y calculan rutas mediante búsqueda en anchura sobre casillas transitables. La guía aplica la misma idea de navegación para marcar próximos pasos entre obstáculos estáticos.

Se adjuntan los diagramas flujo_interaccion.svg y flujo_navegacion.svg. El pseudocódigo se corresponde con motor.py, inteligencia.py y aventura.py, sin agregar estructuras solo para cumplir una lista.

## Validación y límites

La suite actual contiene **19 pruebas unitarias** y una comprobación gráfica. Cubren accesibilidad de objetos, campaña determinista, requisitos, puntuación, daño, reinicio, radio, modos, persecución, cobertura, refugio y audio. La prueba de campaña desactiva centinelas para comprobar rutas de forma repetible. El renderizado se comprueba con vídeo dummy. La dificultad y la comprensión por jugadores externos siguen pendientes de evaluación.

# 7. Gestión Kanban y avance

**Tablero real:** https://app.notion.com/p/190e3d2ac5714a58a4b651dd81806d15.

El 10 de noviembre se revisó el tablero y se actualizaron sus tareas para reflejar la aventura 2D. Las cinco columnas son LISTA GENERAL DE ACTIVIDADES, POR HACER, EN PROCESO, EN REVISION y TERMINADO. Las tarjetas incluyen nombre, descripción, responsable único, plazo, prioridad, evidencia y estado.

Se adjunta una exportación de los datos reales y una vista imprimible con enlace a las tarjetas. Es evidencia de consulta del tablero, no una captura de la interfaz de Notion ni una reconstrucción de actividad pasada. Los estados preparados para revisión no equivalen a aprobación del docente. Las tareas de consulta y evaluación externa permanecen pendientes.

# 8. Investigación y evaluación: instrumentos listos

Se adjuntan encuesta, guía de observación y hoja de registro vacía. No existen respuestas externas confirmadas al corte de esta entrega. Las plantillas se entregan como instrumentos por aplicar; no deben presentarse como resultados.

Para una aplicación breve, solicitar participación voluntaria y usar códigos P01–P05. No pedir nombres de cuentas ni contraseñas. Pedir que la persona juegue el inicio en Fácil, observe el diario y explique con sus palabras cómo identificar y entregar un mensaje. Registrar dificultades y ajustar el prototipo.

# 9. Declaración y pendientes finales

Se utilizó asistencia de Codex para código, pruebas y borradores. El autor debe comprender el material y declarar su uso según las orientaciones del curso. Los dibujos y audio se generan con código propio. Las fuentes académicas del encargo son el PDF y la pieza gráfica suministrados por el estudiante; las observaciones del docente se registran como comunicadas por el autor.

Antes de presentar: completar grupo si corresponde, revisar el documento, ensayar menos de 10 minutos, abrir el tablero real y guardar una captura manual si el docente la solicita. Las entrevistas y la evaluación externa deben declararse como pendientes mientras no se realicen.
