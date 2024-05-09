class movimiento:
    __numero_cuenta:int
    __fecha:str
    __descripcion:str
    __tipo_movimiento:str
    __importe:float
    def __init__(self,xnum,xfecha,xdescripcion,xtipo,ximp):
        self.__numero_cuenta=xnum
        self.__fecha=xfecha
        self.__descripcion=xdescripcion
        self.__tipo_movimiento=xtipo
        self.__importe=ximp
    def get_num_cuenta(self):
        return self.__numero_cuenta
    def get_tipo(self):
        return self.__tipo_movimiento
    def get_imp(self):
        return self.__importe
    def __str__(self):
        return f"{self.__fecha}          {self.__descripcion}              {self.__importe}               {self.__tipo_movimiento}"
    def __lt__(self,xmov):
        return self.__numero_cuenta<xmov.get_num_cuenta()