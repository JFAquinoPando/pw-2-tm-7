lista = [1,2,3,4,5,True, False, "Texto", 41, 147, "otro valor"]
lista.append("valor agregado")

posicion = 11

print("La cantidad de elementos es", len(lista))
print("Estoy en posicion",posicion,":",lista[posicion])
print("listado actual:", lista)
print(lista.pop())
print("listado nuevo:", lista)
lista.reverse()
print("listado en reversa:", lista)
lista.remove('Texto')
print("listado sin texto:", lista)