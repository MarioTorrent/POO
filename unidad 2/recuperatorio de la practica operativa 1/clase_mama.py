class mama:
    __dni:int
    __edad:int
    __apellido_y_nom:str
    def __init__(self,xdni,xedad,xnom):
        self.__dni=int(xdni)
        self.__edad=int(xedad)
        self.__apellido_y_nom=xnom
    def __str__(self):
        return f"Apellido y nombre: {self.__apellido_y_nom}\nEdad: {self.__edad}"
    def get_dni(self):
        return self.__dni