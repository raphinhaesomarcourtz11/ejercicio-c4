#definimos una funcion suma
def suma (x, y):
    resultado= x,y
    return resultado
print("el resultado es",suma(4,5))




#esto es una funcion que nos calcula el siguiente
def siguiente(resultado):
    resultado = resultado+1
    return resultado
print("el resultado es",siguiente(41))



#esto es una funcion que recibe tres numeros y te devuelve el mayor de los tres
def mayor(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b  
        else:
            return c              
print("el mayor de tres",mayor(11,25,28))

