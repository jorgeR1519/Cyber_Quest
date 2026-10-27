# Pensamiento computacional

| Componente | Aplicación concreta |
|---|---|
| Descomposición | Separar contenido, reglas, interfaz y pruebas en módulos |
| Patrones | Todas las escenas comparten incidente, evidencia, acciones y explicación |
| Abstracción | Representar una amenaza mediante datos ficticios y una decisión, omitiendo redes y ataques reales |
| Algoritmos | Validar acción, aplicar consecuencia, comprobar energía y desbloquear el siguiente sector |

## Conceptos de programación

- Variables y tipos: nombre (texto), puntos y energía (enteros), pendiente (booleano).
- Secuencia: validar, actualizar, registrar y mostrar consecuencias.
- Condicionales: respuesta segura, acceso bloqueado, victoria y derrota.
- Ciclos: crear botones por misión y recorrer el historial.
- Ciclos anidados pertinentes: dibujar edificios y sus ventanas en `ciudad`.
- Listas y diccionarios: misiones, escenas, opciones e historial.
- Métodos: `decidir`, `continuar` y `reiniciar_mision` encapsulan reglas reutilizables.
- Validaciones y excepciones: impedir nombres vacíos, índices inválidos y decisiones duplicadas.
- Eventos gráficos: botones invocan métodos; `mainloop` procesa la interacción.

Para defender el proyecto, sigue una decisión desde el botón en `interfaz.py` hasta `Juego.decidir`, explica la actualización de recursos y termina en `continuar`. Compara después una decisión segura con una riesgosa.
