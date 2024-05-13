class pedido():
    __patente_moto:str
    __id_pedido:str
    __comida:str
    __tiempo_estimado:int
    __tiempo_R_entrega:int
    __precio_pedido:float
    def __init__(self,patm,id,comida,estimado,t_real,precio):
        self.__patente_moto=patm
        self.__id_pedido=id
        self.__comida=comida
        self.__tiempo_estimado=estimado
        self.__tiempo_R_entrega=t_real
        self.__precio_pedido=precio
    def getid(self):
        return self.__id_pedido
    def mod_tiempo_real(self,xtiempo):
        self.__tiempo_R_entrega=xtiempo
    def get_patente(self):
        return self.__patente_moto
    def get_tiempo_real(self):
        return self.__tiempo_R_entrega
    def get_estimado(self):
        return self.__tiempo_estimado
    def get_precio(self):
        return self.__precio_pedido
    def __lt__(self,xpedido):
        return self.__patente_moto<xpedido.get_patente()