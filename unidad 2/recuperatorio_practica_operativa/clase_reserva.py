class reserva:
    __num_reserva:int
    __nom_cliente:str
    __num_cabaña:int
    __fecha_inicio:str
    __cantidad_huespedes:int
    __cantidad_dias:int
    __imp_seña:float
    def __init__(self,xnumR,xnomC,xnumC,xfecha,xcantH,xcantD,ximp):
        self.__num_reserva=xnumR
        self.__nom_cliente=xnomC
        self.__num_cabaña=xnumC
        self.__fecha_inicio=xfecha
        self.__cantidad_huespedes=xcantH
        self.__cantidad_dias=xcantD
        self.__imp_seña=ximp
    def get_cab(self):
        return self.__num_cabaña
    def get_fecha(self):
        return self.__fecha_inicio
    def mostrar_datos(self,imp):
        print(f"{self.__num_cabaña}".center(15),f"{imp}".center(20),f'{self.__cantidad_dias}'.center(20),f'{self.__imp_seña}'.center(20),f'{(self.__cantidad_dias*imp)-self.__imp_seña}'.center(20))