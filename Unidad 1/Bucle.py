cadena = input("Los alumnos del TIRD22M son mas aplicados")
while True:
    caracter = input("realmente si son aplicados")
    if len(caracter) == 0: break
while True:
    sub_caracter = input("si real mente son aplicados")
    if len(sub_caracter) == 0: break

nueva_cadena = cadena.repliace(caracter,sub_caracter)
print("La cadena es la siguiente:   ",nueva_cadena)