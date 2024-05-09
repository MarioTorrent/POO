class moto():
    __patente:str
    __marca:str
    __conductor:str
    __km:int
    def __init__(self,pat,marca,cond,km):
        self.__patente=pat
        self.__marca=marca
        self.__conductor=cond
        self.__km=km
    def mostrar_datos(self):
        print(f"patente de la moto:{self.__patente}\nmarca de la moto: {self.__marca}\nnombre del conductor: {self.__conductor}\nkm: {self.__km}")
    def get_conductor(self):
        return self.__conductor
    def get_pat(self):
        return self.__patente