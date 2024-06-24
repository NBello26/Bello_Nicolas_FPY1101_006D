def eliminar_productos(lista):
    print("Eliminar Producto")
    flageliminar=True;
    while flageliminar:
        mostrar_productos(lista)
        productoeliminar=input("Ingrese el nombre del producto que desee eliminar: ")
        flageliminar=False;
        for i in lista[:]:
            if productoeliminar in i:
                lista.remove(i);
    print("Producto eliminado exitosamente.")

        

