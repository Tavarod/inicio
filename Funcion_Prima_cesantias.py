def prima(dias, salario):
    primaC = dias * salario / 360
    return primaC

def cesantias(dias, salario):
    cesantiasC = dias * salario / 360
    return cesantiasC

dias_laborados = int(input("Días trabajados: \n"))
salario = int(input("Salario: \n"))
resultadoP = prima(dias_laborados, salario)
resultadoC = cesantias(dias_laborados, salario)
print(f"{resultadoP}\n{resultadoC}")