"""
Se ha utilizado el operador "not in" para simplificar la condición del bucle while y hacerla más fácil de leer.
Se ha eliminado la comparación con el operador "or", ya que no es necesaria si se utiliza el operador "not"
y se compara el rango
El programa solo hace el calculo sobre dos salarios minimos legales vigentes en colombia
"""
"""
def generoD(), define si el usuario es hombre o mujer 
"""
def generoD():
    genero = ""
    while genero not in ["hombre", "mujer"]:
        genero = input("Ingrese su género (hombre/mujer): ")
        if genero not in ["hombre", "mujer"]:
            print("Entrada inválida, por favor ingrese 'hombre' o 'mujer'.")
    print("Gracias por ingresar su género.")
"""
def edadD(), define si el usuario es mayor de edad y no esta es de  la 
tercera edad 
"""
def edadD():
    edad = 0
    while not (18 <= edad <= 70):
        edad = int(input("Por favor ingrese su edad: "))
        if not (18 <= edad <= 70):
            print("Entrada inválida, usted no cumple con el rango de edad permitido (18-70).")
    print("Entrada válida, ingreso permitido.")

"""
def salarioS(), define si el salario del usuario es mayor a un SMLV en colombia
y defone si se le debe pagar el subsidio de transporte 
"""
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
    dia = (salario / 30)
    print(f"Salario diario: {dia}")