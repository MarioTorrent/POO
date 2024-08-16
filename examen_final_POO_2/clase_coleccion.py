from clase_lista import lista
from clase_paciente_ambulatorio import paciente_ambulatorio,paciente
from clase_paciente_hospitalizado import paciente_hospitalizado
import csv
class coleccion(lista):
    def __init__(self):
        super().__init__()
    def cargar_csv(self):
        archi=open("pacientes.csv")
        reader=csv.reader(archi,delimiter=";")
        next(reader)
        for f in reader:
            if f[0]=="P":
                nuevo_paciente=paciente(f[1],f[2],f[3],f[4])
            elif f[0]=="O":
                nuevo_paciente=paciente_ambulatorio(f[1],f[2],f[3],f[4],f[5],f[6],f[7])
            elif f[0]=="H":
                nuevo_paciente=paciente_hospitalizado(f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9])
            super().agregar_al_final(nuevo_paciente)
    def item_B(self):
        cont_neumonia=0
        cont_ambulatorios=0
        for p in self:
            if isinstance(p,paciente_hospitalizado):
                if p.get_diagnostico()=="Neumonia":
                    cont_neumonia+=1
            if isinstance(p,paciente_ambulatorio):
                cont_ambulatorios+=1
        print(f"la cantidad de pacientes hospitalizados con neumonia es: {cont_neumonia}\nla cantidad de pacientes ambulatorios es: {cont_ambulatorios}\n")
    def importe_cobrado(self):
        for p in self:
            if isinstance(p,paciente_ambulatorio) or isinstance(p,paciente_hospitalizado):
                print(f"\npaciente: {p.get_nom()} {p.get_ap()} importe a pagar: ${p.get_valor_C()+p.calculo_importe()}\n")
            else:
                print(f"\npaciente: {p.get_nom()} {p.get_ap()} importe a pagar: ${p.get_valor_C()}\n")
    def buscar_paciente(self,pos):
        if pos<=super().get_tope():
            i=0
            aux=super().get_comienzo()
            while i!=pos:
                aux=aux.get_siguiente()
                i+=1
            aux=aux.get_dato()
            if isinstance(aux,paciente_ambulatorio):
                print("\nen esta posicion de la coleccion la componente es de tipo paciente ambulatorio con obra social\n")
            elif isinstance(aux,paciente_hospitalizado):
                print("\nen esta posicion de la coleccion la componente es de tipo paciente hospitalizado\n")
            else:
                print("\nen esta posicion de la coleccion la componente es de tipo paciente\n")
        else:
            raise IndexError
    def ingresar_nuevo_valor_por_consulta(self):
        super().get_comienzo().get_dato().modificar_valor_consulta()
    