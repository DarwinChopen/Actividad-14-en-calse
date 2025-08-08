def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
participoantes={}
while True:
    print("Menu")
    print("1.Ingreso")
    print("2. Mostar Por Edad")
    print("3. Mostar por Nombre")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ingreso")
            cantidad = int(input("¿Cuántos participantes desea ingresar? "))
            for i in range(cantidad):
                print(f"\nparticipante #{i + 1}")
                while True:
                   dorsal = int(input("Ingrese el número de dorsal: "))
                   if dorsal in participoantes:
                       print("Este dorsal ya existe Ingrese otro")
                   else:
                       break
                participoantes[dorsal] = {}
                participoantes[dorsal]["nombre"] = input("Ingrese el nombre: ")
                participoantes[dorsal]["edad"] = int(input("Ingrese la edad: "))
                participoantes[dorsal]["categoria"] = input("Ingrese la categoria: ")
        case 2:
            print("Mostrar por edad")
        case 3:
            print("Mostrara por nomnre")
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion Invalida")