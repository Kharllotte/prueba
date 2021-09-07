import os
print("Bienvenido al sistema de ubicación para zonas públicas WIFI") #Mensaje de bienvenida al sistema
usuario = 51614  #usuario predefinido
contrasena = 41615 #contraseña predefinida
coordenadas = [[None,None],
                [None,None],
                [None,None]]

Sup = 6.284    
Inf = 6.077
Or = -75.841     
Occ = -76.049

miLista = ["Cambiar contraseña" ,"Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]
contador = 0
primeraVez = 0
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

                os.system("cls")
                if 'contraseña' in miLista[opcion-1]:
                    print("Usted ha elegido la opción",opcion)
                    if contrasena==int(input("Ingrese contraseña actual: ")):
                        newPass = int(input("Ingrese nueva contraseña: "))
                        if contrasena != newPass:              
                            print("contraseña actualizada")  
                            contrasena = newPass
                            continue
                        else:
                            print("Error\nDebe ingresar una contraseña diferente a la actual")
                            exit()
                    else:
                        print("Error")
                        exit()   

                elif 'coordenadas' in miLista[opcion-1]:
                    listSitios=["Trabajo","Casa","Parque"]
                    print("Usted ha elegido la opción",opcion) 

                    def llenarMatriz():
                        print("A continuación debe ingresar las coordenadas de los tres sitios que más frecuenta: ")
                        index =1
                        for sitios in listSitios:
                            print(index, sitios)
                            index+=1
                        for i in range(3):
                            print("Ingrese la coordenada ",(i+1))
                            try:
                                latitud = round(float(input("ingrese latitud:")),3)
                                if latitud <= Sup and latitud >= Inf:
                                    coordenadas[i][0] = latitud
                                    longitud = round(float(input("ingrese longitud:")),3)
                                    if longitud <= Or and longitud >= Occ:
                                        coordenadas[i][1] = longitud  
                                        #primeraVez = 1                                                     
                                    else:
                                        print("Error coordenada")
                                        exit()        
                                else:
                                    print("Error coordenada")
                                    exit()           
                            except:
                                print("Error")
                                exit()   
                        
                    def ModificarMatriz():
                        print("Modificar matriz")
                        for i,c in enumerate(coordenadas):
                            print(f"coordenada [latitud , longitud] {i+1} : {c}")
                        
                        #Sur  -- Promedio   
                        num = 99
                        posicion = 0
                        s_latitud = 0
                        s_longitud = 0
                        for i,c in enumerate(coordenadas):
                            if num > c[0]:
                                num = c[0]
                                posicion = i+1   

                            s_latitud += c[0] 
                            s_longitud += c[1]
                        p_latitud = round(s_latitud / len(coordenadas),3)
                        p_longitud = round(s_longitud / len(coordenadas),3)
                        print(f"La coordenada {posicion} es la que está más al sur")
                        print( f"La coordenada promedio de todos los puntos es: [{p_latitud}, {p_longitud}]")


                        try:
                            editar = int(input('Presione 1,2 o 3 para actializar la respectiva coordenada\nPresione 0 para regresar al menu\n'))
                            if(editar >= 1 and editar <= 3):
                                latitud = round(float(input("ingrese latitud:")), 3)
                                if latitud <= Sup and latitud >= Inf:
                                    coordenadas[editar - 1][0] = latitud
                                    longitud = round(float(input("ingrese longitud:")), 3)
                                    if longitud <= Or and longitud >= Occ:
                                        coordenadas[editar - 1][1] = longitud
                                    else:
                                        return "Error coordenada"
                                else:
                                    return "Error coordenada"
                            elif editar == 0:
                                return 0
                            else:
                                return "Error actualización"
                                
                        except:
                            return "Error"

                    result = True
                    m = 0
                    while result:
                        if coordenadas[m][0] == None or coordenadas[m][1] == None:
                            result = False
                            break
                        elif m >= 2:
                            break
                        m += 1

                    if result:
                        modi = ModificarMatriz()
                        if type(modi) is str:
                            print(modi)
                            exit()
                        else:
                            continue    
                    else:
                        llenarMatriz()
                        continue

                elif opcion >=1 and opcion <=5:
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

  
