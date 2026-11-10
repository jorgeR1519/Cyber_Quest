"""Reglas del mundo: movimiento, colisiones, objetos y objetivos encadenados."""
import math
import pygame
from mundos import MISIONES, ANCHO, ALTO
from inteligencia import actualizar_centinela, buscar_ruta
from dificultad import MODOS


class Juego:
    ENERGIA_MAXIMA = 5

    def __init__(self, nombre, dificultad="medio"):
        self.nombre = nombre.strip()
        if not 1 <= len(self.nombre) <= 24:
            raise ValueError("Escribe un nombre de 1 a 24 caracteres.")
        if dificultad not in MODOS:
            raise ValueError("Selecciona Fácil, Medio o Difícil.")
        self.dificultad = dificultad
        self.config = MODOS[dificultad].copy()
        self.ENERGIA_MAXIMA = self.config["energia"]
        self.puntos, self.energia, self.radio, self.nivel = 0, self.ENERGIA_MAXIMA, self.config["radio"], 0
        self.completadas = []
        self.victoria = False
        self.cargar_nivel()

    @property
    def mision(self):
        return MISIONES[self.nivel]

    @property
    def derrota(self):
        return self.energia == 0

    @property
    def rect(self):
        return pygame.Rect(round(self.x),round(self.y),20,24)

    def cargar_nivel(self):
        self.x, self.y = 70.,68.
        self.hechos, self.inspeccionados = set(), set()
        self.carga = None
        self.fragmentos = self.cristales = 0
        self.sello = False
        self.invulnerable = self.impulso = self.espera_impulso = self.espera_scan = 0.
        self.objetos = [dict(o) for o in self.mision["objetos"]]
        self.muros = [(x,y) for x in range(ANCHO) for y in range(ALTO) if x in (0,ANCHO-1) or y in (0,ALTO-1)] + self.mision["muros"]
        self.enemigos = [dict(x=a*32+5.,y=b*32+5.,inicio=a*32+5.,fin=c*32+5.,direccion=1) for a,b,c in self.mision["enemigos"]]
        self._inicio = (self.puntos,self.energia,self.radio)
        self.dialogo = [self.mision["historia"],
            "DIFICULTAD: "+self.config["nombre"]+". "+self.config["descripcion"]+". La dificultad se mantiene durante toda esta partida.",
            "CÓMO JUGAR: tú eres el guardián de sombrero rojo. WASD o flechas para moverte. Acércate a "+self.mision["npc"]+" y pulsa E para hablar. E o Enter cierra cada texto; mientras lees, el mundo está detenido.",
            "TU MISIÓN: "+self.mision["objetivo"]+" El diario de la derecha explica el siguiente paso y las marcas doradas señalan una ruta. T abre la guía cuando la necesites."]
        self.eventos = []

    def avisar(self, texto, sonido="pista"):
        self.eventos.append((texto,sonido))

    def solido(self, rect):
        return any(rect.colliderect(pygame.Rect(x*32,y*32,32,32)) for x,y in self.muros)

    def mover(self, dx, dy, dt):
        largo = math.hypot(dx,dy)
        if not largo or self.derrota or self.victoria or self.dialogo:
            return
        velocidad = 165*(2.6 if self.impulso > 0 else 1)
        pasos = max(1,math.ceil(velocidad*dt/5))
        for _ in range(pasos):
            nx = self.x+dx/largo*velocidad*dt/pasos
            if not self.solido(pygame.Rect(round(nx),round(self.y),20,24)):
                self.x = nx
            ny = self.y+dy/largo*velocidad*dt/pasos
            if not self.solido(pygame.Rect(round(self.x),round(ny),20,24)):
                self.y = ny

    def avanzar(self, dt, dx=0, dy=0):
        if self.derrota or self.victoria or self.dialogo:
            return
        dt = min(max(dt,0),.05)
        for atributo in ("invulnerable","impulso","espera_impulso","espera_scan"):
            setattr(self,atributo,max(0,getattr(self,atributo)-dt))
        self.mover(dx,dy,dt)
        for e in self.enemigos:
            actualizar_centinela(self,e,dt)
            if not self.en_refugio() and self.rect.colliderect(pygame.Rect(e["x"],e["y"],23,23)):
                self.recibir_dano()
        for x,y in self.mision["peligros"]:
            if self.rect.colliderect(pygame.Rect(x*32+3,y*32+3,26,26)):
                self.recibir_dano()

    def recibir_dano(self):
        if self.invulnerable > 0 or self.derrota or self.victoria:
            return
        self.energia = max(0,self.energia-1)
        self.puntos = max(0,self.puntos-20)
        self.invulnerable = self.config["proteccion"]
        self.x,self.y = 70.,68.
        self.avisar("Sombra te alcanzó. Vuelves al refugio y conservas tus objetos.","error")

    def en_refugio(self):
        return self.rect.centerx < 5*32 and self.rect.centery < 4*32

    def guia_actual(self):
        """Acción inmediata y destino, derivados del estado real de la misión."""
        def elegir(tipos):
            candidatos = [o for o in self.objetos if o["tipo"] in tipos and o["id"] not in self.hechos]
            return min(candidatos,key=lambda o: math.dist(self.rect.center,(o["x"]*32+16,o["y"]*32+16))) if candidatos else None
        def por_id(id):
            return next(o for o in self.objetos if o["id"] == id)
        if "npc" not in self.hechos:
            return por_id("npc"),"Acércate a "+self.mision["npc"]+" y pulsa E para recibir la misión."
        if self.objetivo_completo():
            return por_id("salida"),"¡Objetivos listos! Ve al portal y pulsa E para avanzar."
        if self.nivel == 0:
            if self.carga:
                paquete = por_id(self.carga)
                if self.carga not in self.inspeccionados:
                    return None,"Llevas un paquete. Pulsa F para leer su remitente y sus señales."
                terminal = por_id("oficial" if paquete["seguro"] else "cuarentena")
                return terminal,"Lleva el paquete a "+terminal["nombre"]+" y pulsa E para entregarlo."
            paquete = elegir(("mensaje",))
            return paquete,"Busca "+paquete["nombre"]+". F lo inspecciona y E lo recoge."
        if self.nivel == 1:
            if self.fragmentos < 3:
                return elegir(("fragmento",)),f"Recoge fragmentos dorados con E: {self.fragmentos}/3."
            if "forja" not in self.hechos:
                return por_id("forja"),"Ya tienes los tres fragmentos. Ve a la forja L y pulsa E."
            if not self.sello:
                return por_id("sello"),"Busca el sello violeta de recuperación y recógelo con E."
            return por_id("factor"),"Lleva el sello al mecanismo 2 y pulsa E para activar la segunda defensa."
        if self.nivel == 2:
            estacion = elegir(("estacion",))
            if estacion:
                return estacion,"Acércate a "+estacion["nombre"]+" (!) y pulsa E para desconectarla."
            return por_id("reporte"),"Las tres estaciones están aisladas. Ve al centro R y entrega el reporte con E."
        rescatables = [o for o in self.objetos if o["tipo"] == "habitante" and o["id"] not in self.hechos and o["requiere"] in self.hechos]
        if rescatables:
            return rescatables[0],"La baliza ya protege a "+rescatables[0]["nombre"]+". Acércate y pulsa E para rescatar."
        if not self.cristales:
            return elegir(("cristal",)),"Busca un cristal turquesa y recógelo con E para alimentar una baliza."
        return elegir(("baliza",)),"Lleva un cristal a una baliza B y pulsa E. Después rescata al habitante protegido."

    def ruta_guia(self):
        objetivo,_ = self.guia_actual()
        if not objetivo:
            return []
        inicio = int(self.rect.centerx//32),int(self.rect.centery//32)
        return buscar_ruta(inicio,(objetivo["x"],objetivo["y"]),set(self.muros+self.mision["peligros"]))

    def ver_tutorial(self):
        if self.derrota or self.victoria or self.dialogo:
            return
        self.dialogo = [
            "MOVIMIENTO: tú eres el personaje con sombrero rojo. WASD o flechas te mueven. Las paredes bloquean el paso. E interactúa con lo que tengas cerca. E/Enter avanza el texto y vuelve a permitir moverte.",
            f"HERRAMIENTAS: F examina objetos y mensajes; es gratis. H llama a Ada ({self.config['radio']} usos por partida). Espacio mientras te mueves da un impulso para esquivar. La energía aparece arriba; la fruta recupera una unidad.",
            "AMENAZAS: si un centinela te ve, muestra ! y se prepara para perseguirte. Rompe su visión con paredes o usa el impulso. Los últimos niveles son más exigentes. El refugio inicial te protege.",
            "AHORA MISMO: "+self.guia_actual()[1]]

    def esquivar(self):
        if not self.dialogo and not self.derrota and not self.victoria and self.espera_impulso == 0:
            self.impulso,self.espera_impulso = .16,self.config["impulso"]
            self.invulnerable = max(self.invulnerable,.2)

    def cercano(self):
        opciones = [o for o in self.objetos if (o["id"] not in self.hechos or o["tipo"] in ("npc","salida","oficial","cuarentena")) and o["id"] != self.carga]
        opciones.sort(key=lambda o: math.dist(self.rect.center,(o["x"]*32+16,o["y"]*32+16)))
        if not opciones:
            return None
        objetivo = (opciones[0]["x"]*32+16,opciones[0]["y"]*32+16)
        if math.dist(self.rect.center,objetivo) > 51:
            return None
        if any(pygame.Rect(x*32,y*32,32,32).clipline(self.rect.center,objetivo) for x,y in self.muros):
            return None
        return opciones[0]

    def escanear(self):
        if self.dialogo or self.derrota or self.victoria or self.espera_scan:
            return
        self.espera_scan = .6
        o = next((o for o in self.objetos if o["id"] == self.carga),None) if self.carga else self.cercano()
        if o and o["tipo"] == "mensaje":
            self.inspeccionados.add(o["id"])
            self.dialogo = ["Escáner: "+o["detalle"]]
            self.avisar("Evidencia inspeccionada y guardada.")
        elif o:
            self.dialogo = ["Escáner: "+o["nombre"]+". "+self.mision["objetivo"]]
        else:
            self.avisar("Acércate a un objeto. El escáner F no consume usos.")

    def consultar_radio(self):
        if self.dialogo or self.derrota or self.victoria:
            return
        if not self.radio:
            self.avisar("No quedan llamadas. Consulta tu objetivo en el diario.")
            return
        self.radio -= 1
        self.dialogo = ["Radio de Ada: "+self.guia_actual()[1],self.progreso()]
        self.avisar("Radio activada; el mundo se pausa mientras lees.")

    def progreso(self):
        contar = lambda ids: sum(id in self.hechos for id in ids)
        if self.nivel == 0:
            return f"Mensajes entregados: {contar(('correo','fraude1','fraude2'))}/3"
        if self.nivel == 1:
            return f"Fragmentos: {self.fragmentos}/3 · Llave: {int('forja' in self.hechos)}/1 · Segundo factor: {int('factor' in self.hechos)}/1"
        if self.nivel == 2:
            return f"Estaciones: {contar(('e1','e2','e3'))}/3 · Reporte: {int('reporte' in self.hechos)}/1"
        return f"Balizas: {contar(('b1','b2','b3'))}/3 · Rescates: {contar(('h1','h2','h3'))}/3 · Cristales: {self.cristales}"

    def objetivo_completo(self):
        ids = [("correo","fraude1","fraude2"),("forja","factor"),("e1","e2","e3","reporte"),("b1","b2","b3","h1","h2","h3")][self.nivel]
        return all(id in self.hechos for id in ids)

    def interactuar(self):
        if self.dialogo:
            self.dialogo.pop(0); return
        if self.derrota or self.victoria:
            return
        o = self.cercano()
        if not o:
            self.avisar("Acércate a un personaje u objeto y pulsa E."); return
        id,tipo = o["id"],o["tipo"]
        if tipo == "npc":
            self.hechos.add("npc"); self.dialogo = [self.mision["dialogo"]]; return
        if tipo == "botiquin":
            if self.energia == self.ENERGIA_MAXIMA:
                self.avisar("Tu energía está completa. Reserva esta fruta para después."); return
            self.energia += 1; self.hechos.add(id)
            self.avisar("Fruta reparadora: +1 energía.","energia"); return
        if "npc" not in self.hechos:
            self.avisar("Habla primero con "+self.mision["npc"]+" en el refugio."); return
        if tipo == "salida":
            if not self.objetivo_completo():
                self.avisar("Portal cerrado. "+self.progreso()); return
            self.completadas.append(self.nivel); self.puntos += 200
            recuperada = min(self.config["recuperacion"],self.ENERGIA_MAXIMA-self.energia)
            self.energia += recuperada
            if self.nivel == 3:
                self.victoria = True; self.avisar("¡Escudo activo! La ciudad está a salvo.","victoria")
            else:
                self.nivel += 1; self.cargar_nivel()
                self.avisar(f"Nuevo distrito · {self.config['nombre']}. "+(f"Recuperas {recuperada} de energía." if recuperada else "Energía conservada."),"energia" if recuperada else "abrir")
            return
        if tipo == "mensaje":
            if self.carga:
                self.avisar("Entrega primero el mensaje que transportas.")
            else:
                self.carga = id; self.avisar("Mensaje recogido. F inspecciona; E entrega junto a una terminal.","abrir")
            return
        if tipo in ("oficial","cuarentena"):
            m = next((m for m in self.objetos if m["id"] == self.carga),None)
            if not m:
                self.avisar("Necesitas transportar un mensaje."); return
            if m["id"] not in self.inspeccionados:
                self.avisar("Inspecciona con F antes de entregar: verifica remitente y dominio."); return
            if m["seguro"] != (tipo == "oficial"):
                self.recibir_dano(); self.avisar("Destino inseguro. Revisa las señales y usa la otra terminal.","error"); return
            self.hechos.add(self.carga); self.carga = None
        elif tipo == "fragmento":
            self.fragmentos += 1; self.hechos.add(id)
        elif tipo == "sello":
            self.sello = True; self.hechos.add(id)
        elif tipo == "forja":
            if self.fragmentos < 3:
                self.avisar("La forja necesita los tres fragmentos."); return
            self.hechos.add(id)
        elif tipo == "factor":
            if "forja" not in self.hechos or not self.sello:
                self.avisar("Forja una llave única y recoge el sello de recuperación."); return
            self.hechos.add(id)
        elif tipo == "estacion":
            self.hechos.add(id)
        elif tipo == "reporte":
            if not all(e in self.hechos for e in ("e1","e2","e3")):
                self.avisar("Desconecta las tres estaciones antes del reporte."); return
            self.hechos.add(id)
        elif tipo == "cristal":
            self.cristales += 1; self.hechos.add(id)
        elif tipo == "baliza":
            if not self.cristales:
                self.avisar("Busca un cristal para alimentar la baliza."); return
            self.cristales -= 1; self.hechos.add(id)
        elif tipo == "habitante":
            if o["requiere"] not in self.hechos:
                self.avisar("Activa la baliza de este sector antes de rescatar."); return
            self.hechos.add(id)
        else:
            return
        premio = 100 if tipo in ("oficial","cuarentena","forja","factor","estacion","reporte","baliza","habitante") else 25
        self.puntos += premio
        mensajes = {"oficial":"Mensaje legítimo entregado por el canal oficial.","cuarentena":"Fraude aislado: nadie más seguirá ese enlace.",
                    "forja":"Llave única creada: protege cada cuenta con una distinta.","factor":"Segundo factor activo. Conserva el sello de recuperación.",
                    "estacion":"Estación desconectada. La amenaza deja de propagarse.","reporte":"Reporte entregado. Contener y comunicar van juntos.",
                    "baliza":"Baliza encendida. Ya puedes rescatar al habitante cercano.","habitante":o["nombre"]+" está a salvo."}
        self.avisar(mensajes.get(tipo,o["nombre"]+" guardado en la mochila.")+f" +{premio} XP","acierto")

    def reiniciar_mision(self):
        if not self.victoria:
            self.puntos,self.energia,self.radio = self._inicio
            self.cargar_nivel()
