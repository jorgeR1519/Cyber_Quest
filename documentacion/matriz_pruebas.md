# Matriz de pruebas

Verificación del 27 de octubre de 2026: las cinco pruebas de `pruebas/test_logica.py` pasaron con Python 3.14.8. Cubren nombre, bloqueos, validaciones, doble respuesta, victoria, derrota, límites y reinicio. También se creó una ventana Tkinter oculta y se recorrieron programáticamente inicio, mapa, escenas, respuesta y cierre sin errores. Esto no sustituye la revisión visual ni las pruebas con usuarios.

Los resultados por caso de la tabla siguiente quedan para el registro manual detallado del estudiante; “Pendiente” se refiere a ese registro. Los resultados automatizados anteriores sí fueron obtenidos.

| Caso | Entrada o situación | Resultado esperado | Obtenido / estado |
|---|---|---|---|
| Nombre | Vacío, espacios o 25 caracteres | Rechazo sin iniciar | Pendiente |
| Nombre válido | ` Ada ` | Nombre Ada; 0 XP y 3 energía | Pendiente |
| Bloqueo | Abrir misión 2 al comenzar | Rechazo | Pendiente |
| Índice inválido | Acción 2 o nivel −1 | Rechazo sin modificar estado | Pendiente |
| Doble clic | Responder dos veces sin continuar | Una sola recompensa | Pendiente |
| Secuencia | Continuar sin responder | Rechazo | Pendiente |
| Acierto | Decisión segura | +100 XP; misma energía | Pendiente |
| Error | Riesgo con 0 XP | 0 XP; −1 energía | Pendiente |
| Límite superior | Completar misión con 3 energía | Permanece en 3 | Pendiente |
| Victoria | Resolver nueve escenas con acciones seguras | 900 XP; cuatro completadas; victoria | Pendiente |
| Derrota | Dos riesgos en nivel 1 y dos en nivel 2 | Energía 0; no continuar | Pendiente |
| Reinicio | Responder y reiniciar misión | Restaurar puntos, energía e historial iniciales | Pendiente |
| Nueva partida | Volver a jugar | Nombre solicitado y progreso vacío | Pendiente |
| Interfaz | Abrir, ayuda, examinar evidencia y completar sectores | Botones legibles y navegación coherente | Pendiente manual |
| Retroalimentación | Elegir ambas clases de acción | Explicación visible antes de continuar | Pendiente manual |
| Cierre | Cerrar y abrir aplicación | Partida nueva sin progreso persistido | Pendiente manual |

Comando: `py -m unittest discover -s pruebas -v`. Las opciones seguras son índice 0 en los datos; la interfaz mezcla su posición visual. No usar la posición del botón como criterio de aprendizaje.
