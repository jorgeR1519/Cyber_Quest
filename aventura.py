"""Presentación Pygame de la aventura: dibujo pixel art, teclado y ciclo de juego."""
import math
import random
import pygame as pg
from motor import Juego
from mundos import MISIONES, ANCHO, ALTO
from temas import TEMAS, paisaje
from sonidos import Sonidos
from dificultad import MODOS

W, H = 1200, 800
ORIGEN = (24,140)
PAPEL, TINTA = "#fff5df", "#40323d"


class Agenda:
    """Adaptador de temporizadores para reutilizar la música sin Tkinter."""
    def __init__(self):
        self.tareas = {}; self.contador = 0

    def after(self, ms, funcion):
        self.contador += 1
        self.tareas[self.contador] = (pg.time.get_ticks()+ms,funcion)
        return self.contador

    def after_cancel(self, id):
        self.tareas.pop(id,None)

    def actualizar(self):
        for id,(fin,funcion) in list(self.tareas.items()):
            if pg.time.get_ticks() >= fin and id in self.tareas:
                self.tareas.pop(id); funcion()


class Aplicacion:
    def __init__(self, audio=True):
        pg.display.init(); pg.font.init()
        self.ventana = pg.display.set_mode((1200,800),pg.RESIZABLE)
        pg.display.set_caption("CyberQuest · Los guardianes del escudo")
        self.lienzo = pg.Surface((W,H))
        self.fuentes = {n:pg.font.SysFont("segoeui",n,bold=n >= 26) for n in (14,16,18,20,24,26,32,48)}
        self.reloj = pg.time.Clock()
        self.agenda = Agenda()
        self.sonidos = Sonidos(self.agenda)
        self.sonidos.activo = audio
        self.sonidos.iniciar_fondo()
        self.nombre = ""; self.juego = None; self.pantalla = "inicio"
        self.dificultad = "medio"
        self.noticia = "Explora. Ayuda. Protege. La aventura comienza contigo."
        self.noticia_hasta = 0; self.particulas = []; self.tiempo = 0
        self.direccion = "abajo"; self.andando = False
        self.salir = False; self.pausa = False; self.confirmar = False
        self.botones = []

    def texto(self, texto, x, y, tam=18, color=TINTA):
        self.lienzo.blit(self.fuentes[tam].render(str(texto),True,color),(x,y))

    def parrafo(self, texto, x, y, ancho, tam=18, color=TINTA, salto=5):
        linea = ""
        for palabra in str(texto).split():
            if self.fuentes[tam].size(linea+palabra)[0] > ancho and linea:
                self.texto(linea,x,y,tam,color); y += tam+salto; linea = ""
            linea += palabra+" "
        if linea:
            self.texto(linea,x,y,tam,color); y += tam+salto
        return y

    def panel(self, rect, color=PAPEL, borde="#c09c7a"):
        r = pg.Rect(rect)
        pg.draw.rect(self.lienzo,"#000000",r.move(0,4),border_radius=10)
        pg.draw.rect(self.lienzo,color,r,border_radius=10)
        pg.draw.rect(self.lienzo,borde,r,2,border_radius=10)

    def boton(self, texto, rect, accion, seleccionado=False):
        r = pg.Rect(rect)
        self.panel(r,"#c8e1bc" if seleccionado else "#ffd489","#3d7150" if seleccionado else "#9b6245")
        etiqueta = self.fuentes[20].render(texto,True,TINTA)
        self.lienzo.blit(etiqueta,etiqueta.get_rect(center=r.center))
        self.botones.append((r,accion))

    def iniciar(self):
        try:
            self.juego = Juego(self.nombre,self.dificultad)
        except ValueError as error:
            self.notificar(str(error),"error"); return
        self.pantalla = "juego"; self.pausa = self.confirmar = False
        self.particulas = []
        self.notificar("Sigue el sendero hasta Ada. E permite hablar e interactuar.","abrir")

    def elegir_dificultad(self, modo):
        self.dificultad = modo

    def notificar(self, texto, sonido="pista"):
        self.noticia = texto; self.noticia_hasta = self.tiempo+6
        self.sonidos.tocar(sonido)
        if sonido in ("acierto","energia","victoria","error") and self.juego:
            for _ in range(18):
                self.particulas.append([ORIGEN[0]+self.juego.x+10,ORIGEN[1]+self.juego.y+8,
                                        random.uniform(-60,60),random.uniform(-90,5),.8,
                                        "#f69780" if sonido == "error" else random.choice(["#fff0b1","#8ed5bd","#ffb56b"])])

    def personaje(self, x, y, color="#c65f45", mover=False, escala=2):
        dibujo = ["...cccc...","..cccccc..","..pppppp..","..ptpptp..","..pppppp..",
                  "...pppp...","..vvvvvv..",".pvvvvvvp.","..vvvvvv..","...v..v...","..tt..tt.."]
        paleta = {"c":color,"p":"#ffe0b0","t":"#3f3347","v":"#377f78"}
        pg.draw.ellipse(self.lienzo,"#574951",(x-2,y+20,25,8))
        saltito = round(math.sin(self.tiempo*16)*2) if mover else 0
        for fila,linea in enumerate(dibujo):
            for columna,pixel in enumerate(linea):
                if pixel in paleta:
                    pg.draw.rect(self.lienzo,paleta[pixel],(x+columna*escala,y+fila*escala+saltito,escala,escala))

    def tile(self, x, y, tipo, tema):
        px,py = ORIGEN[0]+x*32,ORIGEN[1]+y*32
        fondos = [("#b8dce5","#b2d7e0"),("#a5bb78","#9fb572"),("#e6b7ad","#dfb0a8"),("#8b6260","#835959")]
        color = fondos[tema][(x+y)%2]
        pg.draw.rect(self.lienzo,color,(px,py,32,32))
        if tipo == "pared":
            if tema == 1:
                pg.draw.rect(self.lienzo,"#74523c",(px+12,py+12,9,20))
                for dx,dy,w in ((6,2,20),(0,9,32),(5,19,24)):
                    pg.draw.rect(self.lienzo,"#3f7452",(px+dx,py+dy,w,10))
                pg.draw.rect(self.lienzo,"#77a369",(px+9,py+4,7,4))
            elif tema == 3:
                pg.draw.rect(self.lienzo,"#483d4c",(px+1,py+1,30,30))
                pg.draw.line(self.lienzo,"#756077",(px+2,py+15),(px+29,py+15),2)
                pg.draw.line(self.lienzo,"#756077",(px+14,py+2),(px+14,py+14),2)
            else:
                pg.draw.rect(self.lienzo,"#fff2e0",(px+4,py+3,24,23))
                pg.draw.rect(self.lienzo,"#fffaf0",(px,py+10,32,13))
                pg.draw.rect(self.lienzo,"#7da7b7" if tema == 0 else "#b88d9e",(px+4,py+25,24,6))
        elif tipo == "peligro":
            pg.draw.rect(self.lienzo,"#db7545" if tema == 3 else "#8a6d9e",(px+3,py+3,26,26))
            brillo = "#ffe39b" if int(self.tiempo*4)%2 else "#e9ae70"
            for i in range(3):
                pg.draw.rect(self.lienzo,brillo,(px+5+i*7,py+7+(i%2)*9,5,5))
        elif (x*7+y*3)%13 == 0:
            pg.draw.rect(self.lienzo,"#c9dfac" if tema == 1 else "#f3d4b9",(px+12,py+20,4,3))

    def dibujar_objeto(self, o):
        j = self.juego
        if o["id"] == j.carga:
            return
        completado = o["id"] in j.hechos
        if completado and o["tipo"] in ("mensaje","fragmento","sello","cristal","habitante","botiquin"):
            return
        x,y = ORIGEN[0]+o["x"]*32,ORIGEN[1]+o["y"]*32
        tipo = o["tipo"]
        if tipo in ("npc","habitante"):
            self.personaje(x+6,y+3,"#6d67a1" if tipo == "npc" else "#e0a852")
            self.texto(o["nombre"],x-2,y-18,14)
            return
        pg.draw.ellipse(self.lienzo,"#5c5354",(x+3,y+25,26,6))
        if tipo == "mensaje":
            colores = {"correo":"#ffd376","fraude1":"#c7a0e2","fraude2":"#91cfe0"}
            pg.draw.rect(self.lienzo,colores[o["id"]],(x+4,y+7,24,17))
            pg.draw.lines(self.lienzo,"#624b61",False,[(x+4,y+7),(x+16,y+17),(x+28,y+7)],2)
            if o["id"] in j.inspeccionados:
                self.texto("✓",x+20,y-6,16,"#254f45")
        elif tipo in ("fragmento","cristal","sello","botiquin"):
            color = {"fragmento":"#ffd372","cristal":"#8af1dc","sello":"#d5a4ef","botiquin":"#ef9d74"}[tipo]
            salto = math.sin(self.tiempo*3+o["x"])*2
            pg.draw.polygon(self.lienzo,color,[(x+16,y+4+salto),(x+26,y+14+salto),(x+16,y+26+salto),(x+6,y+14+salto)])
            pg.draw.rect(self.lienzo,"#fff5d8",(x+13,y+10+salto,5,6))
        elif tipo == "salida":
            listo = j.objetivo_completo()
            pg.draw.rect(self.lienzo,"#e8c684",(x+2,y-3,28,34),3)
            pg.draw.rect(self.lienzo,"#79d3bd" if listo else "#706178",(x+6,y+2,20,26))
            self.texto("↑" if listo else "×",x+10,y+1,20,"#fff5d8")
        else:
            color = "#8cc9ac" if completado else {"oficial":"#81bed2","cuarentena":"#c399d4","baliza":"#efbb65"}.get(tipo,"#d9b98e")
            pg.draw.rect(self.lienzo,"#4e4655",(x+3,y+3,26,27))
            pg.draw.rect(self.lienzo,color,(x+6,y+6,20,14))
            simbolo = {"oficial":"O","cuarentena":"Q","forja":"L","factor":"2","estacion":"!","reporte":"R","baliza":"B"}.get(tipo,"+")
            self.texto("✓" if completado else simbolo,x+11,y+3,16)
            pg.draw.rect(self.lienzo,"#ecd5aa",(x+10,y+24,12,3))

    def dibujar_mundo(self):
        j = self.juego; tema = j.nivel
        muros = set(j.muros); peligros = set(j.mision["peligros"])
        self.panel((18,134,844,556),"#4b3d4d","#e5be8c")
        for y in range(ALTO):
            for x in range(ANCHO):
                self.tile(x,y,"pared" if (x,y) in muros else "peligro" if (x,y) in peligros else "suelo",tema)
        # Solo se marcan los próximos pasos; las paredes y los peligros se rodean.
        for x,y in j.ruta_guia()[:6]:
            pg.draw.circle(self.lienzo,"#ffe59b",(ORIGEN[0]+x*32+16,ORIGEN[1]+y*32+16),3)
        objetivo,_ = j.guia_actual()
        if objetivo:
            r = pg.Rect(ORIGEN[0]+objetivo["x"]*32-2,ORIGEN[1]+objetivo["y"]*32-2,36,36)
            pg.draw.rect(self.lienzo,"#ffe59b",r,2 if int(self.tiempo*3)%2 else 3)
        pg.draw.rect(self.lienzo,"#bde9c8",(ORIGEN[0]+32,ORIGEN[1]+32,128,96),1)
        self.texto("REFUGIO",ORIGEN[0]+36,ORIGEN[1]+34,14,"#35554d")
        for o in j.objetos:
            self.dibujar_objeto(o)
        for e in j.enemigos:
            x,y = ORIGEN[0]+e["x"],ORIGEN[1]+e["y"]
            alas = 3 if int(self.tiempo*8)%2 else 0
            estado = e.get("estado","patrulla")
            pg.draw.rect(self.lienzo,"#9e4357" if estado == "persigue" else "#503b64",(x+3,y+3,18,19))
            pg.draw.rect(self.lienzo,"#705078",(x-4,y+alas,7,10))
            pg.draw.rect(self.lienzo,"#705078",(x+21,y+alas,7,10))
            pg.draw.rect(self.lienzo,"#ffcf82",(x+6,y+8,4,4)); pg.draw.rect(self.lienzo,"#ffcf82",(x+14,y+8,4,4))
            if estado in ("alerta","persigue"):
                self.texto("!",x+8,y-23,24,"#ffe69c")
            elif estado == "regreso":
                self.texto("?",x+7,y-19,18,"#ffe8cd")
        if not j.invulnerable or int(self.tiempo*12)%2:
            self.personaje(ORIGEN[0]+j.x,ORIGEN[1]+j.y,mover=self.andando)
        if j.carga:
            self.texto("✉",ORIGEN[0]+j.x,ORIGEN[1]+j.y-20,18)
        if j.espera_scan > .3:
            pg.draw.circle(self.lienzo,"#fff5b9",(ORIGEN[0]+int(j.x)+10,ORIGEN[1]+int(j.y)+12),int((.6-j.espera_scan)*160)+20,2)
        cerca = j.cercano()
        if cerca:
            self.panel((34,650,805,30),"#fff0cf")
            verbos = {"npc":"Hablar con", "mensaje":"Recoger", "fragmento":"Recoger", "cristal":"Recoger",
                      "sello":"Recoger", "botiquin":"Recuperar energía con", "oficial":"Entregar en",
                      "cuarentena":"Entregar en", "estacion":"Desconectar", "reporte":"Entregar reporte en",
                      "habitante":"Rescatar a", "salida":"Entrar en"}
            self.texto("E · "+verbos.get(cerca["tipo"],"Activar")+" "+cerca["nombre"]+"    |    F · Inspeccionar",48,653,16)

    def diario(self):
        j = self.juego
        self.panel((880,140,296,544))
        self.texto("DIARIO DEL GUARDIÁN",900,158,20)
        self.texto("SIGUIENTE PASO",900,194,16,"#8b4937")
        self.parrafo(j.guia_actual()[1],900,222,250,18)
        self.parrafo(j.progreso(),900,350,250,16)
        self.texto("Mochila: "+("mensaje" if j.carga else "vacía"),900,416,16)
        self.texto(f"Radio: {j.radio}/{j.config['radio']} · T: guía gratuita",900,440,16)
        for i,linea in enumerate(["WASD / flechas · Mover","E / Enter · Interactuar","F · Escáner gratuito","H · Ayuda por radio","Espacio · Esquivar","Esc · Pausa   M · Sonido","R · Reiniciar distrito"]):
            self.texto(linea,900,476+i*24,16)
        self.texto("Impulso listo" if j.espera_impulso == 0 else "Recargando impulso…",900,657,14,"#765c50")

    def paisaje_menu(self, nivel, rect):
        x,y,w,h = rect
        for px,py,pw,ph,color,etiqueta in paisaje(nivel):
            pg.draw.rect(self.lienzo,color,(x+px*w/900,y+py*h/144,max(1,pw*w/900),max(1,ph*h/144)))

    def dibujar(self):
        self.botones = []
        if self.pantalla == "inicio":
            self.lienzo.fill("#f7e5cf")
            self.texto("CYBERQUEST",62,45,48,"#8b4937")
            self.texto("Los guardianes del escudo",64,109,26)
            self.parrafo("Sombra está apagando los cuatro distritos. Explora sus mundos, ayuda a sus habitantes y recupera las defensas de la ciudad.",64,162,1050,24)
            for i,titulo in enumerate(("Islas del cielo","Selva de las llaves","Cielo al atardecer","Fortaleza de lava")):
                x = 60+i*278
                self.panel((x,265,260,210))
                self.paisaje_menu(i,(x+8,275,244,140))
                self.texto(f"0{i+1} · "+titulo,x+12,436,18)
            self.texto("Dificultad de la partida · elige con clic o Tab",64,480,18)
            for i,(modo,config) in enumerate(MODOS.items()):
                self.boton(config["nombre"]+(" (seleccionado)" if modo == self.dificultad else ""),(60+i*360,510,340,40),lambda m=modo:self.elegir_dificultad(m),modo == self.dificultad)
            self.texto(MODOS[self.dificultad]["descripcion"],64,558,16)
            self.texto("Nombre del guardián",64,585,18)
            self.panel((60,612,690,50),"#fff9ed")
            self.texto(self.nombre+("|" if int(self.tiempo*2)%2 == 0 else ""),78,619,26)
            self.boton("Comenzar aventura  [Enter]",(780,612,355,50),self.iniciar)
            self.parrafo("Tú controlas al guardián de sombrero rojo. Cierra los textos con E/Enter. WASD o flechas para moverte; sigue las marcas doradas y el diario. T abre la guía gratuita.",64,687,1050,18)
            self.texto(self.noticia,64,753,16,"#8b4937")
        else:
            j = self.juego; tema = TEMAS[j.nivel]
            self.lienzo.fill(tema["fondo"])
            self.panel((18,15,1158,100),tema["panel"])
            self.texto(f"0{j.nivel+1} / {j.mision['titulo']}",36,29,32)
            self.texto(f"{j.nombre}   ·   {j.config['nombre']}   ·   {j.puntos} XP   ·   Distritos: {len(j.completadas)}/4",38,76,18)
            self.texto("ENERGÍA",937,22,14)
            self.texto(f"{j.energia}/{j.ENERGIA_MAXIMA}",1100,22,14)
            for i in range(j.ENERGIA_MAXIMA):
                pg.draw.rect(self.lienzo,"#d67464" if i < j.energia else "#d5c0b0",(937+i*31,48,23,23),border_radius=5)
            self.dibujar_mundo(); self.diario()
            self.panel((18,704,1158,77),tema["panel"])
            alertas = sum(e.get("estado") in ("alerta","persigue") for e in j.enemigos)
            aviso = "¡Te han detectado! Busca cobertura, usa Espacio para esquivar o vuelve al refugio." if alertas else j.guia_actual()[1]
            self.parrafo(self.noticia if self.tiempo < self.noticia_hasta else aviso,36,721,1110,18)
            for x,y,vx,vy,vida,color in self.particulas:
                pg.draw.rect(self.lienzo,color,(x,y,5,5))
            if j.dialogo:
                self.modal("GUÍA / TRANSMISIÓN",j.dialogo[0],f"E / Enter · Continuar ({len(j.dialogo)} textos pendientes) · El mundo está en pausa")
            if self.pausa:
                self.modal("REINICIAR DISTRITO" if self.confirmar else "PAUSA",
                           "Se restaurarán los puntos, energía y llamadas al inicio de este distrito." if self.confirmar else "El mundo está detenido. Puedes descansar o reiniciar el distrito actual.",
                           "Enter · Confirmar   Esc · Cancelar" if self.confirmar else "Esc · Continuar   R · Reiniciar distrito")
            if j.victoria or j.derrota:
                self.modal("¡LA CIUDAD VUELVE A BRILLAR!" if j.victoria else "EL GUARDIÁN NECESITA DESCANSAR",
                           f"Conseguiste {j.puntos} XP y protegiste {len(j.completadas)} distritos. "+("Ada, Leo e Iris celebran contigo: el escudo digital está activo." if j.victoria else "Puedes reintentar el distrito conservando el avance anterior o comenzar otra aventura."),
                           "Enter · Nueva aventura" if j.victoria else "R · Reintentar distrito   Enter · Nueva aventura")
        self.texto("Sonido: ON" if self.sonidos.activo else "Sonido: OFF",1055,779,14)

    def modal(self, titulo, contenido, pie):
        velo = pg.Surface((W,H),pg.SRCALPHA); velo.fill((29,24,39,145)); self.lienzo.blit(velo,(0,0))
        self.panel((110,532,980,226),"#fff1d6","#b78963")
        self.texto(titulo,138,552,24,"#8b4937")
        self.parrafo(contenido,138,595,925,20)
        self.texto(pie,138,718,18,"#8b4937")

    def manejar_evento(self, evento):
        if evento.type == pg.QUIT:
            self.salir = True; return
        if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
            escala = min(self.ventana.get_width()/W,self.ventana.get_height()/H)
            ox,oy = (self.ventana.get_width()-W*escala)/2,(self.ventana.get_height()-H*escala)/2
            punto = ((evento.pos[0]-ox)/escala,(evento.pos[1]-oy)/escala)
            for rect,accion in self.botones:
                if rect.collidepoint(punto):
                    accion(); break
        if evento.type != pg.KEYDOWN:
            return
        tecla = evento.key
        if self.pantalla == "inicio":
            if tecla == pg.K_TAB:
                modos = list(MODOS)
                self.elegir_dificultad(modos[(modos.index(self.dificultad)+1)%len(modos)])
            elif tecla == pg.K_RETURN:
                self.iniciar()
            elif tecla == pg.K_BACKSPACE:
                self.nombre = self.nombre[:-1]
            elif evento.unicode.isprintable() and len(self.nombre) < 24:
                self.nombre += evento.unicode
            return
        j = self.juego
        if tecla == pg.K_m:
            self.sonidos.activo = not self.sonidos.activo; return
        if j.victoria or j.derrota:
            if tecla == pg.K_RETURN:
                self.pantalla = "inicio"; self.pausa = self.confirmar = False
            elif tecla == pg.K_r and j.derrota:
                j.reiniciar_mision()
            return
        if tecla == pg.K_ESCAPE:
            if self.confirmar:
                self.confirmar = False
            else:
                self.pausa = not self.pausa
            return
        if self.pausa:
            if tecla == pg.K_r:
                self.confirmar = True
            elif tecla == pg.K_RETURN and self.confirmar:
                j.reiniciar_mision(); self.pausa = self.confirmar = False
            return
        if tecla == pg.K_r:
            self.pausa = self.confirmar = True
        elif tecla in (pg.K_e,pg.K_RETURN):
            j.interactuar()
        elif tecla == pg.K_f:
            j.escanear()
        elif tecla == pg.K_h:
            j.consultar_radio()
        elif tecla == pg.K_t:
            j.ver_tutorial()
        elif tecla == pg.K_SPACE:
            j.esquivar()

    def actualizar(self, dt):
        self.tiempo += dt; self.agenda.actualizar()
        if self.pantalla == "juego":
            teclas = pg.key.get_pressed()
            dx = int(teclas[pg.K_d] or teclas[pg.K_RIGHT])-int(teclas[pg.K_a] or teclas[pg.K_LEFT])
            dy = int(teclas[pg.K_s] or teclas[pg.K_DOWN])-int(teclas[pg.K_w] or teclas[pg.K_UP])
            self.andando = bool(dx or dy) and not self.pausa and not self.juego.dialogo
            if not self.pausa:
                self.juego.avanzar(dt,dx,dy)
            for texto,sonido in self.juego.eventos:
                self.notificar(texto,sonido)
            self.juego.eventos.clear()
            if self.juego.derrota and not getattr(self,"derrota_sonada",False):
                self.sonidos.tocar("derrota"); self.derrota_sonada = True
            elif not self.juego.derrota:
                self.derrota_sonada = False
        for p in self.particulas:
            p[0] += p[2]*dt; p[1] += p[3]*dt; p[4] -= dt
        self.particulas = [p for p in self.particulas if p[4] > 0]

    def presentar(self):
        escala = min(self.ventana.get_width()/W,self.ventana.get_height()/H)
        tam = (max(1,round(W*escala)),max(1,round(H*escala)))
        self.ventana.fill("#292333")
        self.ventana.blit(pg.transform.scale(self.lienzo,tam),((self.ventana.get_width()-tam[0])//2,(self.ventana.get_height()-tam[1])//2))
        pg.display.flip()

    def ejecutar(self):
        try:
            while not self.salir:
                dt = min(self.reloj.tick(60)/1000,.05)
                for evento in pg.event.get():
                    self.manejar_evento(evento)
                self.actualizar(dt); self.dibujar(); self.presentar()
        finally:
            self.cerrar()

    def cerrar(self):
        self.sonidos.cerrar(); pg.quit()
