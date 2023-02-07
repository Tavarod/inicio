#escribir un scrip que nos muestre los numeros impares del 1 al 120
numero = 1
for numero in range(0, 121):
    if numero % 2 == 0:
        print(f"☺{numero}")
    elif not numero % 2 == 0:
        print(f"®{numero}")
"""el for recorre el rango de un a 121 lo guarda en la variable numero
da una vuelta se divide entre dos con el simbolo de porcentaje % se 
saca el resultado, si este es cero carita feliz para el par y  
® para impar ya que el resto (%), no es cero """



















