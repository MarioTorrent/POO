
class paciente():
    __nombre:str
    __apellido:str
    __email:str
    __num_tel:int
    _valor_consulta=15000
    def __init__(self,nom,ap,email,num):
        self.__nombre=nom
        self.__apellido=ap
        self.__email=email
        self.__num_tel=int(num)
    def calculo_importe(self):
        pass
    def get_nom(self):
        return self.__nombre
    def get_ap(self):
        return self.__apellido
    @classmethod
    def modificar_valor_consulta(cls):
        cls._valor_consulta=float(input("ingrese el nuevo valor de consulta: \n"))
    def get_valor_C(self):
        return self._valor_consulta