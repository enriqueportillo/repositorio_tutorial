#Juego de adivinar
from ast import Str
import random

intentos = 0

print("Hola como te llamas?")
miNombre = input()

numero = random.randint(1,20)
print('Bueno, '+miNombre+', estoy pensando en un numero entere 1 y 20.')

while intentos<6:
    print('intenta adivinar el numero')
    tri = input()
    tri = int(tri)

    intentos = intentos + 1

    if tri < numero:
        print('Tu intento es muy bajo.')
    
    if tri > numero:
        print('Tu intento es muy alto.')
    
    if tri == numero:
        print('Su numero es correcto.')
        break

if tri == numero:
    intentos = str(intentos)
    print('Buen trabajo!!!'+miNombre+', Haz adivinado mi numero en, '+intentos+' ,Intentos!')

if tri != numero:
    numero = str(numero)
    print= ('Fallaste, el numero era'+numero)
