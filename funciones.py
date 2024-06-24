def modificar_producto(coleccion):
    contador = 0;
    flagmodificar = True;
    print("\n\n*** Modificando productos ***\n\n");
    print("Mostrando los productos que puede modificar: ");
    ver_productos(coleccion);
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
        ver_productos(coleccion);
    else:
        print("El producto no se encuentra en tu lista.");

def guardar_archivo(coleccion, nombre_archivo):
    with open(nombre_archivo+".txt","w",encoding= "utf-8") as archivo:
        archivo.write(f"Codigo - Nombre - Cantidad - Precio\n");
        for i in coleccion:
                archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]}\n");


def agregar_producto(lista):
    print("Agregar Producto")
    flagagregar=True;
    flagprecio=True;
    contador = 0;
    while flagagregar:
        producto=input("Ingrese el nombre del producto: ")
        codigo=input("Ingrese el codigo del producto: ")
        try:
            cantidad=int(input("Ingrese la cantidad del producto: "))
        except:
            print("Ingrese correctamente la cantidad del producto.\n")
        else:
            flagagregar=False;

    while flagprecio:
        try:
            precio=float(input("Ingrese el precio de su producto: "))
        except:
            print("Ingrese correctamente el precio del producto.")
        else:
            if lista == []:
                    flagprecio=False;
                    lista.append([
                        codigo,
                        producto,
                        cantidad,
                        precio]
                    )
                    print("Producto agregado exitosamente.")
            else:
                flagprecio=False;
                for i in lista:
                    if (producto not in i) and (codigo not in i):
                        contador = 1;
                if contador == 1:
                    lista.append([
                                codigo,
                                producto,
                                cantidad,
                                precio]
                            )
                    print("Producto agregado exitosamente.")
                else:
                    print("El producto no se ha agregado porque el nombre o codigo ya se encuentra en la lista")


        

def eliminar_producto(lista):
    print("Eliminar Producto")
    flageliminar=True;
    while flageliminar:
        ver_productos(lista)
        productoeliminar=input("Ingrese el nombre del producto que desee eliminar: ")
        flageliminar=False;
        for i in lista[:]:
            if productoeliminar in i:
                lista.remove(i);
    print("Producto eliminado exitosamente.")

def menu():
    #Menu del programa
    lista =[];
    flag = True
    while flag:
        print("")
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
            print("")
            agregar_producto(lista)
            print("")
        elif opcion == "2":
            print("")
            ver_productos(lista)
            print("")
        elif opcion == "3":
            print("")
            modificar_producto(lista)
            print("")
        elif opcion == "4":
            print("")
            eliminar_producto(lista)
            print("")
        elif opcion == "5":
            print("")
            nombre_archivo = input("Ingrese el nombre que tendra el archivo sin su extención: ");
            guardar_archivo(lista, nombre_archivo)
            print("")
        elif opcion == "6":
            print("")
            print("Saliste del programa, hasta pronto!!!")
            flag = False
        else:
            print("")
            print("Opcion incorrecta, vuelva a intentarlo")

def ver_productos(lista):
    for i in lista:
        print(i)
