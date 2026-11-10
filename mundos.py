"""Escenarios de aventura 2D. Cada casilla mide 32 píxeles."""
ANCHO, ALTO, CASILLA = 26, 17, 32


def obj(id, tipo, x, y, nombre, **extra):
    return dict(id=id, tipo=tipo, x=x, y=y, nombre=nombre, **extra)


MISIONES = [
 dict(titulo="El correo de las nubes", npc="Ada", tema=0,
      historia="Sombra ha infiltrado las rutas del cielo. Ayuda a Ada a proteger los mensajes de los habitantes.",
      dialogo="Ada: inspecciona con F cada paquete. E recoge o entrega. Lleva el legítimo al correo oficial y los fraudulentos a cuarentena. Solo puedes transportar uno a la vez.",
      objetivo="Inspecciona y entrega 3 mensajes en su destino seguro.",
      muros=[(12,y) for y in range(2,15) if y not in (5,11)]+[(x,8) for x in range(4,10)],
      peligros=[(15,3),(16,3),(7,11),(8,11)], enemigos=[(5,6,9),(15,10,22)],
      objetos=[obj("npc","npc",3,2,"Ada"),
       obj("correo","mensaje",7,3,"Paquete dorado",seguro=True,detalle="biblioteca@campus.example: aviso del préstamo que solicitaste. Destino: correo oficial."),
       obj("fraude1","mensaje",19,4,"Paquete violeta",seguro=False,detalle="premios@campus-regalo.example pide tu clave bajo amenaza de bloqueo. Destino: cuarentena."),
       obj("fraude2","mensaje",8,13,"Paquete azul",seguro=False,detalle="validacion-urgente.example pide un código secreto para un premio no solicitado. Destino: cuarentena."),
       obj("oficial","oficial",22,3,"Correo oficial"),obj("cuarentena","cuarentena",22,13,"Cuarentena"),
       obj("salida","salida",23,8,"Portal a la selva"),obj("fruta","botiquin",4,12,"Fruta reparadora")]),
 dict(titulo="Las llaves de la selva", npc="Leo", tema=1,
      historia="Sombra copió una vieja llave de Leo. La selva guarda los fragmentos para renovar las defensas de la ciudad.",
      dialogo="Leo: recoge tres fragmentos y usa la forja para crear una llave única. Después busca el sello de recuperación y activa el segundo factor. ¡Evita a los centinelas!",
      objetivo="Forja una llave única y activa el segundo factor.",
      muros=[(x,7) for x in range(4,22) if x not in (9,16)]+[(13,y) for y in range(9,15) if y !=12],
      peligros=[(6,9),(7,9),(18,10),(19,10)], enemigos=[(4,5,10),(16,9,23)],
      objetos=[obj("npc","npc",3,2,"Leo"),obj("f1","fragmento",7,4,"Fragmento de llave"),
       obj("f2","fragmento",18,4,"Fragmento de llave"),obj("f3","fragmento",10,13,"Fragmento de llave"),
       obj("sello","sello",4,13,"Sello de recuperación"),obj("forja","forja",21,5,"Forja de clave única"),
       obj("factor","factor",21,12,"Segundo factor"),obj("salida","salida",23,8,"Portal al atardecer"),obj("fruta","botiquin",17,14,"Fruta reparadora")]),
 dict(titulo="Estaciones al atardecer", npc="Iris", tema=2,
      historia="Tres estaciones propagan la oscuridad entre las nubes. Iris necesita que contengas el incidente y alcances el centro de soporte.",
      dialogo="Iris: desconecta las tres estaciones con E y después entrega un reporte al soporte. No borres archivos ni descargues reparaciones desconocidas. Primero contiene; después reporta.",
      objetivo="Desconecta 3 estaciones y entrega el reporte.",
      muros=[(x,8) for x in range(3,23) if x not in (7,17)]+[(14,y) for y in range(2,7) if y !=4],
      peligros=[(5,10),(6,10),(18,12),(19,12),(20,12)], enemigos=[(5,5,11),(16,7,23),(8,11,15)],
      objetos=[obj("npc","npc",3,2,"Iris"),obj("e1","estacion",8,4,"Estación norte"),
       obj("e2","estacion",19,5,"Estación este"),obj("e3","estacion",10,13,"Estación sur"),
       obj("reporte","reporte",22,13,"Centro de soporte"),obj("salida","salida",23,8,"Portal a la fortaleza"),obj("fruta","botiquin",4,14,"Fruta reparadora")]),
 dict(titulo="El corazón de Sombra", npc="Ada", tema=3,
      historia="Sombra se refugia en una fortaleza de lava. Tres habitantes siguen atrapados. Recupera los cristales y reactiva el escudo digital.",
      dialogo="Ada: cada cristal alimenta una baliza. Enciende las tres y rescata a los habitantes protegidos por ellas. Después activa el núcleo. Espacio te permite esquivar a Sombra.",
      objetivo="Enciende 3 balizas, rescata 3 habitantes y activa el núcleo.",
      muros=[(12,y) for y in range(2,15) if y not in (5,11)]+[(x,8) for x in range(15,22) if x !=18],
      peligros=[(6,8),(7,8),(16,3),(17,3),(19,11),(20,11),(9,14)], enemigos=[(4,6,10),(15,6,23),(14,12,22)],
      objetos=[obj("npc","npc",3,2,"Ada"),obj("c1","cristal",5,12,"Cristal de escudo"),
       obj("c2","cristal",18,12,"Cristal de escudo"),obj("c3","cristal",20,3,"Cristal de escudo"),
       obj("b1","baliza",8,4,"Baliza de verificación"),obj("b2","baliza",20,5,"Baliza de acceso"),obj("b3","baliza",18,13,"Baliza de reporte"),
       obj("h1","habitante",6,5,"Noa",requiere="b1"),obj("h2","habitante",17,4,"Sol",requiere="b2"),obj("h3","habitante",14,13,"Teo",requiere="b3"),
       obj("salida","salida",22,9,"Núcleo del escudo"),obj("fruta","botiquin",4,14,"Fruta reparadora")]),
]
