import datetime
from clase_gestor_jugadores import gestor_jugadores
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
class juego(tk.Tk):
    __botones:list
    __text:object
    __xcanvas:object
    __colores_originales:list
    __boton_inicio:object
    __puntos:int
    __boton_random:object
    __lbl_P:object
    __xvent:object
    __lbl:object
    __entr_user:object
    __btn:object
    __nom:StringVar
    __dificultad:int
    __xgestor:object
    __xbtn:object
    __seceuencia_random:list
    __secuencia_clickeada:list
    def __init__(self,xgestor):
        super().__init__()
        self.config(background="grey")
        self.__xgestor=xgestor
        self.geometry("600x600")
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=20)
        self.columnconfigure(0,weight=20)
        self.__xframe=tk.Frame(self)
        self.__xframe.grid(column=0,row=0,sticky=(S,W,E,N))
        self.__xframe.rowconfigure(0,weight=1)
        self.__xframe.rowconfigure(1,weight=1)
        self.__xframe.columnconfigure(0,weight=1)
        self.__xframe.columnconfigure(1,weight=1)
        self.__xcanvas=tk.Canvas(self)
        self.__xcanvas.grid(column=0,row=1,sticky=(N,W,S,E))
        self.__xcanvas.config(background="grey")
        self.__botones=[]
        self.__botones.append(self.__xcanvas.create_arc(90,50,540,430,start=180,extent=-90,outline="white",fill="green"))
        self.__botones.append(self.__xcanvas.create_arc(100,50,550,430,outline="white",fill="red"))
        self.__botones.append(self.__xcanvas.create_arc(90,60,540,440,start=180,extent=90,outline="white",fill="yellow"))
        self.__botones.append(self.__xcanvas.create_arc(100,60,550,440,start=-90,extent=90,outline="white",fill="blue"))
        self.__boton_inicio=self.__xcanvas.create_oval(200,150,450,340,fill="white",outline="white")
        self.__text=None
        self.__colores_originales = [self.__xcanvas.itemcget(boton, "fill") for boton in self.__botones]
        self.__puntos=None
        self.__lbl_P=None
        self.__xvent=None
        self.__lbl=None
        self.__nom=StringVar()
        self.__entr_user=None
        self.__btn=None
        self.__dificultad=tk.IntVar(self,1)
        self.__xbtn=None
        self.__secuencia_clickeada=[]
        self.__seceuencia_random=[]
        self.enter_user()
    def enter_user(self):
        self.__xvent=Toplevel(self)
        self.__xvent.resizable(0,0)
        self.__xvent.grab_set()
        self.__xvent.focus_force()
        self.__xvent.lift()
        self.__xvent.transient(self)
        self.__xvent.geometry("300x150+650+300")
        self.__lbl=tk.Label(self.__xvent,text="nombre de usuario:")
        self.__lbl.pack()
        self.__entr_user=tk.Entry(self.__xvent,textvariable=self.__nom)
        self.__entr_user.pack()
        self.__btn=tk.Button(self.__xvent,text="jugar",command=lambda:[self.__xvent.destroy(),self.inicio()])
        self.__btn.pack()
    def inicio(self):
        self.__lbl_user=ttk.Label(self.__xframe,text=f"usuario: {self.__nom.get()}")
        self.__lbl_user.grid(column=0,row=0,sticky=(W,E,N,S))
        self.__puntos=0
        self.__lbl_P=ttk.Label(self.__xframe,text="puntos: 0")
        self.__lbl_P.grid(column=1,row=0,sticky=(N,S,W))
        self.actualizar_puntos()
        for boton in self.__botones:
            self.__xcanvas.itemconfig(boton,outline="white",width=1)
        self.__text=self.__xcanvas.create_text(327,245,text="INICIO",fill="black",font=("Times New Roman",30))
        self.__xcanvas.tag_bind(self.__boton_inicio, "<Button-1>",lambda event:[self.click_inicio(event),self.start(event)])
        self.__xcanvas.tag_bind(self.__text, "<Button-1>",lambda event:[self.click_inicio(event),self.start(event)])
        self.__btn= tk.Menubutton(self, text="Seleccionar dificultad", relief=RAISED)
        menu = tk.Menu(self.__btn, tearoff=0)
        self.__btn.config(menu=menu)
        menu.add_radiobutton(label="Fácil", variable=self.__dificultad, value=1)
        menu.add_radiobutton(label="Medio", variable=self.__dificultad, value=2)
        menu.add_radiobutton(label="Difícil", variable=self.__dificultad, value=3)
        self.__btn.grid(column=0,row=0,sticky=(S,E))
        self.__xbtn= tk.Menubutton(self.__xframe, text="menu", relief=RAISED)
        xmenu = tk.Menu(self.__xbtn, tearoff=0)
        self.__xbtn.config(menu=xmenu)
        xmenu.add_radiobutton(label="tabla de posiciones", command=lambda:self.mostrar_pos())
        xmenu.add_radiobutton(label="SALIR", command=self.destroy)
        self.__xbtn.grid(column=0,row=1,sticky=(N,W))
    def start(self,event):
        self.__xcanvas.tag_unbind(self.__boton_inicio,"<Button-1>")
        self.__xcanvas.tag_unbind(self.__text,"<Button-1>")
        self.__xcanvas.delete(self.__text)
        for boton in self.__botones:
            self.__xcanvas.tag_bind(boton, "<Button-1>",self.click)
        #if self.__dificultad.get()==2:
            #self.__tiempo_restante=5
        self.elegir_boton_random()
    def click_inicio(self,event):
        self.__xcanvas.itemconfig(self.__boton_inicio,fill="green")
        self.__xcanvas.after(200,lambda: self.__xcanvas.itemconfig(self.__boton_inicio,fill="white"))
    def click(self,event):
        boton=self.__xcanvas.find_closest(event.x, event.y)[0]
        self.__xcanvas.itemconfig(boton,fill="white")
        self.__secuencia_clickeada.append(boton)
        self.__xcanvas.after(200, lambda: self.__xcanvas.itemconfig(boton, fill=self.__colores_originales[self.__botones.index(boton)]))
        if self.__secuencia_clickeada[len(self.__secuencia_clickeada)-1]==self.__seceuencia_random[len(self.__secuencia_clickeada)-1]:
            if len(self.__secuencia_clickeada)==len(self.__seceuencia_random):
                self.__puntos+=1
                self.actualizar_puntos()
                self.__secuencia_clickeada=[]
                self.elegir_boton_random()
        else:
            self.game_over()
    def actualizar_puntos(self):
        self.__lbl_P.config(text=f"puntos: {self.__puntos}")
    def game_over(self):
        fecha_y_hora=datetime.datetime.now()
        self.__seceuencia_random=[]
        self.__secuencia_clickeada=[]
        self.__xgestor.agregar_jugador(self.__nom.get(),self.__puntos,fecha_y_hora.date(),fecha_y_hora.time())
        self.__xvent=Toplevel(self)
        self.__xvent.resizable(0,0)
        self.__xvent.transient()
        self.__xvent.grab_set()
        self.__xvent.geometry("200x200+100+100")
        self.__xvent.rowconfigure(0,weight=1)
        self.__xvent.rowconfigure(1,weight=1)
        self.__xvent.rowconfigure(2,weight=1)
        self.__xvent.columnconfigure(0,weight=1)
        self.__xvent.columnconfigure(1,weight=1)
        self.__xvent.columnconfigure(2,weight=1)
        lbl=tk.Label(self.__xvent,text="¡¡GAME OVER!!")
        lbl.grid(column=1,row=0,sticky=(S,W,N,E))
        self.__lbl=tk.Label(self.__xvent,text=f"puntos: {self.__puntos}")
        self.__lbl.grid(column=1,row=1,sticky=(S,W,N,E))
        self.__btn=tk.Button(self.__xvent,text="volver a intentarlo",command=lambda:[self.__xvent.destroy(),self.enter_user()])
        self.__btn.grid(column=1,row=2)
    def mostrar_pos(self):
        self.__xvent=Toplevel(self)
        self.__xvent.resizable(0,0)
        self.__xvent.geometry("400x400+100+100")
        self.transient()
        self.__xgestor.mostrar_posiciones(self.__xvent)
    def elegir_boton_random(self):
        self.__boton_random=random.choice(self.__botones)
        self.__seceuencia_random.append(self.__boton_random)
        i=0
        for boton in self.__seceuencia_random:
            i+=400
            #x=self.__seceuencia_random[j]
            self.__xcanvas.after(100+i,lambda b=boton: self.__xcanvas.itemconfig(b,outline="black",width=5))
            self.__xcanvas.after(350+i,lambda b=boton: self.__xcanvas.itemconfig(b,outline="white",width=1))
if __name__=="__main__":
    xgestor=gestor_jugadores()
    xjuego=juego(xgestor)
    xjuego.mainloop()