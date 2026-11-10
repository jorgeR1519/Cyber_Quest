"""Mockups SVG vectoriales de los mapas y diálogos de la aventura."""
from html import escape
from textwrap import wrap
from mundos import MISIONES, ANCHO, ALTO
from temas import TEMAS, paisaje
from motor import Juego


def mockup(tipo, nivel=0):
    m = MISIONES[nivel]; tema = TEMAS[nivel]; p = []
    def rect(x,y,w,h,color,borde=None):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"'+(f' stroke="{borde}" stroke-width="2"' if borde else '')+'/>')
    def text(x,y,t,tam=18,color="#40323d"):
        p.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{tam}" fill="{color}">{escape(t)}</text>')
    def parrafo(x,y,t,ancho=34,tam=18):
        for linea in wrap(t,ancho):
            text(x,y,linea,tam); y += tam+7
        return y
    def persona(x,y,color="#c65f45"):
        dibujo = ["...cccc...","..cccccc..","..pppppp..","..ptpptp..","..pppppp..","...pppp...","..vvvvvv..",".pvvvvvvp.","..vvvvvv..","...v..v...","..tt..tt.."]
        colores = dict(c=color,p="#ffe0b0",t="#3f3347",v="#377f78")
        for fila,linea in enumerate(dibujo):
            for columna,pixel in enumerate(linea):
                if pixel in colores: rect(x+columna*2,y+fila*2,2,2,colores[pixel])
    rect(0,0,1200,800,tema["fondo"])
    if tipo == "menu":
        rect(0,0,1200,800,"#f7e5cf")
        text(60,90,"CYBERQUEST",48,"#8b4937")
        text(62,140,"Los guardianes del escudo",28)
        parrafo(62,190,"Sombra está apagando los cuatro distritos. Explora, ayuda a los habitantes y recupera las defensas de la ciudad.",95,22)
        for i in range(4):
            x = 60+i*278
            rect(x,265,260,210,"#fff5df","#c09c7a")
            for px,py,pw,ph,color,etiqueta in paisaje(i):
                rect(x+8+px*244/900,275+py*140/144,max(1,pw*244/900),max(1,ph*140/144),color)
            text(x+12,450,("Islas del cielo","Selva de las llaves","Atardecer","Fortaleza de lava")[i],18)
        text(62,497,"Dificultad de la partida · elige con clic o Tab",18)
        for i,nombre in enumerate(("Fácil","Medio","Difícil")):
            rect(60+i*360,510,340,40,"#c8e1bc" if i == 1 else "#ffd489","#3d7150" if i == 1 else "#9b6245")
            text(135+i*360,537,nombre+(" (seleccionado)" if i == 1 else ""),20)
        text(62,574,"Medio: 5 energías · 3 llamadas · recuperación de 1 por distrito",16)
        text(62,602,"Nombre del guardián",18)
        rect(60,612,690,50,"#fff9ed","#c09c7a"); text(78,647,"Guardián",26)
        rect(780,612,355,50,"#ffd489","#9b6245"); text(803,647,"Comenzar aventura [Enter]",21)
        parrafo(62,710,"WASD / flechas: mover · E: interactuar · F: inspeccionar · H: radio · Espacio: esquivar · T: guía gratuita",90,20)
    else:
        rect(18,15,1158,100,tema["panel"],"#c09c7a")
        text(36,64,f"0{nivel+1} / {m['titulo']}",32)
        text(38,98,"Guardián · Medio · 0 XP · Distritos protegidos: 0/4",18)
        text(937,39,"ENERGÍA",14)
        for i in range(5): rect(937+i*40,44,28,28,"#d67464")
        muros = {(x,y) for x in range(ANCHO) for y in range(ALTO) if x in (0,ANCHO-1) or y in (0,ALTO-1)} | set(m["muros"])
        for y in range(ALTO):
            for x in range(ANCHO):
                px,py = 24+x*32,140+y*32
                fondos = [("#b8dce5","#b2d7e0"),("#a5bb78","#9fb572"),("#e6b7ad","#dfb0a8"),("#8b6260","#835959")]
                rect(px,py,32,32,fondos[nivel][(x+y)%2])
                if (x,y) in muros:
                    if nivel == 1:
                        rect(px+12,py+12,9,20,"#74523c"); rect(px,py+9,32,14,"#3f7452"); rect(px+6,py+2,20,10,"#77a369")
                    elif nivel == 3:
                        rect(px+1,py+1,30,30,"#483d4c"); rect(px+2,py+15,27,2,"#756077")
                    else:
                        rect(px+4,py+3,24,23,"#fff2e0"); rect(px,py+10,32,13,"#fffaf0"); rect(px+4,py+25,24,6,"#7da7b7" if nivel == 0 else "#b88d9e")
                elif (x,y) in m["peligros"]:
                    rect(px+3,py+3,26,26,"#db7545" if nivel == 3 else "#8a6d9e")
                    rect(px+10,py+10,7,7,"#ffe39b")
        for o in m["objetos"]:
            x,y = 24+o["x"]*32,140+o["y"]*32; t = o["tipo"]
            if t in ("npc","habitante"):
                persona(x+6,y+3,"#6d67a1" if t == "npc" else "#e0a852")
                text(x-2,y-3,o["nombre"],14)
            elif t == "mensaje":
                rect(x+4,y+7,24,17,{"correo":"#ffd376","fraude1":"#c7a0e2","fraude2":"#91cfe0"}[o["id"]])
                text(x+8,y+21,"✉",16)
            elif t in ("fragmento","cristal","sello","botiquin"):
                color = {"fragmento":"#ffd372","cristal":"#8af1dc","sello":"#d5a4ef","botiquin":"#ef9d74"}[t]
                p.append(f'<path d="M{x+16} {y+4} L{x+26} {y+14} L{x+16} {y+26} L{x+6} {y+14} Z" fill="{color}"/>')
            else:
                rect(x+3,y+3,26,27,"#4e4655")
                rect(x+6,y+6,20,14,"#d9b98e")
                text(x+10,y+20,{"salida":"×","oficial":"O","cuarentena":"Q","forja":"L","factor":"2","estacion":"!","reporte":"R","baliza":"B"}.get(t,"+"),16)
        persona(94,211)
        for a,b,c in m["enemigos"]:
            x,y = 24+a*32+5,140+b*32+5
            rect(x+3,y+3,18,19,"#503b64"); rect(x-4,y,7,10,"#705078"); rect(x+21,y,7,10,"#705078")
            rect(x+6,y+8,4,4,"#ffcf82"); rect(x+14,y+8,4,4,"#ffcf82")
        rect(880,140,296,544,"#fff5df","#c09c7a")
        text(900,185,"DIARIO DEL GUARDIÁN",20)
        text(900,210,"SIGUIENTE PASO",16)
        parrafo(900,242,"Acércate a "+m["npc"]+" y pulsa E para recibir la misión.",26,18)
        text(900,416,"Mochila: vacía",16); text(900,456,"Radio: 3/3 · T: guía gratuita",16)
        j = Juego("Guardián"); j.nivel = nivel; j.cargar_nivel()
        for x,y in j.ruta_guia()[:6]:
            p.append(f'<circle cx="{24+x*32+16}" cy="{140+y*32+16}" r="3" fill="#ffe59b"/>')
        o = j.guia_actual()[0]
        p.append(f'<rect x="{24+o["x"]*32-2}" y="{140+o["y"]*32-2}" width="36" height="36" fill="none" stroke="#ffe59b" stroke-width="3"/>')
        p.append('<rect x="56" y="172" width="128" height="96" fill="none" stroke="#bde9c8"/>')
        text(60,187,"REFUGIO",14,"#35554d")
        for i,linea in enumerate(["WASD / flechas · Mover","E / Enter · Interactuar","F · Escáner gratuito","H · Ayuda por radio","Espacio · Esquivar","Esc · Pausa   M · Audio","R · Reiniciar distrito"]):
            text(900,492+i*25,linea,16)
        rect(18,704,1158,77,tema["panel"],"#c09c7a")
        parrafo(36,736,m["objetivo"],105,18)
        if tipo in ("retroalimentacion","dialogo"):
            p.append('<rect width="1200" height="800" fill="#211a2a" opacity="0.55"/>')
            rect(110,532,980,226,"#fff1d6","#b78963")
            text(138,583,"TRANSMISIÓN",24,"#8b4937")
            parrafo(138,620,m["dialogo"],92,20)
            text(138,744,"E / Enter · Continuar",18,"#8b4937")
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-label="Mockup de aventura 2D">'+''.join(p)+'</svg>'
