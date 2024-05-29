class nacimiento:
    __dni_mama:int
    __tipo_de_parto:str
    __fecha:str
    __hora:str
    __peso:str
    __altura:int
    def __init__(self,xdni,xtipo,xfecha,xhora,xpeso,xaltura):
        self.__dni_mama=int(xdni)
        self.__tipo_de_parto=xtipo
        self.__fecha=xfecha
        self.__peso=xpeso
        self.__altura=int(xaltura)
        self.__hora=xhora
    def __str__(self):
        return f"{self.__peso}      {self.__altura}"
    def get_dni(self):
        return self.__dni_mama
    def get_tipo(self):
        return self.__tipo_de_parto
    def get_fecha(self):
        return self.__fecha
    def __eq__(self,xnacimiento):
        return self.__fecha == xnacimiento.get_fecha()