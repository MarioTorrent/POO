from clase_gestor_empleados import gestor_empleados
from clase_gestor_programas import gestor_programas
from clase_gestor_matricula import gestor_matriculas
def menu():
    aux=0
    xgestor_de_empleados=gestor_empleados()
    xgestor_de_programas=gestor_programas()
    xgestor_matriculas=gestor_matriculas()
    while aux!=7:    
        aux=int(input("1_agregar empleado por teclado\n2_agregar programa de capacitacion por teclado\n3_agregar matricula\n4_ingresar id del empleado y ver la duracion de los programas de capacitacion que posee\n5_mostrar los empleados en un programa de capacitacion\n6_informar empleados que no han sido matriculados a ningun programa de capacitacion\n7_fin\n"))
        if aux==1:
            xgestor_de_empleados.agregar_empleado()
        elif aux==2:
            xgestor_de_programas.agregar_programa()
        elif aux==3:
            xgestor_matriculas.agregar_matricula(xgestor_de_empleados,xgestor_de_programas)
        elif aux==4:
            xid=int(input("ingrese el id del empleado:\n"))
            print(f"el total de horas de todos los programas a los que se matriculo el empleado es:{xgestor_matriculas.duracion_programas_emp(xid)}")
            
        elif aux==5:
            xnom=input("ingrese el nombre del programa:\n")
            xgestor_matriculas.empleados_matriculados_programa(xnom)
        elif aux==6:
            xgestor_de_empleados.empleados_no_matriculados(xgestor_matriculas)
        elif aux==7:
            pass
        else:
            print("la opcion ingresada no es correcta\n")
if __name__=="__main__":
    menu()