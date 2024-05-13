from clase_pedido import pedido
import csv
class gestor_pedido:
    __lista_pedido:list
    def __init__(self):
        self.__lista_pedido=[]
    def agregar_pedido(self,xpatente):
        xpedido=pedido(xpatente,input("ingrese id del pedido:\n"),input("ingrese comida del pedido:\n"),input("ingrese tiempo estimado de entrega:\n"),input("ingrese tiempo real de entrega:\n"),input("ingrese precio del pedido:\n"))
        self.__lista_pedido.append(xpedido)
    def agregar_p_desde_archi(self):
        archi=open("datosPedidos.csv")
        reader=csv.reader(archi,delimiter=";")
        for fila in reader:
            ypedido=pedido(fila[0],fila[1],fila[2],int(fila[3]),float(fila[4]),float(fila[5]))
            self.__lista_pedido.append(ypedido)
    def mod_tiempo_real(self,xid,xtiempo):
        i=0
        while i<len(self.__lista_pedido) and xid!=self.__lista_pedido[i].getid():
            i+=1
        if i<len(self.__lista_pedido):
            self.__lista_pedido[i].mod_tiempo_real(xtiempo)
        else:
            print("el pedido no se encontro")
    def tiempo_real_prom(self,xpatente):
        total=0
        cont=0
        for i in range(len(self.__lista_pedido)):
            if self.__lista_pedido[i].get_patente()==xpatente:
                total+=self.__lista_pedido[i].get_tiempo_real()
                cont+=1
        print(f"el tiempo real promedio del conductor es: {total/cont}")
    def comision_conductor(self,xpat):
        total=0
        print("identificador de pedido    tiempo estimado    tiempo real    precio\n")
        for i in range(len(self.__lista_pedido)):
            if self.__lista_pedido[i].get_patente()==xpat:
                total=total+self.__lista_pedido[i].get_precio()
                print(f"{self.__lista_pedido[i].getid()}                            {self.__lista_pedido[i].get_estimado()}                {self.__lista_pedido[i].get_tiempo_real()}           {self.__lista_pedido[i].get_precio()}")
        print(f"total:                                                         {total}\ncomision: ${total*0.20}")
    def ordenar(self):
        self.__lista_pedido.sort()