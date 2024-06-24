import Funciones as Funcion
# if usuario in usuarios and usuarios[usuario] == clave:
#whit open("Nombrearchivo.txt", "w-r-a", encoding = "utf-8") as archivo:
#archivo.write()
lista = [
    ["codigo", "nombre", "cantidad", "precio"],
    [111011, "arroz 1kg", "30", "$1.200"],
    [111012, "arroz 3kg", "30", "$1.600"],
    [111013, "arroz 4kg", "30", "$1.900"],
    [111014, "arroz 5kg", "30", "$2.200"],]

Funcion.modificar_producto(lista);
Funcion.mostrar_productos(lista)
Funcion.modificar_producto(lista);
nombre_archivo = "Hola"
Funcion.guardar_archivo(lista,nombre_archivo);