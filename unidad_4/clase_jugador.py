import json
from pathlib import Path
class jugador():
    __nombre:str
    __puntos:int
    __fecha:str
    __hora:str
    def __str__(self):
        return f"{self.__nombre}".center(25)+f"{self.__puntos}".center(25)+f"{self.__fecha}".center(25)+f"{self.__hora}".center(25)
    def __init__(self,nom,puntos,fecha,hora):
        self.__nombre=nom
        self.__puntos=puntos
        self.__fecha=str(fecha)
        self.__hora=str(hora)
    def __gt__(self,otro):
        return self.__puntos>otro.get_puntos()
    def get_puntos(self):
        return self.__puntos
    def toJSON(self):
        d = dict(__class__=self.__class__.__name__ , __atributos__=dict(nombre=self.__nombre,puntos=self.__puntos,fecha=self.__fecha,hora=self.__hora))
        return d