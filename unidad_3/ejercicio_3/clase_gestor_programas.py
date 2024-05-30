from clase_Programa_Capacitacion import programa_capacitacion
class gestor_programas:
    __lista:list
    def __init__(self):
        self.__lista=[]
    def agregar_programa(self):
        xnom=input("ingrese el nombre del programa:\n")
        xcod=input("ingrese el codigo del programa de capacitacion:\n")
        xduracion=int(input("ingrese la duracion del programa de capacitacion:\n"))
        xprograma=programa_capacitacion(xnom,xcod,xduracion)
        self.__lista.append(xprograma)
    def get_programa(self,xnom):
        i=0
        while i<len(self.__lista) and self.__lista[i].get_nom()!=xnom:
            i+=1
        if i<len(self.__lista):
            return self.__lista[i]
        else:
            print("no se encontro en nombre ingresado\n")