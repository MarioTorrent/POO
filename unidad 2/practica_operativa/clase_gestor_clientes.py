from clase_cliente import cliente
import csv
class gestor_cliente:
    __lista_clientes:list
    def __init__(self):
        self.__lista_clientes=[]
    def carga(self):
        bandera=True
        archi=open("unidad 2\\practica_operativa\\ClientesFarmaCiudad.csv")
        reader=csv.reader(archi,delimiter=";")
        for fila in reader:
            if bandera==True:
                bandera=not(bandera)
            else:
                xcliente=cliente(fila[0],fila[1],fila[2],int(fila[3]),float(fila[4]))
                self.__lista_clientes.append(xcliente)
    def buscar_dni(self,xdni,aux=0):
        i=0
        while i<len(self.__lista_clientes) and self.__lista_clientes[i].get_dni()!=xdni:
            i+=1
        if i < len(self.__lista_clientes):
            if aux==0:
                print(f"cliente: {self.__lista_clientes[i].get_ap_nom()}                     numero de la cuenta: {self.__lista_clientes[i].get_numero_cuenta()}\nsaldo anterior: {self.__lista_clientes[i].get_sald()}")
            return self.__lista_clientes[i].get_numero_cuenta()
        else:
            print("el dni no se encontro")
    def actualizar_saldo(self,xdni,xsaldo):
        i=0
        while i<len(self.__lista_clientes) and self.__lista_clientes[i].get_dni()!=xdni:
            i+=1
        if i<len(self.__lista_clientes):
            self.__lista_clientes[i].act_saldo(xsaldo)
            print(f"saldo actualizado {self.__lista_clientes[i].get_sald()}")
    def mostrar_ap_nom(self,xdni):
        i=0
        while i<len(self.__lista_clientes) and self.__lista_clientes[i].get_dni()!=xdni:
            i+=1
        if i<len(self.__lista_clientes):
            print (f"el cliente {self.__lista_clientes[i]} tuvo movimientos en el mes de abril")    