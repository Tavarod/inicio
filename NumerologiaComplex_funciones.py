abecedario = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,'I': 9,'J': 10,'K': 11,'L': 12,'M': 13,
'N': 14,'Ñ': 15,'O': 16,'P': 17,'Q': 18,'R': 19,'S': 20,'T': 21,'U': 22,'V': 23,'W': 24,'X': 25,'Y': 26,'Z': 27}

def valorLetra(letra):
    return abecedario.get(letra.upper())

def imprimirResultado(nombre, suma):
    print(f"tu numero cosmico es ,{suma}, pagame mi maldito dinero por descubrir tu numero")

nombre = input("Ingrese su nombre por favor")

sumaletras = sum(valorLetra(letra) for letra in nombre if valorLetra(letra))

for letra in nombre:
    valor = valorLetra(letra)
    if valor:
        print(f"La letra '{letra}' tiene un valor de {valor}")

imprimirResultado(nombre, sumaletras)