#crear un sistemautilizando operadores donde la temporada de vacciones de
#un trabajador

print("Bienvenidos al sistema de vaciones")

nombre_trabajador = input("Nombre del empleado:   ")
id_trabajador = int(input("Numero de empleado:   "))
#1-Obrero 2-Supervisor 3-Gerente 4-Director
clave_de_area = int(input("Clave del area del trabajo   "))
antigued_trabajador = int(input("Años laborados por el trabajador   "))


if clave_de_area == 1:
    if antigued_trabajador == 1 and antigued_trabajador < 2:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador," tiene 5 dias habiles")
    elif antigued_trabajador >= 2 and antigued_trabajador <= 6:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 15 dias habiles:")
    elif antigued_trabajador >= 9:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 20 dias habiles")
    else:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"Un no acumula sus derechos")
elif clave_de_area ==2:
    if antigued_trabajador == 1 and antigued_trabajador <2:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 7 dias habiles")
    elif antigued_trabajador >=2 and antigued_trabajador <=6:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajador:   ",id_trabajador,"tiene 17 dias habiles")
    elif antigued_trabajador >= 9:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 25 dias habiles")
    else:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"Un no acumula sus derechos")
elif clave_de_area == 3:
    if antigued_trabajador == 1 and antigued_trabajador <2:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 8 dias habiles")
    elif antigued_trabajador >=2 and antigued_trabajador <=6:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajador:   ",id_trabajador,"tiene 18 dias habiles")
    elif antigued_trabajador >= 9:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 26 dias habiles")
    else:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"Un no acumula sus derechos")
elif clave_de_area == 4:
    if antigued_trabajador == 1 and antigued_trabajador <2:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 9 dias habiles")
    elif antigued_trabajador >=2 and antigued_trabajador <=6:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajador:   ",id_trabajador,"tiene 19 dias habiles")
    elif antigued_trabajador >= 9:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"tiene 26 dias habiles")
    else:
        print("El empleado:   ",nombre_trabajador,"   con id de trabajo:   ",id_trabajador,"Un no acumula sus derechos") 
else:
    print("La clave no existe")