def mostrar_productos(lista):
    for i in lista:
        print(i)

def modificar_producto(coleccion):
    contador = 0;
    flagmodificar = True;
    print("\n\n*** Modificando productos ***\n\n");
    print("Mostrando los productos que puede modificar: ");
    mostrar_productos(coleccion);
    opcion = input("Ingrese el nombre del producto desea modificar (igual a como sale en la tabla anterior): ");
    for i in coleccion:
        if opcion in i:
            while flagmodificar:
                print("¿Qué desea modificar?\n1.-Codigo\n2.-Nombre\n3.-Cantidad\n4.-Precio");
                opcionmodificar = input("Ingrese el número de la opción que desea: ");
                if opcionmodificar == "1":
                    codigo = input("Ingrese el nuevo codigo: ");
                    i[0] = codigo;
                    flagmodificar = False;
                elif opcionmodificar == "2":
                    nombre = input("Ingrese el nuevo nombre: ");
                    i[1] = nombre;
                    flagmodificar = False;
                elif opcionmodificar == "3":
                    cantidad = input("Ingrese la nueva cantidad: ");
                    i[2] = cantidad;
                    flagmodificar = False;
                elif opcionmodificar == "4":
                    try:
                        precio = int(input("Ingrese el nuevo precio: "));
                    except:
                        print("Formato ingresado incorrecto, volvera a la opcion de que desea modificar.");
                    else:
                        i[3] = precio;
                        flagmodificar = False;
                else:
                    print("Opción ingresada incorrecta, intentelo nuevamente.\n");
            contador += 1;
    if contador == 1:
        print("Producto modificado exitosamente.");
        mostrar_productos(coleccion);
    else:
        print("El producto no se encuentra en tu lista.");

def guardar_archivo(coleccion, nombre_archivo):
    with open(nombre_archivo+".txt","w",encoding= "utf-8") as archivo:
        for i in coleccion:
                print(i);
                archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]}\n");
