nombre = ""
while not nombre.isalpha() and not nombre.isnumeric():
    nombre = input("Por favor escriba un nombre")
if nombre.isnumeric():
    print("curioso nombre , sus papas no lo querian")
else:
    print(f"bienvenido: "+ nombre)














