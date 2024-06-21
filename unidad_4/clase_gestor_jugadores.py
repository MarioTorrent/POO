import json
from pathlib import Path
from clase_jugador import jugador
import tkinter as tk
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
        lbl=tk.Label(xvent,text="nombre".center(25)+"puntos".center(25)+"fecha".center(25)+"hora".center(25))
        lbl.pack()
        for xjugador in self.__lista:
            xlbl=tk.Label(xvent,text=f"{xjugador}")
            xlbl.pack()
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,jugadores=[xjugador.toJSON() for xjugador in self.__lista ])
        return d