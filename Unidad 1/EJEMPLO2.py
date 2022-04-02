#Realizar un programa el cual introduzca mediante una cadena uno o dos nombres o palabras
#y el cual me muestre las mayusculas de las palabras principales.

nombre = input("Introduce uno o dos nombres:   ")
iniciales = "  "
posicion = 0

#Eliminar las posiciones de los espacios
nombre = nombre.strip()
#Esta parte es para decirle que me muestre de la palabra la letra inicial.
iniciales = iniciales + nombre[0]
#Aqui buscamos todos los espaios de la palabra.
posicion = nombre.find("  ",posicion)
#Utilizamos un while, esto en el caso de que no cumpla con lo que estoy buscando, esto forzara a mostrar lo que busco.
while posicion !=-1:

    while nombre [posicion + 1]== "  ":
        posicion = posicion + 1
        iniciales = iniciales + nombre[posicion + 1]
        posicion = nombre.find("   ",posicion + 1)
print("Las letras de la palabra son:   ",iniciales.upper())