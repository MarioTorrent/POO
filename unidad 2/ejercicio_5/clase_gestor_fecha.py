from clase_fecha_de_futbol import fecha_de_futbol
import csv
class gestor_fecha:
    __lista_fecha:list
    def __init__(self):
        self.__lista_fecha=[]
    def carga(self):
        archi=open("unidad 2\\ejercicio_5\\fechasFutbol.csv")
        reader=csv.reader(archi,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                xfecha=fecha_de_futbol(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista_fecha.append(xfecha)
    def obtener_datosF(self,i):
        if i < len(self.__lista_fecha):
            return self.__lista_fecha[i].obtener_datos()
    def mostrar_partidos(self,id,nom):
        i=0
        print(f"equipo: {nom}\nfecha      goles a favor   goles en contra   puntos")
        while i<len(self.__lista_fecha):
            self.__lista_fecha[i].datos_equipo(id)
            i+=1
    def mostrar_long(self):
        return len(self.__lista_fecha)