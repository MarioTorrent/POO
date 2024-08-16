class nodo:
    __xobjeto:object
    __sig:object
    def __init__(self, xobj):
        self.__xobjeto=xobj
        self.__sig=None
    def set_siguiente(self,siguiente):
        self.__sig=siguiente
    def get_siguiente(self):
        return self.__sig
    def get_dato(self):
        return self.__xobjeto