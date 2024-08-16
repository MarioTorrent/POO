from clase_coleccion import coleccion, cliente_nacional, cliente_local
def test(xcoleccion):
    cliente1=cliente_local("Mario","Torrent","mnt2610@gmail.com","password123","xdir-55",2646277207)
    cliente2=cliente_nacional("Nahuel","Diaz","mntd2610@gmail.com","contraseña321","xdir-66",2645277205,"san juan","media agua",5435)
    xcoleccion.agregar_final(cliente1)
    xcoleccion.agregar_final(cliente2)
    print("los cliente nacionales son:\n")
    xcoleccion.mostrar_clientes_nacionales()
    xcoleccion.mostrar_tipo_cliente(1)
def menu(xcoleccion):
    try:
        aux=int(input("1_ejecutar test\n2_registrar clienete\n3_mostrar nombre de los clientes nacionales y sus provincias\n4_mostrar que tipo de cliente se encuentra en una posicion\n5_salir\n"))
    except ValueError:
        print("ingrese un valor entero por favor")
    while aux !=5:
        if aux==1:
            test(xcoleccion)
        elif aux==2:
            try:    
                tipo_cliente=int(input("ingrese el tipo de cliente que se va a registrar(1_cliente local o 2_cliente nacional):\n"))
                assert tipo_cliente<=2 and tipo_cliente>=1,"el tipo de cliente solo puede ser 1 o 2"
                nom=input("ingrese nombre:\n")
                apellido=input("ingrese apellido:\n")
                correo=input("ingrese correo electronico:\n")
                contraseña=input("ingrese contraseña:\n")
                dir_post=input("ingrese direccion postal:\n")
                num=input("ingrese numero telefonico:\n")
                if tipo_cliente==1:
                    xcliente=cliente_local(nom,apellido,correo,contraseña,dir_post,num)
                    xcoleccion.agregar_final(xcliente)
                elif tipo_cliente==2:
                    prov=input("ingrese provincia del cliente:\n")
                    localidad=input("ingrese localidad del cliente:\n")
                    cod_post=input("ingrese codigo postal del cliente:\n")
                    xcliente=cliente_nacional(nom,apellido,correo,contraseña,dir_post,num,prov,localidad,cod_post)
                    xcoleccion.agregar_final(xcliente)
            except ValueError:
                print("ingrese un valor entero por favor")
            except AssertionError as e:
                print(e)
        elif aux==3:
            print("los cliente nacionales son:\n")
            xcoleccion.mostrar_clientes_nacionales()
        elif aux==4:
            try:
                aux2=int(input("ingrese la posicion del cliente en la lista:\n"))
                xcoleccion.mostrar_tipo_cliente(aux2)
            except ValueError:
                print("ingrese un valor entero")
        else:
            print("ingrese una opcion valida\n")
        try:
            aux=int(input("1_ejecutar test\n2_registrar clienete\n3_mostrar nombre de los clientes nacionales y sus provincias\n4_mostrar que tipo de cliente se encuentra en una posicion\n5_salir\n"))
        except ValueError:
            print("ingrese un valor entero por favor")
if __name__=="__main__":
    xcoleccion=coleccion()
    menu(xcoleccion)