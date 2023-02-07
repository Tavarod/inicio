# sacar el porcentaje de un número
def es_flotante(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

numeroA = input("a = ")
while not es_flotante(numeroA):
    print(f"ERROR, valor {numeroA} no es válido")
    numeroA = input("a = ")
numeroA = float(numeroA)

porcenA = input("% = ")
while not es_flotante(porcenA):
    print(f"ERROR, valor {porcenA} no es válido")
    porcenA = input("% = ")
porcenA = float(porcenA)

resultado = numeroA * porcenA / 100
print(f"El {porcenA}% de {numeroA} es: {resultado}")


"""El código calcula el % de un número . Se pide al usuario que ingrese el número a y el porcentaje % que se 
quiere calcular. utilizo una función llamada es_flotante para verificar si el valor ingresado 
por el usuario es un número válido (flotante). Si no es un número flotante válido, se muestra un error y 
se vuelve a pedir el valor al usuario. Una vez que se han ingresado números válidos para 'a y %',
se calcula el porcentaje multiplicando 'a' por el porcentaje dividido por 100, y se muestra el 
 resultado en el print."""