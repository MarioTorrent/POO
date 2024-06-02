from abc import ABC,abstractmethod
class publicacion(ABC):
    __titulo:str
    __categoria:str
    __precio_base:float
    def __init__(self,titulo,categoria,precio_base):
        self.__titulo=titulo
        self.__categoria=categoria
        self.__precio_base=precio_base
    @abstractmethod
    def datos(self):
        pass