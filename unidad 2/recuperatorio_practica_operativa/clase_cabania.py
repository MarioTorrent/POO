class cabania:
    __num:int
    __cant_hab:int
    __cant_camasG:int
    __cant_camasC:int
    __import_dia:float
    __reserva:bool
    def __init__(self,xnum,xhab,xcamG,xcamC,ximp):
        self.__num=xnum
        self.__cant_hab=xhab
        self.__cant_camasC=xcamC
        self.__cant_camasG=xcamG
        self.__import_dia=ximp
        self.__reserva=False
    def __ge__(self,n):
        return self.get_capacidad()>=n
    def get_capacidad(self):
        return (self.__cant_camasG*2)+self.__cant_camasC
    def get_num(self):
        return self.__num
    def reservar(self):
        self.__reserva=True
    def get_num(self):
        return self.__num
    def get_reserva(self):
        return self.__reserva
    def get_imp(self):
        return self.__import_dia