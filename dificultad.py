"""Parámetros de campaña centralizados; el modo se elige antes de comenzar."""
MODOS = {
    "facil": dict(nombre="Fácil", energia=7, radio=5, recuperacion=2, velocidad=.75,
                  vision=.8, aviso=.9, memoria=1.4, proteccion=2., impulso=.9,
                  descripcion="7 energías · 5 llamadas · enemigos más lentos · recuperas hasta 2 energías por distrito"),
    "medio": dict(nombre="Medio", energia=5, radio=3, recuperacion=1, velocidad=1.,
                  vision=1., aviso=.55, memoria=2.2, proteccion=1.5, impulso=1.2,
                  descripcion="5 energías · 3 llamadas · persecución equilibrada · recuperas hasta 1 energía por distrito"),
    "dificil": dict(nombre="Difícil", energia=3, radio=1, recuperacion=0, velocidad=1.18,
                    vision=1.15, aviso=.35, memoria=3.2, proteccion=1., impulso=1.6,
                    descripcion="3 energías · 1 llamada · enemigos más rápidos · sin recuperación al completar un distrito"),
}
