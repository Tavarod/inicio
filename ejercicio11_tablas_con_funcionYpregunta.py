print("█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█")
print("█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█Tablas*☺█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄██▄█")
#tablas de multiplicar con funciones
def tabla(numero, rango):
    print(f"Tabla a imprimir: {numero}")
    print(f"Rango deseado: {rango}")

    for contador in range(rango):
        operacion = numero * contador
        print(f"{numero} * {contador} = {operacion}")

numero = int(input("Que tababla desea ver? : \n"))
rango = int(input("Rango de la tabla? : \n"))
tabla(numero, rango)
pregunta = input("desea ver otra tabla S/N").upper()

while pregunta == "S":
    numero = int(input("Que tababla desea ver? : \n"))
    rango = int(input("Rango de la tabla? : \n"))
    tabla(numero, rango)
    pregunta = input("¿Desea ver otra tabla?(S/N)")

if pregunta == "N":
    print("Bye que tenga un buen dia")