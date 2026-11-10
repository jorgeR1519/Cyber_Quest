# Pensamiento computacional · Aventura 2D

| Componente | Evidencia en el juego |
|---|---|
| Descomposición | Mundos y datos, reglas, dibujo, audio, pruebas y documentación |
| Patrones | Los objetos comparten id, tipo y coordenadas; las misiones comparten refugio, objetivo y portal |
| Abstracción | La seguridad digital se representa con paquetes, llaves, balizas y conexiones; no se realizan ataques reales |
| Algoritmos | Colisiones por eje, validación de interacciones, secuencias de objetivos, avance y reinicio |

Variables: posición, energía, XP, nivel y radio. Listas: objetos y centinelas. Diccionarios: mapas y tipos de objetos. Conjuntos: objetivos terminados e inspecciones. Condicionales: requisitos de mecanismos y finales. Ciclos anidados: casillas del mapa y píxeles del personaje. Funciones/métodos: mover, escanear, interactuar, recibir_dano y cargar_nivel.

La prueba de accesibilidad usa una búsqueda en anchura sobre casillas transitables. Es una herramienta de validación de mapas y no una función artificial dentro del producto. Cada estructura responde a un problema concreto del mundo 2D.
