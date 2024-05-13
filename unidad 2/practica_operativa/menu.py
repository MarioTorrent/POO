from clase_gestor_clientes import gestor_cliente
from clase_gestor_movimientos import gestor_movimientos
import numpy as np
def menu():
    clientes=gestor_cliente()
    movimientos=gestor_movimientos()
    aux=1
    while aux!=0:
        aux=int(input("1_cargar clientes del mes de arbil\n2_cargar mocimientos del mes de abril\n3_actualizar los datos de un cliente\n4_verificar si un cliente tuvo movimientos en al mes de abril\n5_ordenar lista de movimientos\n6_fin\n"))
        if aux == 1:
            clientes.carga()
        elif aux == 2:
            movimientos.carga()
        elif aux == 3:
            xdni=input("ingrese el dni:\n")
            xnum=clientes.buscar_dni(xdni)
            xsaldo=movimientos.get_saldo_act(xnum)
            clientes.actualizar_saldo(xdni,xsaldo)
        elif aux == 4:
            xdni=input("ingrese dni:\n")
            xnum=clientes.buscar_dni(xdni,1)
            if movimientos.buscar(xnum)==1:
                clientes.mostrar_ap_nom(xdni)
        elif aux == 5:
            movimientos.ordenar()
        elif aux == 6:
            return ()
if __name__=="__main__":
    menu()