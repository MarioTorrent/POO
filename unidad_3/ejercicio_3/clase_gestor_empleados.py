from clase_empleado import empleado
class gestor_empleados:
    __lista:list
    def __init__(self):
        self.__lista=[]
    def agregar_empleado(self):
        xnom=input("ingrese el nombre y apellido de empleado:\n")
        xid=int(input("ingrese el id del empleado:\n"))
        xpuesto=input("ingrese el puesto del empleado:\n")
        xempleado=empleado(xnom,xid,xpuesto)
        self.__lista.append(xempleado)
    def get_emp(self,xid):
        i=0
        while i<len(self.__lista) and self.__lista[i].get_id()!=xid:
            i+=1
        if i<len(self.__lista):
            return self.__lista[i]
        else:
            print("no se encontro el id ingresado\n")
    def empleados_no_matriculados(self,gestor_mat):
        for xemp in self.__lista:
            gestor_mat.informar_no_mat(xemp)