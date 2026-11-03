# Registro de decisiones y mejoras

## Música ambiental

Se añadió un arpegio original suave de fondo en bucle, con prioridad para los efectos. Un efecto interrumpe el fondo y programa su retorno al terminar; un nuevo efecto sustituye el temporizador anterior. El silencio y el cierre cancelan el retorno pendiente. Se ejecutaron seis pruebas automatizadas, incluida una de prioridad de audio con backend simulado, y la comprobación de interfaz: todas pasaron. La prueba automatizada no valora la experiencia auditiva; el volumen final depende del dispositivo.

## 3 de noviembre de 2026 · Ambientación por misión

Se incorporaron cielo claro, selva, cielo al atardecer e infierno fantástico, con paletas de interfaz propias y paisajes pixel art animados. El módulo temas.py comparte los dibujos y colores entre el juego y los mockups. Se generaron SVG de las cuatro misiones y cuatro estados de retroalimentación, además de conservar los nombres generales del primer nivel. Se actualizaron HTML, Word y PDF de entrega. Las cinco pruebas de lógica y la comprobación gráfica automatizada pasaron; esta última verifica el cambio de tema y su restauración al regresar al mapa. Se revisó visualmente una lámina comparativa de los cuatro SVG. No se modificaron las reglas ni se atribuyeron estos cambios a evaluación con usuarios.

| Cambio preparado | Motivo | Verificación |
|---|---|---|
| Cuatro niveles | Cubrir el mínimo técnico más exigente de la guía | Revisar contenido y completar partida |
| Separar lógica e interfaz | Probar reglas sin ventanas y facilitar explicación | Pruebas unitarias |
| Bloquear respuestas repetidas | Evitar duplicar puntos por escena | Caso de doble respuesta |
| Reinicio con restauración | Evitar acumular premios al repetir una misión | Caso de reinicio |
| Mezclar botones | Evitar que la respuesta se aprenda por su posición | Revisión manual |
| Sin dependencias externas | Simplificar ejecución en el aula | Iniciar en Python con Tkinter |

Estas decisiones corresponden a la implementación inicial. No se atribuyen a evaluaciones con usuarios que todavía no se han realizado.

## Mejoras tras evaluación real

Actualización de interfaz solicitada por el autor: tema de terminal hacker, escaneo de ciudad, consola animada, partículas, indicadores de energía y audio arcade original con control de silencio. La navegación cancela las animaciones pendientes y la pantalla admite desplazamiento. Se ejecutaron nuevamente las cinco pruebas lógicas y `pruebas/verificar_interfaz.py`: todas pasaron. Esta última comprobó WAV válidos, respuestas, daño, recuperación, victoria, derrota y cambios repetidos de pantalla sin errores de callbacks. La apariencia y reproducción audible requieren revisión humana; no se atribuyen estos cambios a pruebas con usuarios.

| Fecha | Evidencia o comentario | Cambio aplicado | Resultado comprobado |
|---|---|---|---|
| Pendiente | Pendiente | Pendiente | Pendiente |
