"""
Hacer un programa que imprima y cuente los múltiplos de 3 que hay entre el 0 y el 20
"""

def imprimir_resultado(cantidad):
    print("La cantidad de multiplos de 3 es de:",cantidad)

def incrementar(valor_actual, incremento):
    return valor_actual + incremento

inicio = 0
fin = 20
contador = 0
multiplos3 = []
while(inicio <= fin):
    if inicio % 3 == 0:
        print("numero:",inicio)
        #contador = contador + 1
        multiplos3.append(inicio)
    inicio = incrementar(inicio,1)

imprimir_resultado(len(multiplos3))