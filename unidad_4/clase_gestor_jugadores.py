from clase_jugador import jugador
import tkinter as tk
class gestor_jugadores():
    __lista:list 
    def __init__(self):
        self.__lista=[]
    def agregar_jugador(self,nom,puntos,fecha,hora):
        xhora=str(hora)[:8]
        xjugador=jugador(nom,puntos,fecha,xhora)
        self.__lista.append(xjugador)
        self.ordenar()
    def ordenar(self):
        self.__lista.sort(reverse=True)
    def mostrar_posiciones(self,xvent):
        lbl=tk.Label(xvent,text="nombre".center(25)+"puntos".center(25)+"fecha".center(25)+"hora".center(25))
        lbl.pack()
        for xjugador in self.__lista:
            xlbl=tk.Label(xvent,text=f"{xjugador}")
            xlbl.pack()