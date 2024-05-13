from clase_gestor_pedidos import gestor_pedido
from clase_gestor_motos import gestor_motos
def menu():
    aux=1
    pedidos=gestor_pedido()
    motos=gestor_motos()
    while aux!=0:
        aux=int(input("1_cargar datos de las motos desde archivo\n2_cargar datos de los pedidos desde archivos\n3_cargar nuevo pedido\n4_modificar el tiempo real de entrega\n5_mostrar datos de un conductor y el tiempo real de entrega promedio\n6_generar listado de motos y el pago de comisiones a conductores\n7_ordenar\n8_fin\n"))
        if aux==1:
            motos.agregar_motos()
        elif aux==2:
            pedidos.agregar_p_desde_archi()
        elif aux==3:
            xpat=input("ingrese la patente de la moto a la que se la asigna el pedido:\n")
            if motos.buscar_moto(xpat)!=-1:
                pedidos.agregar_pedido(xpat)
        elif aux==4:
            xid=input("ingrese el id del pedido:\n")
            xtiempo_real=int(input("ingrese el tiempo real:\n"))
            pedidos.mod_tiempo_real(xid,xtiempo_real)
        elif aux==5:
            xpatente=input("ingrese la patente de la moto:\n")
            motos.mostrar_datos_conductor(xpatente)
            pedidos.tiempo_real_prom(xpatente)
        elif aux==6:
            for i in range(0,motos.cant_motos()):
                pat=motos.mostrar_pat_y_nombre(i)
                pedidos.comision_conductor(pat)
        elif aux==7:
            pedidos.ordenar()
        elif aux==8:
            return
if __name__=="__main__":
    menu()