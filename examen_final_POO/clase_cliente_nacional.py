from clase_cliente_local import cliente_local
class cliente_nacional(cliente_local):
    __provincia:str
    __localidad:str
    __cod_postal:int
    def __init__(self, xnom, xapellido, xemail, xcontraseña, xdir_postal, xtel,xprov,xloc,xcod_postal):
        super().__init__(xnom, xapellido, xemail, xcontraseña, xdir_postal, xtel)
        self.__provincia=xprov
        self.__localidad=xloc
        self.__cod_postal=xcod_postal
    def get_prov(self):
        return self.__provincia
    def get_nombre(self):
        return super().get_nombre()