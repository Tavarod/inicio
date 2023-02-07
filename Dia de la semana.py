#dia de la semana usando if else, abajo un codigo mas eficiente

dia = input("introduce el dia de la semana")
if int(dia) == 1:
    print("El dia es lunes")
else:
    if int(dia) == 2:
        print("El dia es martes")
    else:
        if int(dia) ==3:
            print("El dia es miercoles")
        else:
            if int(dia) == 4:
                print("El dia es jueves")
            else:
                if int(dia) == 5:
                    print("El dia es viernes")
                else:
                    if int(dia) == 6:
                        print("El dia es sabado")
                    else:
                        if int(dia) == 7:
                            print("El dia es domingo")
                        else:
                            if int(dia) >= 8:
                                print("Ese dia no existe o tal vez si , en tu mente ◘☺◘")

#aca un codigo mas eficiente
print("☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺")
dia = input("introduce  de nuevo el dia de la semana☺\n")
if int(dia) == 1:
    print("Lunes")
elif int(dia) == 2:
    print("Martes")
elif int(dia) == 3:
    print("Miercoles")
elif int(dia) == 4:
    print("Jueves")
elif int(dia) == 5:
    print("viernes")
else:
    print("ES FIN DE SEMANA")




