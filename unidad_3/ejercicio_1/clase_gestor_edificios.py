import csv
from clase_edificio import edificio
class gestor_edificios:
    __edificios:list
    def __init__(self):
        self.__edificios=[]
    def carga_archi(self):
        archi=open("unidad_3\\ejercicio_1\\EdificioNorte.csv")
        reader=csv.reader(archi,delimiter=";")
        for fila in reader:
            if len(fila)==6:
                xedificio=edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                self.__edificios.append(xedificio)
            else:
                self.__edificios[int(fila[0])-1].carga_deptos(int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
    def mostar_propietarios_edificio(self,xnom):
        i=0
        while i <len(self.__edificios) and self.__edificios[i].get_nom()!=xnom:
            i+=1
        if i<len(self.__edificios):
            self.__edificios[i].mostrar_propietarios()
    def mostrar_sup_edificio(self,xnom):
        i=0
        while i <len(self.__edificios) and self.__edificios[i].get_nom()!=xnom:
            i+=1
        if i<len(self.__edificios):
            print(f"la superficie total del edificio es: {self.__edificios[i].get_sup_total()}")
        else:
            print("el nombre ingresado no es valido")
    def sup_depto_prop(self,xnom):
        for i in range(len(self.__edificios)):
            self.__edificios[i].get_sup_depto(xnom)
    def golden_deptos_piso(self,xpiso):
        cont=0
        for i in range(len(self.__edificios)):
            cont=self.__edificios[i].golden_deptos(xpiso,cont)
            print(f"el numero de departamentos en el piso {xpiso} con tres dormitorios y mas de 1 banio es: {cont}")
            