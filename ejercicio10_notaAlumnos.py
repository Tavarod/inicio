"""pedir la nota de X alumnos y decir quien aprobo"""
contador = 0
aprobado = 0
suspendidos = 0
alumnosAprobados = []

numeroAlumnos = int(input("Cuantos alumnos a evaluar: "))

while contador < numeroAlumnos:
    nombreAlumno = input(f"Nombre del alumno {contador + 1}: ")
    nota = int(input(f"Nota del alumno {nombreAlumno}: "))

    if  nota >= 4:
        aprobado += 1
        alumnosAprobados.append(nombreAlumno)
#        print(f"El alumno {nombreAlumno} aprobó")
    else:
        suspendidos += 1
#        print(f"El alumno {nombreAlumno} suspendió")

    contador += 1
print(f"Aprobaron {aprobado} alumnos.")
print(f"Suspendieron {suspendidos} alumnos.")
print(f"Alumnos que aprobaron : {alumnosAprobados}")





