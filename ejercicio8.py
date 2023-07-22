""" Ingresar 5 numeros por teclado y al final de los mismos, 

el programa debe emitir los siguientes datos: 

Suma total, Cantidad de numeros impares, y un mensaje que indique si existen números superiores a 100 """

def incrementar(valor_actual, incremento):
    return valor_actual + incremento

def decrementar(valor_actual, decremento):
    return valor_actual - decremento


cantidad = 5
numeros = []
suma = 0
cant_impares = 0
superior_100 = 0
while (cantidad > 0):
    numero = int(input("Ingresa un numero, por favor: "))
    numeros.append(numero)
    cantidad =  decrementar(cantidad, 1)#cantidad - 1


print("Lo que hay: ", numeros)

contador = 0
while(contador < len(numeros)):
    suma = incrementar(suma, numeros[contador])
    if numeros[contador] % 2 != 0:
        cant_impares = incrementar(cant_impares, 1)
    if numeros[contador] > 100:
        superior_100 = incrementar(superior_100, 1)
    contador = incrementar(contador, 1)
print("La suma total es de:", suma)
print("La cantidad de impares es de:", (cant_impares))
print("La cantidad de numeros mayores a 100 es de:", (superior_100))
