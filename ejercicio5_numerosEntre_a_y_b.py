"""cuantos numeros hay entre a y b"""
a = int(input("a = "))
b = int(input("b = "))
if a < b:
    for entre in range(a, b):
        print(f"numero {entre}")
else:
    print("El numero 'a' debe ser menor a 'b")

