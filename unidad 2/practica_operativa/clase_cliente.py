class cliente:
    __nombre:str
    __apellido:str
    __dni:str
    __numero_cuenta:int
    __saldo:float
    def __init__(self,xnom,xapellido,xdni,xnum,xsaldo):
        self.__nombre=xnom
        self.__apellido=xapellido
        self.__dni=xdni
        self.__numero_cuenta=xnum
        self.__saldo=xsaldo
    def get_dni(self):
        return self.__dni
    def get_numero_cuenta(self):
        return self.__numero_cuenta
    def get_sald(self):
        return self.__saldo
    def get_ap_nom(self):
        return self.__apellido+" "+self.__nombre
    def act_saldo(self,xsaldo):
        self.__saldo+=xsaldo
    def __str__(self):
        return self.__nombre+" "+self.__apellido