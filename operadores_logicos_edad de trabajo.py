edad = int(input("Ingrese edad"))
if edad >= 18 and edad <= 60:
    print("Usted tiene que pagar ...daaaaaa ♥")
else:
    print("Bienvenido usted NO paga nadita nada de nada")

salario = int(1160000)
auxilioTransporte = int(140606)
salarioEmpleado = int(input("Ingrese salario"))
diasTrabajados = int(input("ingrese dias trabajados"))
totalSalario = salarioEmpleado + auxilioTransporte
valorDia = salarioEmpleado / 30
#se usa operador logico and para crear ciertas condiciones
if salarioEmpleado >= 1160000 and salarioEmpleado <= salario *2 and diasTrabajados > 0:
    print(f"{totalSalario}")
    print(f"{valorDia * diasTrabajados}")
else:
    print("usted debe realizar el calculo en el modulo 2")