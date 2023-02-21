from datetime import datetime, time, timedelta

def horallegada():

    print("Digite su hora de llegada")
    horaE = int(input("Hora , Digite un numero entre el 1 y el 24 =♥ "))
    while horaE < 1 or horaE > 24:
        print("HORA NO VALIDA")
        horaE = int(input("Hora , Digite un numero entre el 1 y el 24 =♦ "))
    else:
        print("Hora Ingresada")

    minutoE = int(input("Minutos, Digite un numero entre el 1 y 60 =♥ "))
    while minutoE < 0 or minutoE > 60:
        print("MINUTO NO VALIDO")
        minutoE = int(input("Minuto, Digite un numero entre el 1 y 60 =♦"))
    else:
        print("Minuto Ingresado")

    hora_de_entrada = datetime.combine(datetime.today(), time(horaE, minutoE))

    return (hora_de_entrada)


def horasalida():
    print("Digite su hora de salida")
    horaS = int(input("Hora, Digite un numero entre el 1 y el 24: "))

    while horaS < 1 or horaS > 24:
        print("HORA NO VALIDA")
        horaS = int(input("Hora, Digite un numero entre el 1 y el 24: "))
    else:
        print("Hora de salida ingresada")

    minutoS = int(input("Minutos, Digite un numero entre el 1 y el 60: "))
    while minutoS < 0 or minutoS > 60:
        print("MINUTO NO VALIDO")
        minutoS = int(input("Minutos, Digite un numero entre el 1 y 60: "))
    else:
        print("Minuto de salida ingresado")

    hora_de_salida = datetime.combine(datetime.today(), time(horaS, minutoS))

    return hora_de_salida

hora_llegada = horallegada()
print("Hora de llegada:", hora_llegada)

hora_salida = horasalida()
print("Hora de salida:", hora_salida)

horasTrabajadas = hora_salida - hora_llegada - timedelta(hours=1)
print(horasTrabajadas)