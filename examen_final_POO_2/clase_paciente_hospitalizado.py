from clase_paciente import paciente
class paciente_hospitalizado(paciente):
    __num_hab:int
    __fecha_ingreso:str
    __diagnostico:str
    __cant_dias_internacion:int
    __importe_descartables:float
    def __init__(self, nom, ap, email, num,num_hab,fecha_ing,diagnostico,cant_dias_internacion,imp_descartables):
        super().__init__(nom, ap, email, num)
        self.__num_hab=num_hab
        self.__fecha_ingreso=fecha_ing
        self.__diagnostico=diagnostico
        self.__cant_dias_internacion=int(cant_dias_internacion)
        self.__importe_descartables=float(imp_descartables)
    def calculo_importe(self):
        aux=self.__cant_dias_internacion*150000+self.__importe_descartables
        return self._valor_consulta+aux
    def get_diagnostico(self):
        return self.__diagnostico