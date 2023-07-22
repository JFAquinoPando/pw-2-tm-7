""" El programa debe emitir los siguientes datos: 

Suma total, Cantidad de numeros impares, y un mensaje que indique si existen números superiores a 100 """

def incrementar(valor_actual, incremento):
    return valor_actual + incremento

def decrementar(valor_actual, decremento):
    return valor_actual - decremento

superior_100 = 0
cantidad_impar = 0
numero1 = int(input("Ingresa un valor: "))
numero2 = int(input("Ingresa un valor: "))
numero3 = int(input("Ingresa un valor: "))
numero4 = int(input("Ingresa un valor: "))
numero5 = int(input("Ingresa un valor: "))


suma = numero3 + numero1 + numero2 + numero4 + numero5


if numero1 > 100:
    superior_100 = incrementar(superior_100,1)

if numero2 > 100:
    superior_100 = incrementar(superior_100,1)

if numero3 > 100:
    superior_100 = incrementar(superior_100,1)

if numero4 > 100:
    superior_100 = incrementar(superior_100,1)

if numero5 > 100:
    superior_100 = incrementar(superior_100,1)



if numero1 % 2 != 0:
    cantidad_impar = incrementar(cantidad_impar,1)

if numero2 % 2 != 0:
    cantidad_impar = incrementar(cantidad_impar,1)

if numero3 % 2 != 0:
    cantidad_impar = incrementar(cantidad_impar,1)

if numero4 % 2 != 0:
    cantidad_impar = incrementar(cantidad_impar,1)

if numero5 % 2 != 0:
    cantidad_impar = incrementar(cantidad_impar,1)

print("La suma total es de: ", suma)
print("La cantidad de numeros impares es de: ", cantidad_impar)
print("La cantidad de numeros mayores a 100 es de: ", superior_100)
if(superior_100 > 0):
    print("Existen numeros superiores a 100")
else:
    print("No existen numeros mayoresa 100")



