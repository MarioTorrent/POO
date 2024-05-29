import csv
from clase_nacimiento import nacimiento
class gestor_nacimiento:
    __lista:list
    def __init__(self):
        self.__lista=[]
    def carga(self):
        archi=open("unidad 2\\recuperatorio de la practica operativa 1\\Nacimientos.csv")
        reader=csv.reader(archi,delimiter=";")
        next(reader)
        for fila in reader:
            xobjeto=nacimiento(*fila)
            self.__lista.append(xobjeto)
    def mostrar_datos_nacimiento_mama(self,xdni):
        bandera=True
        for xnacimiento in self.__lista:
            if xnacimiento.get_dni()==xdni:
                if bandera==True:
                    if xnacimiento.get_tipo()=="N":
                        tipo="normal"
                    else:
                        tipo="cesaria"
                    print(f"tipo de parto: {tipo}\nBebe/s\n","peso      Altura")
                    bandera=not bandera
                print(f"{xnacimiento}")
    def contar_nacimientos_de_una_mama(self,xdni):
        cont=0
        ynacimiento:object
        bandera=True
        for xnacimiento in self.__lista:
            if xnacimiento.get_dni()==xdni:
                if bandera:
                    ynacimiento=xnacimiento
                    bandera=not bandera
                if xnacimiento == ynacimiento:
                    cont+=1
        return cont