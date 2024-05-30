class empleado:
    __Nombre_Y_Apellido:str
    __id_emp:int
    __Puesto:str
    __matriculas:list
    def __init__(self,nom,id,puesto):
        self.__Nombre_Y_Apellido=nom
        self.__id_emp=id
        self.__Puesto=puesto
        self.__matriculas=[]
    def __str__(self):
        return f"---------------------------------\nnombre y apellido: {self.__Nombre_Y_Apellido}\nid: {self.__id_emp}\nPuesto: {self.__Puesto}\n---------------------------------"
    def addmatricula(self,xmat):
        self.__matriculas.append(xmat)
    def get_id(self):
        return self.__id_emp