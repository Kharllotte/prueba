import os

print("Bienvenido al sistema de ubicación para zonas públicas WIFI") #Mensaje de bienvenida al sistema
usuario = 51614  #usuario predefinido
contrasena = 41615 #contraseña predefinida
usuario1 = int(input("Ingrese el usuario: "))
if usuario1 == usuario: #validacion del usuario
    contrasena1 = int(input("Ingrese la contraseña: "))
    if contrasena1 == contrasena: #validacion contraseña
        captcha1 = 614
        captcha2 = (4+6-(5*1)-4)      
        captcha3 = captcha1 + captcha2  
        print(captcha1,"+",captcha2, "=")
        captcha = int(input())
        if captcha == captcha3:
            print("Sesión iniciada")
            miLista = ["Cambiar contraseña" ,"Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]
            contador = 0
            while True:
                os.system("cls")
                for i in range(0,7):
                    print(str(i+1) + ". " + miLista[i])
                opcion = int(input("Elija una opción\n"))    

                if opcion >=1 and opcion <=5:
                    print("Usted ha elegido la opción",opcion)
                    exit()

                elif opcion == 6:
                    fav = int(input("Seleccione opción favorita\n"))
                    if fav>=1 and fav<=5:
                        adiv1 = int(input("Para confirmar por favor responda: ¿cual es el primer numero? "))
                        if adiv1 == 1:
                            adiv2 = int(input("Para confirmar por favor responda: ¿cuanto es 2 + 2? la respuesta es "))
                            if adiv2 == 4:
                                #limpiar consola
                                os.system("cls")
                                opc = miLista.pop(fav-1) 
                                miLista.insert(0, opc)           
                            else:
                                print("Error")
                        else:
                            print("Error")
                    else:
                        print("Error")
                        exit()

                elif opcion == 7:
                    print("Hasta pronto")
                    exit()

                else:
                    print("Error")
                    contador+= 1
                    if contador >=3:
                        exit()
        else:
           print("Error")    
           exit()      
    else:    
        print("Error")    
        exit()   
else:
    print("Error")    
    exit()
   


        



