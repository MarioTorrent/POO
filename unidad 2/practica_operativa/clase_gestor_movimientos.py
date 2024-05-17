import numpy as np
import csv
from clase_movimiento import movimiento
class gestor_movimientos:
    __arreglo_movi:np.array
    def __init__(self):
        self.__arreglo_movi=np.array([])
    def carga(self):
        bandera=True
        archi=open("unidad 2\\practica_operativa\\MovimientosAbril2024.csv")
        reader=csv.reader(archi,delimiter=";")
        for fila in reader:
            if bandera==True:
                bandera=not bandera
            else:
                xmovimiento=movimiento(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4]))
                self.__arreglo_movi=np.append(self.__arreglo_movi,xmovimiento)
    def get_saldo_act(self,xnum):
        xsaldo=0
        print("fecha        descripcion             importe        tipo de movimiento")
        for xmov in self.__arreglo_movi:
            if xnum==xmov.get_num_cuenta():
                if xmov.get_tipo()=="C":
                    xsaldo+=xmov.get_imp()
                elif xmov.get_tipo()=="P":
                    xsaldo-=xmov.get_imp()
                print(xmov)
        return xsaldo
    def buscar(self,xnum):
        aux=-1
        for xmov in self.__arreglo_movi:
            if xmov.get_num_cuenta()==xnum:
                aux=1
        return aux
    def ordenar(self):
        self.__arreglo_movi=np.sort(self.__arreglo_movi)
