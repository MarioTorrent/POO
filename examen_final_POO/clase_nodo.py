class nodo:
    __cliente:object
    __sig:object
    def __init__(self, xcliente):
        self.__cliente=xcliente
        self.__sig=None
    def set_siguiente(self,siguiente):
        self.__sig=siguiente
    def get_siguiente(self):
        return self.__sig
    def get_dato(self):
        return self.__cliente