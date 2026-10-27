"""Pantallas y dibujos propios, sin recursos ni dependencias externas."""
import random
import tkinter as tk
from tkinter import messagebox

from logica_juego import Juego
from misiones import MISIONES
from sonidos import Sonidos

FONDO = "#fff7eb"
PANEL = "#ffe4c4"
TEXTO = "#493226"
ACENTO = "#a64222"
ERROR = "#ac2941"


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CyberQuest · Defensa Digital")
        self.geometry("1080x880")
        self.minsize(850, 720)
        self.configure(bg=FONDO)
        self.juego = None
        self.sonidos = Sonidos()
        self.tareas = set()
        self.generacion = 0
        self.efecto_id = 0
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        barra = tk.Frame(self, bg=PANEL)
        barra.pack(fill="x")
        tk.Label(barra, text="✦ CYBERQUEST  ·  Una aventura para cuidar tu mundo digital", bg=PANEL,
                 fg=ACENTO, font=("Segoe UI", 11, "bold")).pack(side="left", padx=18, pady=10)
        self.audio = tk.Button(barra, text="SONIDO: ON", command=self.alternar_sonido,
                               bg=PANEL, fg=ACENTO, relief="flat", font=("Segoe UI", 10))
        self.audio.pack(side="right", padx=16)
        # Contenido desplazable para que los controles no se corten en pantallas pequeñas.
        zona = tk.Frame(self, bg=FONDO)
        zona.pack(fill="both", expand=True)
        self.scroll = tk.Canvas(zona, bg=FONDO, highlightthickness=0)
        desplazamiento = tk.Scrollbar(zona, command=self.scroll.yview)
        desplazamiento.pack(side="right", fill="y")
        self.scroll.pack(side="left", fill="both", expand=True)
        self.scroll.config(yscrollcommand=desplazamiento.set)
        self.contenido = tk.Frame(self.scroll, bg=FONDO, padx=30, pady=14)
        ventana = self.scroll.create_window(0, 0, window=self.contenido, anchor="nw")
        self.contenido.bind("<Configure>", lambda e: self.scroll.config(scrollregion=self.scroll.bbox("all")))
        self.scroll.bind("<Configure>", lambda e: self.scroll.itemconfigure(ventana, width=e.width))
        self.bind("<MouseWheel>", lambda e: self.scroll.yview_scroll(int(-e.delta / 120), "units"))
        self.inicio()

    def despues(self, demora, funcion):
        """Registra animaciones para cancelarlas al cambiar de pantalla."""
        generacion = self.generacion
        def ejecutar():
            self.tareas.discard(tarea)
            if generacion == self.generacion:
                funcion()
        tarea = self.after(demora, ejecutar)
        self.tareas.add(tarea)

    def alternar_sonido(self):
        self.sonidos.activo = not self.sonidos.activo
        self.audio.config(text="SONIDO: ON" if self.sonidos.activo else "SONIDO: OFF")
        if not self.sonidos.activo:
            from sonidos import winsound
            if winsound:
                winsound.PlaySound(None, 0)

    def destroy(self):
        for tarea in self.tareas:
            self.after_cancel(tarea)
        self.tareas.clear()
        self.sonidos.cerrar()
        super().destroy()

    def efecto(self, mensaje, color=ACENTO, sonido=None):
        """Pulso y confeti de píxeles, sin bloquear los botones."""
        if sonido:
            self.sonidos.tocar(sonido)
        self.efecto_id += 1
        actual = self.efecto_id
        self.monitor.delete("efecto")
        ancho = max(700, self.monitor.winfo_width())
        texto = self.monitor.create_text(ancho/2, 37, text=mensaje, fill=color,
                                         font=("Segoe UI", 14, "bold"), tags="efecto")
        particulas = []
        for _ in range(18):
            x = ancho/2 + random.randint(-90, 90)
            item = self.monitor.create_rectangle(x, 52, x+6, 58,
                       fill=random.choice([color, "#f5a623", "#d35274", "#398578"]), outline="", tags="efecto")
            particulas.append((item, random.uniform(-6, 6), random.uniform(-2, 3)))
        def cuadro(paso=0):
            if actual != self.efecto_id or not self.monitor.winfo_exists():
                return
            for item, dx, dy in particulas:
                self.monitor.move(item, dx, dy)
            self.monitor.itemconfigure(texto, fill=color if paso % 8 < 6 else TEXTO)
            if paso < 30:
                self.despues(30, lambda: cuadro(paso+1))
            else:
                self.monitor.delete("efecto")
        cuadro()

    def consola(self):
        self.monitor = tk.Canvas(self.contenido, height=78, bg=PANEL,
                                 highlightthickness=1, highlightbackground="#edc59c")
        self.monitor.pack(fill="x", pady=8)
        self.monitor.create_text(15, 16, text="✦ Tu aventura, paso a paso", anchor="w",
                                 fill="#805334", font=("Segoe UI", 10))
        barrido = self.monitor.create_rectangle(0, 71, 100, 75, fill="#e99c41", outline="")
        def animar(paso=0):
            ancho = max(700, self.monitor.winfo_width())
            x = (paso * 12) % ancho
            self.monitor.coords(barrido, x, 71, min(x+100, ancho), 75)
            self.despues(65, lambda: animar(paso+1))
        animar()

    def texto(self, contenido, tam=13, color=TEXTO):
        etiqueta = tk.Label(self.contenido, text=contenido, bg=FONDO, fg=color,
                            font=("Segoe UI", tam), wraplength=780, justify="left")
        etiqueta.pack(anchor="w", pady=7)
        return etiqueta

    def boton(self, texto, comando, activo=True):
        boton = tk.Button(self.contenido, text=texto, command=comando,
                          bg=PANEL, fg=TEXTO, activebackground="#f7bc75",
                          activeforeground=TEXTO, font=("Segoe UI", 12),
                          cursor="hand2", disabledforeground="#836e5e",
                          relief="raised", borderwidth=2, padx=16, pady=9, wraplength=760,
                          anchor="w", state="normal" if activo else "disabled")
        boton.pack(fill="x", pady=4)
        boton.bind("<Enter>", lambda e: boton.config(bg="#ffd29a") if boton["state"] == "normal" else None)
        boton.bind("<Leave>", lambda e: boton.config(bg=PANEL))
        return boton

    def limpiar(self, titulo):
        self.generacion += 1
        for tarea in self.tareas:
            self.after_cancel(tarea)
        self.tareas.clear()
        for widget in self.contenido.winfo_children():
            widget.destroy()
        self.scroll.yview_moveto(0)
        self.texto("CYBERQUEST / DEFENSA DIGITAL", 12, ACENTO)
        self.texto(titulo, 25)
        if self.juego:
            self.estado = self.texto(f"Guardián: {self.juego.nombre}    |    XP: {self.juego.puntos}    |    "
                       f"Energía: {self.juego.energia}/3    |    Misiones: {len(self.juego.completadas)}/4", 11, ACENTO)
            self.vidas = self.texto("ENERGÍA  " + "◆ " * self.juego.energia + "◇ " * (3-self.juego.energia), 16, ACENTO)
        self.consola()
        self.efecto("¡Tu próxima aventura te espera!")

    def pixel_art(self, lienzo, dibujo, x, y, escala=4, etiqueta="personaje"):
        """Sprites propios: cada carácter de la matriz representa un píxel."""
        colores = {"c": "#b64839", "o": "#ffbf69", "p": "#ffe1a3",
                   "t": "#493226", "v": "#398578", "b": "#fffaf0"}
        for fila, linea in enumerate(dibujo):
            for columna, pixel in enumerate(linea):
                if pixel in colores:
                    px, py = x + columna*escala, y + fila*escala
                    lienzo.create_rectangle(px, py, px+escala, py+escala,
                                            fill=colores[pixel], outline="", tags=etiqueta)

    def ciudad(self):
        lienzo = tk.Canvas(self.contenido, height=160, bg="#ffe7c5", highlightthickness=0)
        lienzo.pack(fill="x", pady=10)
        lienzo.create_rectangle(0, 130, 1800, 160, fill="#e3b77b", outline="")
        lienzo.create_rectangle(0, 130, 1800, 136, fill="#8aa66c", outline="")
        # Sol escalonado y nubes hechas de bloques, sin imágenes externas.
        for x, y, w, h in ((62, 15, 30, 42), (56, 21, 42, 30)):
            lienzo.create_rectangle(x, y, x+w, y+h, fill="#f3ac36", outline="")
        for x in (170, 430, 710):
            for dx, dy, w, h in ((0, 12, 70, 12), (12, 0, 40, 24)):
                lienzo.create_rectangle(x+dx, 16+dy, x+dx+w, 16+dy+h,
                                       fill="#fffaf0", outline="", tags="nubes")
        # Ciclos anidados: edificios y ventanas de la ciudad que protegemos.
        for columna in range(12):
            x = 180 + columna * 64
            alto = 36 + (columna % 4) * 12
            lienzo.create_rectangle(x, 130-alto, x+44, 130,
                                   fill=("#e89b69", "#dfb563", "#d78d85", "#96b4a1")[columna % 4], outline="")
            lienzo.create_rectangle(x-4, 126-alto, x+48, 132-alto, fill="#ad6651", outline="")
            for fila in range(alto // 18):
                lienzo.create_rectangle(x+9, 118-fila*18, x+17, 124-fila*18, fill="#fff2bd", outline="")
        self.pixel_art(lienzo, ["..cccc..", ".cccccc.", "..pppp..", "..ptpt..",
                               "..pppp..", ".vvvvvv.", "pvovvovp", "..vvvv..",
                               "..v..v..", ".tt..tt."], 75, 80, 5)
        self.pixel_art(lienzo, [".oo.oo.", "ooooooo", "ooooooo", ".ooooo.",
                               "..ooo..", "...o..."], 125, 70, 3, "corazon")
        def escanear(paso=0):
            # Pequeño salto del guardián y balanceo del corazón pixelado.
            desplazamiento = -1 if paso % 24 < 12 else 1
            lienzo.move("personaje", 0, desplazamiento)
            lienzo.move("corazon", 0, -desplazamiento)
            lienzo.move("nubes", .2 if paso % 240 < 120 else -.2, 0)
            self.despues(90, lambda: escanear(paso+1))
        escanear()

    def inicio(self):
        self.juego = None
        self.limpiar("Una ciudad. Cuatro misiones. Tu defensa.")
        self.ciudad()
        self.texto("Conviértete en guardián digital. Ayuda a Ada y Leo a proteger la ciudad de engaños y amenazas.")
        self.texto("Nombre del guardián (máximo 24 caracteres)")
        self.nombre = tk.Entry(self.contenido, font=("Segoe UI", 16), bg=PANEL, fg=TEXTO,
                               insertbackground=ACENTO, relief="flat")
        self.nombre.pack(fill="x", pady=12, ipady=8)
        self.nombre.focus_set()
        self.boton("Comenzar aventura", self.comenzar)
        self.texto("Decisión segura: +100 XP. Riesgo: −50 XP y −1 energía. Cada misión completada recupera 1 energía. Con 0, termina la partida.", 11)
        self.texto("Simulación educativa: no escribas contraseñas ni datos reales.", 11, ACENTO)

    def comenzar(self):
        try:
            self.juego = Juego(self.nombre.get())
        except ValueError as error:
            messagebox.showerror("Revisa el nombre", str(error))
            return
        self.mapa()
        self.efecto("¡Bienvenido! Vamos a proteger la ciudad", sonido="abrir")

    def mapa(self):
        self.limpiar("Centro de mando / Mapa de misiones")
        self.ciudad()
        self.texto("Completa las misiones en orden para activar el escudo de la ciudad.")
        for i, mision in enumerate(MISIONES):
            estado = "COMPLETADA" if i in self.juego.completadas else "DISPONIBLE" if i == len(self.juego.completadas) else "BLOQUEADA"
            self.boton(f"0{i+1}  {mision['titulo']} · {mision['zona']}  [{estado}]",
                       lambda nivel=i: self.abrir(nivel), estado == "DISPONIBLE")
        self.boton("Cómo jugar", self.ayuda)
        self.boton("Nueva partida", self.nueva)

    def ayuda(self):
        messagebox.showinfo("Cómo jugar", "Abre la misión disponible. Examina las evidencias antes de actuar.\n\n"
                            "Cada acción cambia tus puntos o energía. Lee la explicación y pulsa Continuar. "
                            "Completar los cuatro niveles activa el escudo.\n\n"
                            "Reiniciar una misión restaura sus puntos y energía iniciales; no acumula premios.")

    def abrir(self, nivel):
        self.juego.iniciar_mision(nivel)
        self.escena()
        self.efecto("¡Una nueva misión comienza!", sonido="abrir")

    def examinar(self, pista):
        self.pista.config(text=pista, fg=ACENTO)
        self.efecto("¡Encontraste una pista!", sonido="pista")

    def escena(self):
        mision = MISIONES[self.juego.nivel]
        actual = self.juego.escena_actual()
        self.limpiar(mision["titulo"])
        self.texto(mision["objetivo"], 12, ACENTO)
        self.texto(f"Sector {self.juego.nivel+1} · Situación {self.juego.paso+1}/{len(mision['escenas'])}", 11)
        self.texto(actual["texto"], 17)
        self.pista = self.texto("Evidencia sin examinar. Usa el botón para analizar la situación.", 12)
        self.boton("✦ Examinar evidencia", lambda: self.examinar(actual["pista"]))
        indices = list(range(len(actual["opciones"])))
        random.shuffle(indices)
        self.acciones = []
        for indice in indices:
            self.acciones.append(self.boton(actual["opciones"][indice]["texto"], lambda i=indice: self.responder(i)))
        self.retro = self.texto("Elige cómo actuar.", 12)
        self.siguiente = self.boton("Continuar", self.continuar, False)
        self.boton("Reiniciar esta misión", self.reiniciar)

    def responder(self, indice):
        resultado = self.juego.decidir(indice)
        self.vidas.config(text="ENERGÍA  " + "◆ " * self.juego.energia + "◇ " * (3-self.juego.energia),
                          fg=ACENTO if resultado["segura"] else ERROR)
        self.efecto("ACCESO SEGURO / +100 XP" if resultado["segura"] else "¡ALERTA! / −1 ENERGÍA",
                    ACENTO if resultado["segura"] else ERROR,
                    "acierto" if resultado["segura"] else "error")
        self.estado.config(text=f"Guardián: {self.juego.nombre}    |    XP: {self.juego.puntos}    |    "
                          f"Energía: {self.juego.energia}/3    |    Misiones: {len(self.juego.completadas)}/4")
        for boton in self.acciones:
            boton.config(state="disabled")
        prefijo = "Defensa reforzada: +100 XP. " if resultado["segura"] else "Brecha de seguridad: −50 XP (mínimo 0) y −1 energía. "
        self.retro.config(text=prefijo + resultado["explicacion"], fg=ACENTO if resultado["segura"] else ERROR)
        self.siguiente.config(state="normal", text="Ver resultado" if self.juego.derrota else "Continuar")

    def continuar(self):
        if self.juego.derrota:
            self.final()
            return
        energia_anterior = self.juego.energia
        estado = self.juego.continuar()
        if estado == "victoria":
            self.final()
        elif estado == "completada":
            self.mapa()
            recuperada = self.juego.energia > energia_anterior
            self.efecto("SECTOR PROTEGIDO / +1 ENERGÍA" if recuperada else "SECTOR PROTEGIDO / ENERGÍA AL MÁXIMO",
                        sonido="energia" if recuperada else "acierto")
        else:
            self.escena()

    def reiniciar(self):
        if self.juego.derrota:
            self.final()
        elif messagebox.askyesno("Reiniciar misión", "¿Restaurar el estado al inicio de esta misión?"):
            self.juego.reiniciar_mision()
            self.escena()
            self.efecto("MISIÓN RESTAURADA", sonido="abrir")

    def nueva(self):
        if messagebox.askyesno("Nueva partida", "¿Comenzar de nuevo? El progreso actual se perderá."):
            self.inicio()

    def final(self):
        self.limpiar("¡Escudo digital activado!" if self.juego.victoria else "La ciudad necesita otra oportunidad")
        self.ciudad()
        seguras = sum(1 for decision in self.juego.historial if decision["segura"])
        self.texto(f"Tomaste {seguras} decisiones seguras de {len(self.juego.historial)}. Puntuación: {self.juego.puntos}/900.")
        self.texto("Aprendizajes: verifica los mensajes por canales oficiales, protege cada cuenta con una clave única y multifactor, y reporta alertas siguiendo el protocolo.")
        riesgos = sorted({registro["nivel"] for registro in self.juego.historial if not registro["segura"]})
        if riesgos:
            self.texto("Repasa: " + ", ".join(MISIONES[i]["titulo"] for i in riesgos), 13, ACENTO)
        self.boton("Volver a jugar", self.inicio)
        self.boton("Salir", self.destroy)
        self.efecto("ESCUDO ACTIVADO / CIUDAD A SALVO" if self.juego.victoria else "CONEXIÓN PERDIDA / REINTENTAR",
                    ACENTO if self.juego.victoria else ERROR,
                    "victoria" if self.juego.victoria else "derrota")
