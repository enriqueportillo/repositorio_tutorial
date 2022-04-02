#Programa de calculadora de propina

print('Bienvenido a la calculadora de propinas.\n')
dias_trabajados = int(input("Ingrese la cantidad de dias trabajados para conocer el porcentaje de su propina\n"))

if dias_trabajados == 1 and dias_trabajados < 2:
    print('Usted ha trabajado 1 dia por lo tanto su propina es del 15%\n Ingrese la cantidad para obtener su porcentaje')
    cantidad = int(input(""))
    resultado = cantidad * 0.15
    print('La propina global es:', resultado)
    print('para conocer la cantidad que le toca a cada empleado ingrese la cantidad de empleados:')
    empleados = int(input(""))
    cantempleados = resultado / empleados
    print('La cantidad por empleado es:  ',cantempleados)
elif dias_trabajados >= 2 and dias_trabajados < 3:
    print('Usted ha trabajado 2 dias por lo tanto su propina es del 20%\n Ingrese la cantidad para obtener su porcentaje')
    cantidad = int(input(""))
    resultado = cantidad * 0.20
    print('La propina global es:', resultado)
    print('para conocer la cantidad que le toca a cada empleado ingrese la cantidad de empleados:')
    empleados = int(input(""))
    cantempleados = resultado / empleados
    print('La cantidad por empleado es:  ',cantempleados)
elif dias_trabajados >= 3 and dias_trabajados < 4:
    print('Usted ha trabajado 3 dias por lo tanto su propina es del 25%\n Ingrese la cantidad para obtener su porcentaje')
    cantidad = int(input(""))
    resultado = cantidad * 0.25
    print('La propina global es:', resultado)
    print('para conocer la cantidad que le toca a cada empleado ingrese la cantidad de empleados:')
    empleados = int(input(""))
    cantempleados = resultado / empleados
    print('La cantidad por empleado es:  ',cantempleados)
elif dias_trabajados >= 4 and dias_trabajados <= 7:
    print('Usted ha trabajado 4 dias por lo tanto su propina es del 30%\n Ingrese la cantidad para obtener su porcentaje')
    cantidad = int(input(""))
    resultado = cantidad * 0.30
    print('La propina global es:', resultado)
    print('para conocer la cantidad que le toca a cada empleado ingrese la cantidad de empleados:')
    empleados = int(input(""))
    cantempleados = resultado / empleados
    print('La cantidad por empleado es:  ',cantempleados)
else:
    print('La cantidad igresada no es valida')