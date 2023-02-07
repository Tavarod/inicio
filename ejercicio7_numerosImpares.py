"""programa que muestra todos los numeros impares que eliga el usuario"""
while True:
    numeroA = input("a = ")
    while not numeroA.isnumeric():
        print("Valores Incorrectos en A")
        numeroA = (input("a = "))
    numeroA = int(numeroA)

    numeroB = input("b = ")
    while not numeroB.isnumeric():
        print("Valores Incorrectos en B")
        numeroB = input("b = ")
    numeroB = int(numeroB)

    if numeroA < numeroB:
        for impar in range(numeroA, numeroB +1):
            if impar%2 == 0:
                print(f"{impar} es par")
            else:
                print(f"{impar} es impar")
    else:
        print("para realizar el calculo 'a' debe ser menor que 'b'")







