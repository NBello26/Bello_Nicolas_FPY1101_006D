#Menu del programa

flag = True
while flag:
    print("-------------Opciones Productos-------------")
    print("1.- Agregar un producto")
    print("2.- Ver todos los productos")
    print("3.- Modificar un producto")
    print("4.- Elimina un producto")
    print("5.- Guardar coleccion en un archivo")
    print("6-. Salir del programa")
    print("")
    opcion = input("Ingrese la opcion que desee ingresar: ");
    if opcion == "1":
        agregar_producto(coleccion)
    elif opcion == "2":
        ver_productos(coleccion)
    elif opcion == "3":
        modificar_producto(coleccion)
    elif opcion == "4":
        eliminar_producto(coleccion)
    elif opcion == "5":
        guardar_archivo(coleccion, nombre_archivo)
    elif opcion == "6":
        print("Saliste del programa, hasta pronto!!!")
        flag = False
    else:
        print("Opcion incorrecta, vuelva a intentarlo")
