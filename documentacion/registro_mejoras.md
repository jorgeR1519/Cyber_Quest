# Registro de mejoras

## 6 de noviembre de 2026 · Migración a aventura 2D

Tras la observación del docente y la solicitud del autor, se reemplazó el cuestionario por una aventura tradicional vista desde arriba. La interfaz activa utiliza Pygame y ofrece movimiento por teclado, colisiones, patrullas, diálogos, objetos, inventario y cuatro misiones espaciales.

Se conservaron las cuatro ambientaciones y la música original. Las ayudas de selección fueron sustituidas por escáner gratuito, radio de Ada con tres llamadas e impulso para esquivar. Los objetivos se validan en el mundo y los portales dependen de su finalización. El historial de la versión anterior se conserva en historial/prototipo_cuestionario; no es la aplicación activa.

Se verificaron rutas seguras hacia todos los objetos, campaña completa, restricciones de objetos, daño y reinicio. También se comprobaron renderizado y eventos sin ventana. La matriz identifica los límites de estas pruebas. Queda pendiente evaluar con personas la claridad, dificultad y utilidad educativa. No se atribuye aprobación docente a la nueva versión sin mostrársela.

## Tres modos de dificultad

Se incorporó un selector visible con Fácil, Medio y Difícil, configuración centralizada y modo persistente durante la campaña. Se parametrizaron energía, radio, recuperación, detección, movimiento enemigo, memoria, advertencia, protección y recarga. Pasaron 19 pruebas y la verificación gráfica del selector. La guía y el refugio siguen disponibles en todos los modos.

## 9 de noviembre de 2026 · Persecución y guía durante el juego

Se sustituyó la patrulla exclusivamente horizontal por detección con visión, alerta, persecución, memoria y regreso, con velocidades progresivas y refugio protegido. Se agregaron guía inicial, siguiente paso dinámico, resaltado del destino, ruta parcial y tutorial gratuito T. La radio ahora adapta su consejo al progreso actual. Pasaron 15 pruebas unitarias y la comprobación gráfica; se verificaron también el tutorial y su pausa. La valoración humana de dificultad y comprensión sigue pendiente.
