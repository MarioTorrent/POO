class caja_de_ahorro:
    __nro_cuenta:str
    __cuil:str
    __apellido:str
    __nombre:str
    __saldo:float
    def __str__(self):
        return f"el numero de cuenta es: {self.__nro_cuenta} \ncuil:{self.__cuil}\napelllido: {self.__apellido}\nnombre: {self.__nombre}\nsaldo: {self.__saldo}\n"
    def __init__(self, xnum, xcuil, xapellido, xnombre, xsaldo):
        self.__nro_cuenta=xnum
        self.__cuil=xcuil
        self.__apellido=xapellido
        self.__nombre=xnombre
        self.__saldo = xsaldo
    def mostrar_datos(self):
        print(f"el numero de cuenta es: {self.__nro_cuenta} \ncuil:{self.__cuil}\napelllido: {self.__apellido}\nnombre: {self.__nombre}\nsaldo: {self.__saldo}")
    def extraer(self,importe):
        if(self.__saldo>=importe):
            self.__saldo-=importe
            print("el nuevo saldo es: ",self.__saldo)
        else:
            print("su saldo es negativo, el saldo faltante es: ", importe-self.__saldo)
            self.__saldo-=importe
    def depositar(self, importe):
        if importe>=0:
            print("el importe es positivo")
            self.__saldo+=importe
        else: 
            print("el importe no es positivo")
    def obtenerCUIL(self):
        return self.__cuil
    def verificar_cuil(cuil):
        # Verificar que el CUIL tenga 11 dígitos
        if len(cuil) != 11:
            return False

        # Extraer los componentes del CUIL
        xy = cuil[:2]
        dni = cuil[2:10]
        z = int(cuil[10])

        # Calcular la suma de multiplicaciones
        suma = 0
        for i, digito in enumerate(dni):
            peso = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2][i]
            suma += int(digito) * peso

        # Calcular el resto de la división por 11
        resto = suma % 11

        # Determinar el valor de Z
        if resto == 0:
            z_calculado = 0
        elif resto == 1:
            if xy == "20" or xy == "27":
                z_calculado = 9
            else:
                z_calculado = 4
        else:
            z_calculado = 11 - resto

        # Verificar si Z coincide con el valor calculado
        return z == z_calculado
