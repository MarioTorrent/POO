class cliente_local:
    __nombre:str
    __apellido:str
    __email:str
    __contraseña:str
    __dir_postal:str
    __telefono:int
    def __init__(self,xnom,xapellido,xemail,xcontraseña,xdir_postal,xtel):
        self.__nombre=xnom
        self.__apellido=xapellido
        self.__email=xemail
        self.__contraseña=xcontraseña
        self.__dir_postal=xdir_postal
        self.__telefono=xtel
    def get_nombre(self):
        return self.__nombre