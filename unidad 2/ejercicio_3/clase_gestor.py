import numpy as np
class gestor_Ventas:
    __ventas=np.array
    #se inicia la una matriz de 5x7 en cero
    def __init__(self):
        self.__ventas=np.zeros((5,7))
    #se carga la matriz con los datos que recibe de una factura
    def registrar(self,dia,sucur,imp):
        self.__ventas[sucur,dia]+= imp
    #se calcula el total recaudado por una sucursal que recibe por parametros
    def total_sucur(self,sucur):
        return np.sum(self.__ventas[sucur])
    #se busca cual es la sucursal que mas recaudo en un dia que recibe por parametros
    def max_factu(self,dia):
        maxi=self.__ventas[:,dia]
        return np.max(maxi)
    #se busca cual es la sucursal que menos recaudo en la semana
    def min_factu(self):
        min=np.sum(self.__ventas[0])
        smin=0
        for i in range(1, 4):
            if min>np.sum(self.__ventas[i]):
                min=np.sum(self.__ventas[i])
                smin=i
        return smin+1
    #se calcula cual es el total recaudado por todas las sucursales
    def total(self):
        return np.sum(self.__ventas)