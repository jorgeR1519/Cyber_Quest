# Diccionario de datos

| Dato | Tipo | Rango / función |
|---|---|---|
| nombre | str | 1–24 caracteres tras strip |
| puntos | int | 0–900 en una partida con el contenido actual |
| energia | int | 0–3; cero indica derrota |
| completadas | list[int] | Índices consecutivos de misiones completadas |
| nivel | int o None | 0–3 si hay misión activa |
| paso | int | Índice de la escena activa; vuelve a 0 al completar |
| pendiente | bool | True después de decidir y antes de continuar |
| historial | list[dict] | Nivel, paso, resultado seguro y explicación por decisión |
| _inicio | tuple o None | Puntos, energía y longitud del historial al iniciar misión |
| MISIONES | list[dict] | Cuatro niveles con título, zona, objetivo y escenas |
| opciones | list[dict] | Texto, segura (bool), explicación |
| victoria / derrota | propiedades bool | Calculadas a partir del progreso y energía |

No se almacenan contraseñas reales ni información de cuentas. Todo el estado es temporal.
