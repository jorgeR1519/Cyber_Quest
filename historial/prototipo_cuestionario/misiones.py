"""Contenido ficticio de las misiones. No se usan enlaces ni cuentas reales."""


def escena(texto, pista, segura, riesgosa, explicacion):
    return {"texto": texto, "pista": pista, "opciones": [
        {"texto": segura, "segura": True, "explicacion": explicacion},
        {"texto": riesgosa, "segura": False, "explicacion": explicacion},
    ]}


MISIONES = [
    {"titulo": "La alerta sospechosa", "zona": "Centro de comunicaciones",
     "objetivo": "Protege a Ada de un mensaje que intenta robar su cuenta.",
     "escenas": [
         escena("Ada recibe: '¡Tu cuenta será bloqueada en 10 minutos! Entra y confirma tu clave'.",
                "El remitente es soporte@banco-premios.example. El enlace dice banco-validacion.example.",
                "Abrir la aplicación oficial por mi cuenta para verificar", "Abrir el enlace del mensaje",
                "La urgencia y un dominio extraño son señales de alerta. Verifica por un canal oficial independiente."),
         escena("Ada confirma por la aplicación oficial que su cuenta está bien. El mensaje sigue en la bandeja.",
                "El mensaje pide la contraseña y un código de verificación.",
                "Reportar el mensaje como phishing y eliminarlo", "Responder con el código para aclararlo",
                "Reportar ayuda a proteger a otras personas. Nunca compartas contraseñas ni códigos de acceso."),
     ]},
    {"titulo": "El acceso protegido", "zona": "Torre de identidad",
     "objetivo": "Ayuda a Leo a reforzar la protección de su cuenta.",
     "escenas": [
         escena("Leo reutiliza la misma clave en el correo y en un juego. El juego sufrió una filtración.",
                "Si dos servicios comparten clave, una filtración puede afectar ambos.",
                "Cambiarla por una contraseña larga y única, guardada en un gestor", "Añadir un 1 a la clave reutilizada",
                "Una contraseña larga y única reduce el riesgo de reutilización. Un gestor permite conservar claves distintas."),
         escena("La torre permite habilitar una segunda comprobación de acceso.",
                "Una contraseña puede ser robada aunque sea larga.",
                "Activar autenticación multifactor y guardar los códigos de recuperación", "Mantener solo la contraseña",
                "La autenticación multifactor añade protección. Guarda los códigos de recuperación en un lugar seguro."),
     ]},
    {"titulo": "La red comprometida", "zona": "Estación de trabajo",
     "objetivo": "Contén una alerta sin agravar el incidente.",
     "escenas": [
         escena("En la estación aparece una ventana desconocida: 'Equipo infectado. Instala este limpiador'.",
                "La alerta aparece dentro de una página y pide descargar un archivo.",
                "Evitar la descarga y avisar al soporte autorizado", "Instalar el limpiador anunciado",
                "Una alerta falsa puede inducir a instalar software dañino. Usa los canales de soporte establecidos."),
         escena("La estación empieza a enviar mensajes extraños. El protocolo del centro indica desconectar la red y avisar.",
                "El soporte necesita saber qué ocurrió y cuándo, sin recibir datos sensibles.",
                "Seguir el protocolo, desconectar la red y reportar los síntomas", "Borrar archivos al azar y ocultar lo ocurrido",
                "Seguir el protocolo y reportar permite contener y analizar el incidente. No borres posibles evidencias."),
     ]},
    {"titulo": "Operación Escudo Digital", "zona": "Núcleo de la ciudad",
     "objetivo": "Aplica lo aprendido para mantener los servicios de la ciudad.",
     "escenas": [
         escena("Durante una emergencia, un supuesto administrador pide tu código de acceso por chat.",
                "El avatar es conocido, pero la petición exige entregar un secreto.",
                "Rechazar la petición y verificar por el canal oficial", "Enviar el código porque parece urgente",
                "Una identidad visible puede ser suplantada. Los códigos de acceso son secretos."),
         escena("Debes preparar una cuenta de respaldo para el centro de control.",
                "Cada cuenta debe tener sus propias medidas de protección.",
                "Usar una clave única y activar multifactor", "Copiar la clave compartida del equipo",
                "Las claves únicas y multifactor reducen el impacto de una credencial comprometida."),
         escena("El núcleo detecta actividad inusual al mismo tiempo que llega otro enlace de reparación.",
                "El protocolo dispone reportar al equipo responsable y evitar herramientas desconocidas.",
                "Reportar por el canal autorizado y seguir el protocolo", "Ejecutar la reparación del enlace",
                "Coordinar la respuesta y evitar software desconocido protege los servicios durante un incidente."),
     ]},
]

# Cada incidente ofrece cuatro acciones: una segura y tres alternativas plausibles.
# Las dos primeras conservan sus índices para facilitar la lectura de las reglas.
ALTERNATIVAS = [
    ("Buscar el mismo enlace en los comentarios del mensaje", "Confiar porque el mensaje incluye el logotipo del banco"),
    ("Reenviar el mensaje al grupo para que otros prueben el enlace", "Conservarlo y abrirlo más tarde si vuelve a llegar"),
    ("Cambiar solo la clave del juego y mantener la misma en el correo", "Usar una clave larga igual en todos los servicios"),
    ("Compartir los códigos de recuperación por el chat del equipo", "Activar multifactor y aprobar cualquier solicitud que llegue"),
    ("Pedir a un compañero que descargue el limpiador para comprobarlo", "Introducir los datos de la cuenta en la ventana para verificar la alerta"),
    ("Desconectar la red pero no reportar hasta que alguien lo note", "Reenviar todos los archivos al correo personal para investigarlos"),
    ("Pedir una foto de su identificación y enviarle después el código", "Enviar solo una parte del código para comprobar si es administrador"),
    ("Crear una clave única y compartirla para facilitar la emergencia", "Activar multifactor pero conservar la clave reutilizada del equipo"),
    ("Aplicar primero la reparación y reportar únicamente si falla", "Esperar sin reportar porque otras personas podrían resolverlo"),
]
CONSEJOS = [
    "Compara el dominio real con el canal que utilizas habitualmente. Un logotipo no demuestra quién envía el mensaje.",
    "Piensa qué acción reduce también el riesgo para otras personas sin difundir el contenido fraudulento.",
    "Una filtración en un servicio puede afectar a otro si comparten la misma credencial.",
    "La segunda comprobación ayuda si también proteges sus códigos y revisas qué solicitudes apruebas.",
    "Pedir a otra persona que pruebe una descarga sospechosa traslada el riesgo; no lo resuelve.",
    "Contener el incidente y avisar son pasos complementarios. Evita mover información a servicios personales.",
    "Una foto o un avatar no justifican entregar un secreto de acceso, ni completo ni por partes.",
    "Combina medidas: una clave reutilizada o compartida sigue siendo un punto débil aunque actives otra protección.",
    "Durante un incidente importa tanto evitar nuevas acciones riesgosas como coordinar la respuesta por un canal autorizado.",
]
indice = 0
for nivel, mision in enumerate(MISIONES):
    mision["dificultad"] = ("Aprendiz", "Explorador", "Especialista", "Guardián experto")[nivel]
    for situacion in mision["escenas"]:
        for alternativa in ALTERNATIVAS[indice]:
            situacion["opciones"].append({"texto": alternativa, "segura": False,
                                         "explicacion": situacion["opciones"][0]["explicacion"]})
        situacion["consejo"] = CONSEJOS[indice]
        indice += 1
