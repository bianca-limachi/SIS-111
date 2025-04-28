def nombre_funcion(): 
    print("salida de funcion")

def nombre_funcion2():
    print("salida de funcion 2")

#salida
nombre_funcion2()

def obtener_edad():
    edad = int(input("Indique su edad: "))
    if(edad > 0):
        return "Edad"
    else:
        return "Error solo numeros positivos"
    
def habilitado_brevet(hedad):
    if (hedad == 0): return "SOLO POSITIVOS"

    if(hedad >= 18):
        return "Verdadero:)"
    else:
        return "Falso :( "
#Salida consola
#var_edad = obtener_edad()
#var_habilitado = habilitado_brevet
#print(var_edad)

def calcular_descuento_producto():
    precio_original = 100
    descuento = 20
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento
    return precio_final

def calcular_descuento_producto_mejorado(precio_original, descuento):
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento


#var_precio_f = calcular_descuento_producto()
#print(var_precio_f)

precio_original = int(input("INGRESE EL PRECIO DEL PRODUCTO: "))
descuento = int(input("INGRESE EL % DE DESCUENTO DEL PRODUCTO: "))
var_precio_ff = calcular_descuento_producto_mejorado(precio_original, descuento)
print(var_precio_ff)

#1 Edad minima para votar
def edad_minima_votar():
    print("La edad minima es 18 años")

#2 Numero mayor
def mayor_dos_num(numA, numB):
        if(numA == numB): "IGUALES"

        if (numA > numB):
            return numA
        else:
            return numB
    
def mayor_dos_num_mejorado(numA,numB):
    if(numA == numB) : return "IGUALES"

    return numA if (numA > numB) else numB

        
var_numA = int(input("INGRESE EL NUMERO A: "))
var_numB = int(input("INGRESE EL NUMERO B: "))
var_num_mayor = mayor_dos_num(var_numA, var_numB)
print(var_num_mayor)

def recorrer_digitos(num):
    while(num>0):
        dig = num % 10
        print (dig)
        num=num//10

def par_impar_dig(num):
    while(num >0):
        dig = num %10
        print(dig)

        var_temp = "PAR" if (dig %2 == 0) else "Impar"
        print(var_temp)
        num = num //10

    def suma_dig_num(num):
        suma = 0
        while(num > 0):
            dig = num % 10
            suma = suma + dig
            num = num // 10
        return suma
    
var_suma = suma_dig_num(78234)
print(var_suma)
