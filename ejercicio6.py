"""
Introducir por teclado tantas frases como se deseen y contarlas.
"""
def imprimir_resultado(cantidad):
    if cantidad == 0:
        print("No hay frases")
    else:
        print("La cantidad de frases es de",cantidad)

frases = []
frase = input("Ingrese su frase: ")

while(frase != ''):
    frases.append(frase)
    frase = input("Ingrese su frase: ")

imprimir_resultado(len(frases))



