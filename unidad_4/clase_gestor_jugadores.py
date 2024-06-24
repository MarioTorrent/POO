import json
from pathlib import Path
from clase_jugador import jugador
import tkinter as tk
from tkinter import ttk
class gestor_jugadores(object):
    __lista:list 
    def __init__(self):
        self.__lista=[]
    def agregar_jugador(self,nom,puntos,fecha,hora):
        xhora=str(hora)[:8]
        xjugador=jugador(nom,puntos,fecha,xhora)
        self.__lista.append(xjugador)
        self.ordenar()
    def agregar_jugador_json(self,xjugador):
        self.__lista.append(xjugador)
    def ordenar(self):
        self.__lista.sort(reverse=True)
    def mostrar_posiciones(self,xvent):
        tabla=ttk.Treeview(xvent,columns=("nombre","puntos","fecha","hora"))
        tabla.heading("#0",text="posicion")
        tabla.heading("#1",text="nombre")
        tabla.heading("#2",text="puntos")
        tabla.heading("#3",text="fecha")
        tabla.heading("#4",text="hora")
        tabla.column("#0",anchor="center")
        tabla.column("#1",anchor="center")
        tabla.column("#2",anchor="center")
        tabla.column("#3",anchor="center")
        tabla.column("#4",anchor="center")
        tabla.pack()
        i=1
        for xjugador in self.__lista:
            tabla.insert("","end",text=f"{i}°",values=xjugador.get_datos())
            i+=1
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,jugadores=[xjugador.toJSON() for xjugador in self.__lista ])
        return d