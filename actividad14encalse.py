def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
participantes={}
while True:
    print("Menu")
    print("1.Ingreso")
    print("2. Mostar Por Nombre")
    print("3. Mostar por Edad")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ingreso")
            cantidad = int(input("Ingrese cuantos participantes va a ingresar? "))
            for i in range(cantidad):
                print(f"\nparticipante #{i + 1}")
                while True:
                   dorsal = int(input("Ingrese el número de dorsal: "))
                   if dorsal in participantes:
                       print("Este dorsal ya existe Ingrese otro")
                   else:
                       break
                participantes[dorsal] = {}
                participantes[dorsal]["nombre"] = input("Ingrese el nombre: ")
                participantes[dorsal]["edad"] = int(input("Ingrese la edad: "))
                participantes[dorsal]["categoria"] = input("Ingrese la categoria: ")
        case 2:
            print("Mostrar por edad")
            listaEdad = [(var, datos["edad"]) for var, datos in participantes.items()]
            listaOrdenada = quick_sort(listaEdad)
            for dorsal, _ in listaOrdenada:
                datos = participantes[dorsal]
                print(f"Dorsal: {dorsal}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Edad: {datos["edad"]}")
                print(f"Categoria: {datos["categoria"]}")
        case 3:
            print("Mostrara por nombre")
            listaNombre = [(var, datos["nombre"]) for var, datos in participantes.items()]
            listaOrdenada = quick_sort(listaNombre)
            for dorsal, _ in listaOrdenada:
                datos = participantes[dorsal]
                print(f"Dorsal: {dorsal}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Edad: {datos["edad"]}")
                print(f"Categoria: {datos["categoria"]}")
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion Invalida")