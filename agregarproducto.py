

def agregar_productos(lista):
    print("Agregar Producto")
    flagagregar=True;
    flagprecio=True;
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
            flagprecio=False;
            lista.append([
                codigo,
                producto,
                cantidad,
                precio]
            )
    print("Producto agregado exitosamente.")


        


    

  




