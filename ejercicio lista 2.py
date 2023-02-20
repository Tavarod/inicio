#escribir un programa que añada valores a una lista mientras que su longitud sea 120 y luego mostrar la lista
#usar while y for

lista = [1,2,3,4,5,6,7,8,9,0,]
agregar1 = input("va agregar elementos a la lista? (S/N)")
while agregar1.upper() == "S":
    agregar = input(f"que valor va agregar")
    while not agregar.isnumeric():
        print(f"el valor ingresado :{agregar},  no es un numero")
        agregar = input(f"que valor va agregar")
    if len(lista) > 15:
        print("no se pueden agregar mas numero")
        break
    else:
        lista.append(agregar)
    agregar1 = input("Desea agregar elementos a la lista? (S/N)")

print("gracias vuelva pronto")
print(f"La lista final es {lista}")
resultado = 0
for elemento in lista:
    resultado += int(elemento)
print(f"La suma de los elementos de la lista es: {resultado}")


