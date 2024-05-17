from clase_equipo import equipo
import csv
class gestor_equipo:
    __lista_equipo:list
    def __init__(self):
        self.__lista_equipo=[]
    def carga (self):
        archi=open("unidad 2\\ejercicio_5\\equipos2024.csv")
        reader=csv.reader(archi,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                xequipo=equipo(fila[0],fila[1],int(fila[2]),int(fila[3]),int(fila[4]))
                self.__lista_equipo.append(xequipo)
        archi.close
    def act_datos(self,id,golesF,golesC):
        i=0
        while self.__lista_equipo[i].obtener_id() != id and i<len(self.__lista_equipo):
            i+=1
        if i<len(self.__lista_equipo):
            if golesF>golesC:
                puntos=3
            elif golesF==golesC:
                puntos=1
            else:
                puntos=0
            self.__lista_equipo[i].actualizar_datos(int(golesF),int(golesC),int(puntos))
    def obt_id(self,nom):
        i=0
        while i<len(self.__lista_equipo) and nom!=self.__lista_equipo[i].obtener_nombre():
            i+=1
        if i<len(self.__lista_equipo):
            return self.__lista_equipo[i].obtener_id()
    def ordenar_tabla(self):
        self.__lista_equipo.sort(reverse=True)
    def mostrar_equipos(self):
        for i in range(len(self.__lista_equipo)):
            print (self.__lista_equipo[i])