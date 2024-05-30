class programa_capacitacion:
    __nombre:str
    __codigo:str
    __duracion:int
    __matriculas:list
    def __init__(self,nom,cod,duracion):
        self.__nombre=nom
        self.__codigo=cod
        self.__duracion=duracion
        self.__matriculas=[]
    def addmatricula(self,xmat):
        self.__matriculas.append(xmat)
    def get_nom(self):
        return self.__nombre
    def get_duracion(self):
        return self.__duracion