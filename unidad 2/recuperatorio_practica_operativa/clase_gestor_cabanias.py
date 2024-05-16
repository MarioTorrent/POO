import numpy as np
from clase_cabania import cabania
import csv
class gestor_cabanias:
    __cabanias:np.array
    def __init__(self):
        self.__cabanias=np.empty(10,dtype=object)
    def carga(self):
        archi=open("unidad 2\\recuperatorio_practica_operativa\\Cabañas.csv")
        reader=csv.reader(archi,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                xnum=int(fila[0])-1
                xcabania=cabania(int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),float(fila[4]))
                self.__cabanias[xnum]=xcabania
    def reserva(self,xnum):
        self.__cabanias[xnum-1].reservar()
    def mostrar_cabañas_disponibles(self,cant_huespedes):
        for xcabania in self.__cabanias:
            if xcabania>=cant_huespedes and xcabania.get_reserva()==False:
                print(f"cabania numero: {xcabania.get_num()}")
    def get_imp(self,num):
        return self.__cabanias[num-1].get_imp()