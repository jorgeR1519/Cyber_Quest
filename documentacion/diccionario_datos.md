# Diccionario de datos

| Dato | Tipo | Función y límites |
|---|---|---|
| nombre | str | 1–24 caracteres después de quitar espacios exteriores |
| x, y | float | Posición del personaje en píxeles del mapa |
| rect | pygame.Rect calculado | Área de colisión de 20 × 24 píxeles |
| energia | int | 0–5; cero indica derrota |
| puntos | int | No negativo; máximo sin daño 2475 |
| nivel | int | 0–3 |
| completadas | list[int] | Distritos terminados en orden |
| hechos | set[str] | Identificadores de objetivos u objetos usados en el distrito |
| inspeccionados | set[str] | Mensajes examinados con el escáner |
| carga | str o None | Identificador del único mensaje transportado |
| fragmentos, cristales | int | Recursos recogidos; cristales se consumen en balizas |
| sello | bool | Recuperación disponible para activar segundo factor |
| radio | int | 0–3 llamadas en la partida |
| dialogo | list[str] | Textos pendientes; detienen la simulación |
| invulnerable, impulso, espera_impulso | float | Segundos restantes de protección y recarga |
| muros | list[tuple[int,int]] | Casillas no transitables |
| objetos | list[dict] | id, tipo, x, y, nombre y requisitos |
| enemigos | list[dict] | Posición, dirección y extremos de patrulla |
| eventos | list[tuple[str,str]] | Mensaje de consecuencia y efecto sonoro |
| _inicio | tuple | Puntos, energía y radio al entrar al distrito |
