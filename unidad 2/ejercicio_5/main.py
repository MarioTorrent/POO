from clase_gestor_equipo import gestor_equipo
from clase_gestor_fecha import gestor_fecha
def menu():
    equipos=gestor_equipo()
    fechas=gestor_fecha()
    aux=1
    while aux!=0:
        print("1_ cargar los datos del equipo desde el archivo\n2_cargar los datos de las fechas de futbol desde el archivo\n3_ver las fechas jugadas por un equipo\n4_actualizar la tabla de todos los equipos con el resultado de las fechas disputadas\n5_ordenar la tabla de posiciones\n6_cargar la tabla de posiciones en archivo tabla.csv\n7_mostrar equipos\n8_salir\n")
        aux=int(input())
        if aux==1:
            equipos.carga()
        elif aux==2:
            fechas.carga()
        elif aux==3:
            xnom=input("ingrese el nombre del equipo: \n")
            xid=equipos.obt_id(xnom)
            fechas.mostrar_partidos(xid,xnom)
        elif aux==4:
            for i in range(fechas.mostrar_long()):
                idL,idV,golesL,golesV = fechas.obtener_datosF(i)
                equipos.act_datos(idL,golesL,golesV)
                equipos.act_datos(idV,golesV,golesL)
        elif aux==5:
            equipos.ordenar_tabla()
        elif aux==6:
            pass
        elif aux==7:
            equipos.mostrar_equipos()
        elif aux==8:
            return()
        else:
            print("opcion no encontrada, vuelva a intentarlo\n")
            print("1_ cargar los datos del equipo desde el archivo\n2_cargar los datos de las fechas de futbol desde el archivo\n3_ver las fechas jugadas por un equipo\n4_actualizar la tabla de todos los equipos con el resultado de las fechas disputadas\n5_ordenar la tabla de posiciones\n6_cargar la tabla de posiciones en archivo tabla.csv")
            aux=int(input())
if __name__=="__main__":
    menu()