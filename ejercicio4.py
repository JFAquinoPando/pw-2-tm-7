"""
Hacer un programa que imprima los números impares entre el 10 y el cero en orden decreciente y que calcule la suma de esos números impares.
"""

def imprimir(dato):
    print(dato)

def imprimir_suma(total):
    print("El total es de:", total)

def decrementar(valor_actual, decremento):
    return valor_actual - decremento

def incrementar(valor_actual, incremento):
    return valor_actual + incremento

inicio = 10
fin = 0
suma = 0
while inicio >= fin:
    if (inicio % 2 != 0):
        imprimir(inicio)
        suma = incrementar(suma, inicio)
    inicio = decrementar(inicio,1)
imprimir_suma(suma)
    
