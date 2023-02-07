"""
primera opcion
"""
def generoD():
    genero = ""
    while genero != "hombre" and genero != "mujer":
        genero = input("Ingrese su género (hombre/mujer): ")
        if genero != "hombre" and genero != "mujer":
            print("Entrada inválida, por favor ingrese 'hombre' o 'mujer'.")
    print("Gracias por ingresar su género.")

def edadD():
    edad = 0
    while (edad < 18 or edad > 70):
        edad = int(input("Por favor ingrese su edad: "))
        if (edad < 18 or edad > 70):
            print("Entrada inválida, usted no cumple con el rango de edad permitido (18-70).")
    print("Entrada válida, ingreso permitido.")

def salarioS():
    salario = 0
    while not (1160000 <= salario <= 2320000):
        salario = int(input("Por favor ingrese su salario: "))
        if salario < 1160000:
            print("Entrada inválida, por favor ingrese un salario mayor a 1160000")
        elif salario > 2320000:
            print("Salario mayor a 2 SMLV, usted no tiene derecho a subsidio de transporte")
    print("Entrada válida, su salario se encuentra dentro del rango permitido.")
    return salario

generoD()
edadD()
salario = salarioS()
if salario > 1160000:
    dia =(salario / 30)
    print(f"Salario diario: {dia}")