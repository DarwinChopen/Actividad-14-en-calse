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

        case 2:
            print("Mostrar por edad")
        case 3:
            print("Mostrara por nomnre")
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion Invalida")