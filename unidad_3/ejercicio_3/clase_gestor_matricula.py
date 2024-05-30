from clase_matricula import matricula
class gestor_matriculas:
    __lista:list
    def __init__(self):
        self.__lista=[]
    def agregar_matricula(self,gestor_emp,gestor_programas):
        xfecha=input("ingrese la fecha de la matricula:\n")
        xid=int(input("ingrese el id del empleado que obtuvo la matricula:\n"))
        xnom=input("ingrese el nombre del programa de capacitacion de la matricula:\n")
        xmatricula=matricula(xfecha,gestor_emp.get_emp(xid),gestor_programas.get_programa(xnom))
        self.__lista.append(xmatricula)
    def duracion_programas_emp(self,xid):
        total=0
        for xmat in self.__lista:
            xemp=xmat.get_emp()
            if xemp.get_id()==xid:
                xprograma=xmat.get_programa()
                total+=xprograma.get_duracion()
        return total
    def empleados_matriculados_programa(self,xnom):
        for xmat in self.__lista:
            xprograma=xmat.get_programa()
            if xprograma.get_nom()==xnom:
                xmat.mostrar_empleado()
    def informar_no_mat(self,xemp):
        i=0
        yemp=self.__lista[i].get_emp()
        while i<len(self.__lista) and xemp.get_id()!=yemp.get_id():
            i+=1
            if i<len(self.__lista):
                yemp=self.__lista[i].get_emp()
        if not i<len(self.__lista):
            print (xemp)