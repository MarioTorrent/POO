from caja import caja_de_ahorro
class lista_caja:
    __cajas:list
    __xcajita:caja_de_ahorro
    def __init__(self):
        self.__cajas=[]
    def carga_lista(self):
        xcajita=caja_de_ahorro(input("ingrese numero de la cuenta: \n"),input("ingrese numero de cuil: \n"),input("ingrese apellido: \n"),input("ingrese nombre: \n"),input("ingrese saldo de la cuenta: \n"))
        self.__cajas.append(xcajita)
    def mostrar_lista(self):
        for caja in self.__cajas:
            print(caja)
    def obtenerDatos(self):
        i=0
        cuilb=input("ingrese el cuil de la caja de ahorro que desea buscar: ")
        while (i <= (len(self.__cajas))) and (cuilb!=self.__cajas[i].obtenerCUIL()):
            i+=1
        if cuilb==self.__cajas[i].obtenerCUIL():
            return self.__cajas[i]
        else: 
            print("el cuil ingresado no pertenece a ninguna de las cajas de ahorro registradas")