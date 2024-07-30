from clase_coleccion import coleccion, cliente_nacional, cliente_local
def test(xcoleccion):
    cliente1=cliente_local("Mario","Torrent","mnt2610@gmail.com","password123","xdir-55",2646277207)
    cliente2=cliente_nacional("Nahuel","Diaz","mntd2610@gmail.com","contraseña321","xdir-66",2645277205,"san juan","media agua",5435)
    xcoleccion.agregar_al_final(cliente1)
    xcoleccion.agregar_al_final(cliente2)
    print("los cliente nacionales son:\n")
    xcoleccion.mostrar_clientes_nacionales()
    xcoleccion.mostrar_tipo_cliente(1)
if __name__=="__main__":
    xcoleccion=coleccion()
    test(xcoleccion)