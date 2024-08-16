from clase_paciente import paciente
class paciente_ambulatorio(paciente):
    __historial_med:str
    __alergias:str
    __obra_social:str
    def __init__(self, nom, ap, email, num,historial_m,alergias,obra_social):
        super().__init__(nom, ap, email, num)
        self.__historial_med=historial_m
        self.__alergias=alergias
        self.__obra_social=obra_social
    def calculo_importe(self):
        if self.__obra_social=="Obra Social Provincia":
            plus=5000
        elif self.__obra_social=="Obra Social OSDE":
            plus=2000
        else:
            plus=10000
        return self._valor_consulta-self.get_valor_C()+plus