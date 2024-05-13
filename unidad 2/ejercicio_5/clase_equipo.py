class equipo:
    __id:int
    __nombre:str
    __goles_a_favor:int
    __goles_en_contra:int
    __diferencia_goles:int
    __puntos:int
    def __str__(self):
        return f"id:{self.__id}    nom:{self.__nombre}    goles a favor:{self.__goles_a_favor}    goles en contra:{self.__goles_en_contra}   dif. goles:{self.__diferencia_goles}    puntos:{self.__puntos}\n"
    def __init__(self,id,nom,golesF,golesC,puntos):
        self.__id=id
        self.__nombre=nom
        self.__goles_a_favor=golesF
        self.__goles_en_contra=golesC
        self.__diferencia_goles=golesF-golesC
        self.__puntos=puntos
    def obtener_nombre(self):
        return self.__nombre
    def obtener_id(self):
        return self.__id
    def actualizar_datos(self,golesF,golesC,puntos):
        self.__goles_a_favor+=golesF
        self.__goles_en_contra+=golesC
        self.__diferencia_goles=(self.__goles_a_favor - self.__goles_en_contra)
        self.__puntos+=puntos
    def __gt__(self,xequipo):
        if self.__puntos!=xequipo.__puntos:
            return self.__puntos>xequipo.__puntos
        elif self.__diferencia_goles!=xequipo.__diferencia_goles:
            return self.__diferencia_goles>xequipo.__diferencia_goles
        else:
            return self.__goles_a_favor>xequipo.__goles_a_favor