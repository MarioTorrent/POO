from clase_nodo_dobl_enl import nodo
class lista:
    __cabeza:nodo
    __actual:nodo
    __iniciado:bool
    def __init__(self):
        self.__cabeza=None
        self.__actual=None
        self.__iniciado=None
    def agregar_final(self,xobj):
        nuevo_nodo=nodo(xobj)
        if not self.__cabeza:
            self.__cabeza=nuevo_nodo
            self.__cabeza.set_sig(self.__cabeza)
            self.__cabeza.set_ant(self.__cabeza)
        else:
            ultimo=self.__cabeza.get_ant()
            ultimo.set_sig(nuevo_nodo)
            nuevo_nodo.set_ant(ultimo)
            nuevo_nodo.set_sig(self.__cabeza)
            self.__cabeza.set_ant(nuevo_nodo)
    def __iter__(self):
        self.__actual=self.__cabeza
        self.__iniciado=False
        return self
    def __next__(self):
        if self.__cabeza is None or (self.__actual==self.__cabeza and self.__iniciado):
            raise StopIteration
        self.__iniciado=True
        dato=self.__actual.get_dato()
        self.__actual=self.__actual.get_sig()
        return dato
    def get_cabeza(self):
        return self.__cabeza
    def eliminar_segun_xatributo(self,xatributo):
        aux=self.__cabeza
        while True:
            if aux.get_dato().get_xatr()==xatributo:#cambiar el get_xatr por el atributo que se desea comparar
                break
            else:
                aux=aux.get_sig()
        aux.get_sig().set_ant(aux.get_ant())
        aux.get_ant().set_sig(aux.get_sig())