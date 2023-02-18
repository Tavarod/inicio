def numerosId (nombre, cedula):
   emplado = nombre+ ", con identificacion numero: " +cedula+ " "

   ingreso = ""
   ingreso += emplado
   return ingreso

registros = []

while True:
   name1 = input("Ingrese su nombre")
   cedula = input("Ingrese su numero de cedula")
   registros.append(numerosId(name1, cedula))
   nuevo = input("otro ingreso , SI o NO").upper()
   if nuevo == "NO":
      break

print("Lista de usuarios conectados")
for registro in registros:
   print(registro)