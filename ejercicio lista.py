"""
hacer un programa que tenga una lista de 8 numeros enteros y nos de el siguiente resultado
1.recorrer una lista y mostrarla
2.hacer una funcion que recorra lista de numeros y devuelva un string
3.ordenarla y mostrarla
4.mostrar su longitud
5.buscar algun elemento (que el usuario pida por teclado)
"""

numerosEnteros = [1,2,3,4,5,6,7,8,-1,-3,12,-8,-6,-9,-3,-1]
for numeros in (numerosEnteros):
    print(f"Recorriendo la lista:{numeros}")

def numEnt (lista):

    resultado = ""
    for elemento in (lista):
        resultado += str(elemento)
        resultado += "\n"

    return resultado

print("aca va la funcion:")
print(numEnt(numerosEnteros))

print("aca va la longitud de la lista:")
print(len(numEnt(numerosEnteros)))

busqueda = int(input("que numero va a buscar"))
#aca se omprueba si es un entero
comprobar = isinstance(busqueda, int)
while not comprobar :
    busqueda = int(input("que numero va a buscar"))
else:
    print(f"el valor , {busqueda}, es valido")

print(f"Buscando......{busqueda},LOAD.......")
search = numerosEnteros.index(busqueda)
print(f"el numero existe,esta en la ubicacion {search}")

print(numerosEnteros.count(busqueda))
print(f"{busqueda}" in numerosEnteros)

print("Aca se organizan")
numerosEnteros.sort()
print(numerosEnteros)

