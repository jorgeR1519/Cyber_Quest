# Registro de decisiones y mejoras

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
