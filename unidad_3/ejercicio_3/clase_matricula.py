from clase_empleado import empleado
from clase_Programa_Capacitacion import programa_capacitacion
class matricula:
    __fecha:str
    __empleado:empleado
    __programa:programa_capacitacion
    def __init__(self,xfecha,emp,programa):
        self.__fecha=xfecha
        self.__empleado=emp
        self.__programa=programa
        self.__empleado.addmatricula(self)
        self.__programa.addmatricula(self)
    def get_programa(self):
        return self.__programa
    def mostrar_empleado(self):
        print(self.__empleado)
    def get_emp(self):
        return self.__empleado