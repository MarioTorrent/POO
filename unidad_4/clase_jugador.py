class jugador():
    __nombre:str
    __puntos:int
    __fecha:str
    __hora:str
    def __str__(self):
        return f"{self.__nombre}".center(25)+f"{self.__puntos}".center(25)+f"{self.__fecha}".center(25)+f"{self.__hora}".center(25)
    def __init__(self,nom,puntos,fecha,hora):
        self.__nombre=nom
        self.__puntos=puntos
        self.__fecha=fecha
        self.__hora=hora
    def __gt__(self,otro):
        return self.__puntos>otro.get_puntos()
    def get_puntos(self):
        return self.__puntos