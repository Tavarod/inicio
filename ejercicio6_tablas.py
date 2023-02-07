"""todas las tablas"""
tabla = input("Tabla de multiplicar = ")
while not tabla.isnumeric():
    print("Ingrese solo numeros")
    tabla = input("Tabla de multiplicar = ? ")
tabla = int(tabla)

rango = input("Rango de la tabla = ")
while not rango.isnumeric():
    print("Ingrese solo numeros")
    rango = input("Rango de la tabla")
rango = int(rango)

if tabla < 0:
    print("Solo numeros positivos")
for contador in range(tabla, rango + 1):
    resultado = tabla * contador
    print(f"{tabla} * {contador} = {resultado}")