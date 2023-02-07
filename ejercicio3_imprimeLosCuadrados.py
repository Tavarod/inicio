#escribir un programa que imprima los cuadrados de los primeros 60 primeros numeros naturales usar while y for
contador = 0
while contador <= 10:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}▓▓")
    contador += 1

"""Creamos la variable Contador que es un número que va alterando hasta llegar al 60.
Utilizamos el bucle While para decirle mientras que Contador sea menor o igual a 60 sigue dando vueltas
en el bucle, se  sigue iterando en el bucle hasta que llege a 60"""

"""linea 5__Entonces entramos al bucle mientras que Contador sea menor de 60 creamos una variable cuadrado y sacamos
el cuadrado de Contador que multiplica el contador por Contador y lo guardamos dentro de la variable
cuadrado."""

"""Utilizamos la función Print con la f para intemporar y mostrar dentro de un string estas variables y
mostramos este string por pantalla directamente que dice que el cuadrado de número Contador es el númeroque se genere 
al hacer la multiplicación de Contador por Contador y luego ya por último aumentamos 

en 1 el contador para que el bucle siga aumentando poco a poco """

contador = 1
while contador <= 10:
    print(f"El cuadrado de {contador} es {contador**2}☺")
    contador += 1


for numero in range(0, 10):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}® ")















