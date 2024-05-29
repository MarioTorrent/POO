from clase_gestor_mamas import gestor_mamas
from clase_gestor_nacimientos import gestor_nacimiento
def menu():
    xgestor_mamas=gestor_mamas()
    xgestor_nacimientos=gestor_nacimiento()
    aux=1
    while aux!=5:
        aux=int(input("1_cargar gestor de mamas\n2_cargar gestor de nacimientos_\n3_mostrar informarmacion del parto y de la mama con el dni ingresado\n4_ mostrar datos de la/s mama/s que han tenido parto multiple\n5_fin\n"))
        if aux==1:
            xgestor_mamas.carga()
        elif aux==2:
            xgestor_nacimientos.carga()
        elif aux==3:
            xdni=int(input("ingrese el dni de la madre:\n"))
            xgestor_mamas.mostrar_datos_mama(xdni)
            xgestor_nacimientos.mostrar_datos_nacimiento_mama(xdni)
        elif aux==4:
            for i in range(xgestor_mamas.get_long()):
                xdni=xgestor_mamas.get_dni_mama(i)
                bebes=xgestor_nacimientos.contar_nacimientos_de_una_mama(xdni)
                if bebes>1:
                    print(f"{xgestor_mamas.mostrar_datos_mama(xdni)}")
if __name__=="__main__":
    menu()