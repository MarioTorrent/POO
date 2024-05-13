from clase_moto import moto
import csv
class gestor_motos:
    __lista_moto:list
    def __init__(self):
        self.__lista_moto=[]
    def agregar_motos(self):
        archi=open("datosMotos.csv")
        reader=csv.reader(archi,delimiter=";")
        for fila in reader:
            ymoto=moto(fila[0],fila[1],fila[2],int(fila[3]))
            self.__lista_moto.append(ymoto)
    def buscar_moto(self,patente):
        aux=-1
        for zmoto in self.__lista_moto:
            if patente==zmoto.get_pat():
                aux= 1
        return aux
    def cant_motos(self):
        return len(self.__lista_moto)
    def mostrar_datos_conductor(self,patente):
        i=0
        while i<len(self.__lista_moto) and patente!=self.__lista_moto[i].get_pat():
            i+=1
        if i<len(self.__lista_moto):
            self.__lista_moto[i].mostrar_datos()
    def mostrar_pat_y_nombre(self,i):
        print(f"\npatente: {self.__lista_moto[i].get_pat()}\nnombre: {self.__lista_moto[i].get_conductor()}")
        return self.__lista_moto[i].get_pat()