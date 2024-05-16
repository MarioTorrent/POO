from clase_gestor_cabanias import gestor_cabanias
from clase_gestor_reservas import gestor_reservas
def menu():
    xgestor_cabanias=gestor_cabanias()
    xgestor_reservas=gestor_reservas()
    bandera=True
    while bandera:
        aux=int(input("1_cargar cabanias\n2_cargar reservas\n3_mostrar cabañas con capacidad mayor o igual ingresada no reservadas\n4_mostrar las reservas para una fecha\n5_fin\n"))
        if aux==1:
            xgestor_cabanias.carga()
        elif aux==2:
            xgestor_reservas.carga()
            long=xgestor_reservas.get_long()
            for i in range(long):
                aux=xgestor_reservas.get_cabania(i)
                xgestor_cabanias.reserva(aux)
        elif aux==3:
            cantH=int(input("ingrese la cantidad de huespedes:\n"))
            xgestor_cabanias.mostrar_cabañas_disponibles(cantH)
        elif aux==4:
            xfecha=input("ingrese la fecha:\n")
            print(f"reservas para la fecha: {xfecha}\n")
            print("N° de cabania ","Importe diario".center(20),"Cantidad dias".center(20),"Senia".center(20),"importe a cobrar\n".center(20))
            for i in range(xgestor_reservas.get_long()):
                xnum=xgestor_reservas.get_cabania(i)
                ximp=xgestor_cabanias.get_imp(xnum)
                if xfecha==xgestor_reservas.get_fecha(i):
                    xgestor_reservas.mostrar_segun_fecha(i,ximp)
        elif aux==5:
            return()
if __name__=="__main__":
    menu()