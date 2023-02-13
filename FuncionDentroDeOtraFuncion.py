def getname(nom1):
    texto = input(nom1)
    return texto
def getsurname(surname1):
     texto = input(surname1)
     return texto
def fullname(name, surnamE):
    texto = getname(name) + getsurname(surnamE)
    texto += str(f"Nombre completo:\n{name} {surnamE}")
    return texto

name = input("Nombres por favor")
surname = input("Apellidos por favor")
print(fullname(name, surname))


