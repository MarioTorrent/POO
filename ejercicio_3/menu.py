from clase_gestor import gestor_Ventas
def menu():
    xgestor=gestor_Ventas()
    aux=1
    while aux!=0:
        factura=[]
        #se ingresa por teclado un numero que indica la opcion elegida del menu
        aux=int(input("1. cargar factura \n2. calcular total de facturacion de una sucursal \n3. obtener la sucursal que mas facturo en un dia \n4. calcular la sucursal que menos facturo en la semana \n5. total facturad por todas las sucursales \n6. cerrar programa \n"))
        if(aux==1):
            #se carga los datos de una venta en la lista "factura"
            factura.append(int(input("ingrese dia de la semana: \n")))
            factura.append(int(input("ingrese numero de la sucursal:\n")))
            factura.append(float(input("ingrese importe: \n")))
            #se envian los datos de la factura para ser cargados en un gestor de ventas
            xgestor.registrar(factura[0]-1,factura[1]-1,factura[2])
        elif(aux==2):
            #se ingresa por teclado el numero de una sucursal y se muestra por pantalla el total recaudado por dicha sucursal
            sucur=int(input("ingrese el numero de la sucursal: \n"))
            print(f"el total recaudado de la sucursal {sucur} es: {xgestor.total_sucur(sucur-1)}\n")
        elif(aux==3):
            #se ingresa por teclado un dia y se muestra por pantalla cual fue la sucursal que mas recaudo dicho dia
            xdia=int(input("ingrese el dia de la semana: \n"))
            print(f"la sucursal que mas facturo el dia {xdia} es la sucursal {xgestor.max_factu(xdia-1)} \n")
        elif(aux==4):
            #se muestra por pantalla cual es la sucursal que menos recaudo en la semana
            print(f"la sucursal que menos facturo en la semana es: {xgestor.min_factu()}\n")
        elif(aux==5):
            #se muestra por pantalla el total recaudado en la semana
            print(f"el total facturado por todas las sucursales es: {xgestor.total()}\n")
        elif(aux==6):
            return ()
        else :
            #se muestra por pantalla un mensaje de error y se pide ingresar nuevamente una opcion del menu
            print("error")
            aux=int(input("1. cargar factura \n2. calcular total de facturacion de una sucursal \n3. obtener la sucursal que mas facturo en un dia \n4. calcular la sucursal que menos facturo en la semana \n5. total facturad por todas las sucursales \n6. cerrar programa"))
#se llama a la funcion "menu" cuando inicia el programa 
if __name__=="__main__":
    menu()