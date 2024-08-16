from clase_nodo import nodo
class lista:
    __comienzo:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope=0
        self.__indice=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.get_dato()
            self.__actual=self.__actual.get_siguiente()
            return dato
    def agregar(self,xobj):
        xnodo=nodo(xobj)
        xnodo.set_siguiente(self.__comienzo)
        self.__comienzo=xnodo
        self.__actual=xnodo
        self.__tope+=1
    def agregar_al_final(self,xobj):
        xnodo=nodo(xobj)
        aux=self.__comienzo
        if self.__comienzo==None:
            self.__comienzo=xnodo
            self.__actual=xnodo
            self.__tope+=1
        else:
            while aux.get_siguiente()!=None:
                aux=aux.get_siguiente()
            aux.set_siguiente(xnodo)
            self.__tope+=1
    def get_tope(self):
        return self.__tope
    def get_comienzo(self):
        return self.__comienzo