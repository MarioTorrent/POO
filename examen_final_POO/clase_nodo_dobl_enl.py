class nodo:
    __dato:object
    __sig:object
    __ant:object
    def __init__(self,xobj):
        self.__dato=xobj
        self.__sig=None
        self.__ant=None
    def get_dato(self):
        return self.__dato
    def set_sig(self,xnodo):
        self.__sig=xnodo
    def get_sig(self):
        return self.__sig
    def set_ant(self,xnodo):
        self.__ant=xnodo
    def get_ant(self):
        return self.__ant
    