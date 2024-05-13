
from clase_gestor_edificios import gestor_edificios
def menu():
    edificios=gestor_edificios()
    aux=1
    while aux!=0:
        aux=int(input("1-cargar edificios desde archi\n2_mostrar los propietarios de los departamentos de un edificio\n3_mostrar la superficie total cubierta de un edificio \n4_mostrar la superficie del depto de un propietario\n5_contar y mostrar la cantidad de deptos que tienen 3 dormitorios y mas de un baño en un piso\n6_fin\n"))
        if aux==1:
            edificios.carga_archi()
        elif aux==2:
            xnom=input("ingrese el nombre del edificio:\n")
            edificios.mostar_propietarios_edificio(xnom)
        elif aux==3:
            xnom2=input("ingrese nombre del edificio:\n")
            edificios.mostrar_sup_edificio(xnom2)
        elif aux==4:
            xnom_prop=input("ingrese nombre del propietario:\n")
            edificios.sup_depto_prop(xnom_prop)
        elif aux==5:
            xpiso=int(input("ingrese el numero del piso:\n"))
            edificios.golden_deptos_piso(xpiso)
        elif aux==6:
            return()
if __name__=="__main__":
    menu()