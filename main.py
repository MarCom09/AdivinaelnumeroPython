#Juego por Marcos Comeche

import time
import random

numeroporadivinar = random.randint(1, 20)
intentos = 0
print('Como te llamas?')
nombre = input('Me llamo ')
time.sleep(0.5)
print(f'Hola, {nombre}, estoy pensando en un número del 1 al 20. Intenta adivinarlo.')
time.sleep(0.5)
print('Pero cuidado, solo tienes 8 intentos!')
time.sleep(0.5)
print('Vamos allá!')
time.sleep (0.5)

while intentos < 8:
    numeroadivinado = input('El número es ')
    numeroadivinado = int(numeroadivinado)
    if numeroadivinado > numeroporadivinar:
        print('Muy alto, inténtalo de nuevo.')
        intentos += 1
        time.sleep(0.5)
    
    if numeroadivinado < numeroporadivinar:
        print('Muy bajo, inténtalo de nuevo.')
        intentos += 1
        time.sleep(0.5)

    if numeroadivinado == numeroporadivinar:
        break

time.sleep(0.5)
if numeroadivinado == numeroporadivinar:
    print(f'Enhorabuena, has adivinado el número {numeroporadivinar}')       
else:
    print('Te has quedado sin intentos, prueba de nuevo.')
