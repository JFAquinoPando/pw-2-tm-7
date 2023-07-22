def saludar(nombre='Anonimo'):
    if nombre == 'Anonimo' or nombre == '':
        print("Por favor carga un nombre")
    else:
        print("Hola me llamo ",nombre," y vos?")
persona = input("Por favor ingresa tu nombre: ")
saludar(persona)