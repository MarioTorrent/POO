from clase_coleccion import coleccion
def menu(xcoleccion):
    aux=1
    xcoleccion.cargar_csv()
    while aux !=5:
        try:
            aux=int(input("1_cantidad de pacientes hospitalizados con neumonia y cantidad de pacientes ambulatorios\n2_mostrar el importe cobrado por la clinica a cada paciente\n3_indicar que tipo de paciente se encuentra en la posicion buscada\n4_ingresar un nuevo valor por consulta\n5_salir\n"))
            assert aux<=5 and aux>=1,"ingrese una opcion valida"
            if aux==1:
                xcoleccion.item_B()
            elif aux==2:
                xcoleccion.importe_cobrado()
            elif aux==3:
                xpos=int(input("ingrese la posicion del paciente:\n"))
                xcoleccion.buscar_paciente(xpos)
            elif aux==4:
                xcoleccion.ingresar_nuevo_valor_por_consulta()
        except TypeError:
            print("ingrese un valor entero")
        except AssertionError as e:
            print(e)
        except IndexError:
            print("indice fuera de rango\n")
if __name__=="__main__":
    xcoleccion=coleccion()
    menu(xcoleccion)