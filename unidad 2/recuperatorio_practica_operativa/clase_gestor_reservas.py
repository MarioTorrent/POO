import csv
from clase_reserva import reserva
class gestor_reservas:
    __reservas:list
    def __init__(self):
        self.__reservas=[]
    def carga(self):
        archi=open("unidad 2\\recuperatorio_practica_operativa\\Reservas.csv")
        reader=csv.reader(archi,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                xreserva=reserva(int(fila[0]),fila[1],int(fila[2]),fila[3],int(fila[4]),int(fila[5]),float(fila[6]))
                self.__reservas.append(xreserva)
    def get_long(self):
        return len(self.__reservas)
    def get_cabania(self,i):
        return self.__reservas[i].get_cab()
    def get_fecha(self,i):
        return self.__reservas[i].get_fecha()
    def mostrar_segun_fecha(self,i,ximp):
        self.__reservas[i].mostrar_datos(ximp)