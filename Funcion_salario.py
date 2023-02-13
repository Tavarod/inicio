def salario(diasL, salario, diasA):
    pagoDia = salario / 30
    descuento = pagoDia * diasA
    totalPago = diasL * pagoDia - descuento

    resultado = ""
    resultado +="Pago por dia  $" + str(pagoDia)
    resultado += "\n"
    resultado += "Descuentos por dias faltantes $" + str(descuento)
    resultado += "\n"
    resultado += "Salario total $" + str(totalPago)
    return resultado

diasL = float(input("Cuantos dias trabajo en este mes"))
while diasL > 30:
    print("El mes laboral solo tiene 30 dias")
    diasL = float(input("Cuantos dias trabajo en este mes"))

salarioM = float(input("Salario mensual"))
while salarioM < 1160000:
    print("El salario no puede ser menor a $1.160.000 pesos para el año 2023")
    salarioM = float(input("Salario mensual"))

diasDescuento = float(input("Cuantos dias se descuentan"))
while diasDescuento <= 0:
    print("El numero de dias de descento debe ser mayor a 0")
    diasDescuento = float(input("Cuantos dias se descuentan"))

print(salario(diasL, salarioM, diasDescuento))

