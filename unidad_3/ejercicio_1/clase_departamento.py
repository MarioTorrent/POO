class departamento:
    __id:int
    __nom_y_ap:str
    __num_piso:int
    __num_depto:int
    __cant_dorm:int
    __cant_banios:int
    __superficie:float
    def __init__(self,xid,xnom_y_ap,xnum_piso,xnum_depto,xcant_hab,xcant_banios,xsuperficie):
        self.__id=xid
        self.__nom_y_ap=xnom_y_ap
        self.__num_piso=xnum_piso
        self.__num_depto=xnum_depto
        self.__cant_dorm=xcant_hab
        self.__cant_banios=xcant_banios
        self.__superficie=xsuperficie
    def get_id(self):
        return self.__id
    def get_nom(self):
        return self.__nom_y_ap
    def get_sup(self):
        return self.__superficie
    def get_dormi(self):
        return self.__cant_dorm
    def get_num_piso(self):
        return self.__num_piso
    def get_banios(self):
        return self.__cant_banios