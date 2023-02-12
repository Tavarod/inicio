def nombre(nombre1, nombre2, apellido1, apellido2 ):

    nombres = nombre1+ " " + nombre2 + " "
    apellido = apellido1 +" "+ apellido2

    nombreC= ""
    nombreC += nombres
    nombreC += apellido
    return nombreC

nombreUno = input("Digite su primer nombre , como aparece en la cedula\n")
if nombreUno.isnumeric():
    print("Nombre no valido")
else:
    nombreUno = nombreUno.upper()

nombredos = input("Digite su segundo nombre , como aparece en la cedula\n")
if nombredos.isnumeric():
    print("Nombre no valido")
else:
    nombredos = nombredos.upper()

apellidoUno = input("Digite su primer apellido , como aparece en la cedula\n")
if apellidoUno.isnumeric():
    print("Nombre no valido")
else:
    apellidoUno = apellidoUno.upper()

apellidoDos = input("Digite su segundo apellido , como aparece en la cedula\n")
if apellidoDos.isnumeric():
    print("Nombre no valido")
else:
    apellidoDos = apellidoDos.upper()

if nombre(nombreUno, nombredos, apellidoUno, apellidoDos).isalnum():
    print("Vueva a escribir su nombre ")
else:
    print(nombre(nombreUno, nombredos, apellidoUno, apellidoDos))