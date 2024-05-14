from clase_departamento import departamento
class edificio:
    __id:int
    __nom:str
    __dir:str
    __nom_constructora:str
    __cant_pisos:int
    __cant_deptos:int
    __deptos:list
    def __init__(self,xid,xnom,xdir,xnom_c,xcant_p,xcant_d):
        self.__id=xid
        self.__nom=xnom
        self.__dir=xdir
        self.__nom_constructora=xnom_c
        self.__cant_pisos=xcant_p
        self.__cant_deptos=xcant_d
        self.__deptos=[]
    def carga_deptos(self,xid,xnom_y_ap,xnum_piso,xnum_depto,xcant_hab,xcant_baños,xsuperficie):
        xdepto=departamento(xid,xnom_y_ap,xnum_piso,xnum_depto,xcant_hab,xcant_baños,xsuperficie)
        self.__deptos.append(xdepto)
    def get_nom(self):
        return self.__nom
    def mostrar_propietarios(self):
        for i in range(len(self.__deptos)):
            print(f"el propietario del departamento numero {self.__deptos[i].get_id()} es: {self.__deptos[i].get_nom()}\n")
    def get_sup_total(self):
        total=0
        for i in range (len(self.__deptos)):
            total+=self.__deptos[i].get_sup()
        return total
    def get_sup_depto(self,xnom):
        for xdepto in self.__deptos:
            if xnom==xdepto.get_nom():
                sup_total=self.get_sup_total()
                sup_depto=xdepto.get_sup()
                print(f"la superficie total cubierta de su departamento es: {sup_depto}\n y el porcentaje que representa de la superficie total del edificio es: {(sup_depto*100)/sup_total}%")
    def golden_deptos(self,xpiso,cont):
        for xdepto in self.__deptos:
            if xpiso==xdepto.get_num_piso() and xdepto.get_dormi()==3 and xdepto.get_banios()>1:
                cont+=1
        return cont