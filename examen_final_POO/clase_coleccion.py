from clase_lista_circular_dobl_enl import lista
from clase_cliente_nacional import cliente_nacional,cliente_local
class coleccion(lista):
    def __init__(self):
        super().__init__()
    def mostrar_clientes_nacionales(self):
        for xcliente in self:
            if isinstance (xcliente,cliente_nacional):
                print(f"nombre: {xcliente.get_nombre()}\nprovincia: {xcliente.get_prov()}\n\n")
    def mostrar_tipo_cliente(self,pos):
        if super().get_cabeza()==None:
            print("la lista esta vacia\n")
        else:
            aux=super().get_cabeza()
            i=1
            while i<pos:
                aux=aux.get_sig()
                i+=1
            if isinstance(aux.get_dato(),cliente_local):
                print(f"el tipo de cliente en la posicion {pos} es: cliente local\n")
            else:
                print(f"el tipo de cliente en la posicion {pos} es: cliente nacional\n")
