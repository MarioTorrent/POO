import numpy as np
import csv
from clase_mama import mama
class gestor_mamas:
    __lista:np.array
    def __init__(self):
        self.__lista=np.array([],dtype=object)
    def carga(self):
        archi=open("unidad 2\\recuperatorio de la practica operativa 1\\Mamas.csv")
        reader=csv.reader(archi,delimiter=";")
        next(reader)
        for fila in reader:
            objeto=mama(*fila)
            self.__lista=np.append(self.__lista,objeto)
    def mostrar_datos_mama(self,xdni):
        i=0
        while self.__lista[i].get_dni()!=xdni and i<len(self.__lista):
            i+=1
        if i<len(self.__lista):
            print(f"{self.__lista[i]}")
        else:
            print("no se encontro el dni")
    def get_dni_mama(self,i):
        return self.__lista[i].get_dni()
    def get_long(self):
        return len(self.__lista)