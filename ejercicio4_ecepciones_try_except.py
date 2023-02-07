"""hacer todas las operaciones basica de una calculadora con dos numeros"""
while True:
    try:
        numeroA = int(input("Numero A: "))
        break
    except ValueError:
        print("Ingresa un número válido para A.")

while True:
    try:
        numeroB = int(input("Numero B: "))
        break
    except ValueError:
        print("Ingresa un número válido para B.")

while True:
    operacion = input(f"+\n-\n*\n/\n")
    if operacion in ["+", "-", "*", "/"]:
        break
    else:
        print("Operación inválida, ingresa una operación válida.")

if operacion == "+":
    print(f"{numeroA} + {numeroB} = {numeroA + numeroB}")
elif operacion == "-":
    print(f"{numeroA} - {numeroB} = {numeroA - numeroB}")
elif operacion == "*":
    print(f"{numeroA} * {numeroB} = {numeroA * numeroB}")
elif operacion == "/":
    print(f"{numeroA} / {numeroB} = {numeroA / numeroB}")
else:
    print("Operación inválida")


"""El bloque try en Python se utiliza para manejar errores o excepciones. Es decir, permite ejecutar un bloque de 
código y capturar posibles errores o excepciones que puedan ocurrir durante la ejecución. Si se produce un error, 
el control se transfiere automáticamente al bloque except correspondiente, que puede realizar alguna acción para 
manejar el error.
Por ejemplo, en el código anterior se utiliza un bloque try para intentar convertir los valores ingresados por el 
usuario en números enteros (int). Si la conversión falla, se produce una excepción ValueError, que es capturada por el 
bloque except. El bloque except imprime un mensaje de error indicando que el usuario debe ingresar un número válido."""