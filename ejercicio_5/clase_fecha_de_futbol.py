class fecha_de_futbol:
    __fecha_partido:str
    __id_local:int
    __id_visitante:int
    __goles_local:int
    __goles_visitante:int
    def __init__(self,fecha,id_L,id_V,golesL,golesV):
        self.__fecha_partido=fecha
        self.__id_local=id_L
        self.__id_visitante=id_V
        self.__goles_local=golesL
        self.__goles_visitante=golesV
    def obtener_datos(self):
        return self.__id_local,self.__id_visitante,self.__goles_local,self.__goles_visitante
    def obtener_id(self):
        return self.__id_local,self.__goles_visitante
    def datos_equipo(self,id):
        if id==self.__id_local:
            if self.__goles_local>self.__goles_visitante:
                punt=3
            elif self.__goles_local==self.__goles_visitante:
                punt=1
            else:
                punt=0
            print (f"{self.__fecha_partido}    {self.__goles_local}          {self.__goles_visitante}            {punt}\n")
        elif id==self.__id_visitante:
            if self.__goles_local<self.__goles_visitante:
                punt=3
            elif self.__goles_local==self.__goles_visitante:
                punt=1
            else:
                punt=0
            print (f"{self.__fecha_partido}    {self.__goles_visitante}          {self.__goles_local}            {punt}\n")
            