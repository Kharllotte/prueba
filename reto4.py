import os
import math

print("Bienvenido al sistema de ubicación para zonas públicas WIFI") #Mensaje de bienvenida al sistema
user = "Tripulante2022"
usuario = "51614"  #usuario predefinido
contrasena = 41615 #contraseña predefinida
coordenadas = [[None,None],
                [None,None],
                [None,None]]

Sup = 6.284    
Inf = 6.077
Or = -75.841     
Occ = -76.049

velMoto = 19.44
velBici = 3.33

def definirZonas():
    listZonasWifi=[[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]]
    validaZonas = 0
    for i in range(4):
        for j in range(2):
            if j == 0:
                if listZonasWifi[i][j] >= 6.284 or listZonasWifi[i][j] < 6.077:
                    print(f"La latitud de la coordenada {i+1} No esta dentro de los limites")
                    validaZonas = 1
            else: 
                if listZonasWifi[i][j] >= -75.841 or listZonasWifi[i][j] < -76.049: 
                    print(f"La longitud de la coordenada {i+1} No esta dentro de los limites")
                    validaZonas = 1     
    if validaZonas == 0:
        print("Las coordenadas se encuentran dentro de los limites")
    return(listZonasWifi)    

def mostrarCoordenadas(matriz):
    for i in range(len(matriz)):
        print("coordenada [latitud,longitud] "+str(i+1)+" :", matriz[i])

def distanciaZonas(zonas, punto):
    latitud1 = math.radians(punto[0])
    longitud1 = math.radians(punto[1])
    R = 6372.795477598 #Km
    #Calcular distancias
    for i in range(len(zonas)):
        latitud2 = math.radians(zonas[i][0])
        longitud2 = math.radians(zonas[i][1])
        #deltaLatitud = latitud2 - latitud1
        deltaLongitud = longitud2 - longitud1
        #distancia = 2 * R * math.asin((math.sin(deltaLatitud/2))**2 + (math.cos(latitud1) * math.cos(latitud2) * (math.sin(deltaLongitud / 2))**2))**1/2
        distancia = (math.acos(math.sin(latitud1) * math.sin(latitud2) + math.cos(latitud1) * math.cos(latitud2) * math.cos(deltaLongitud))) * R
        distancia = distancia*1000 #Convertir de Km a m
        distancia = round(distancia,3)
        zonas[i].append(distancia)

    #Ordenar de menor a mayor las distancias
    for i in range(len(zonas) - 1):
        for j in range(i+1,len(zonas)):
            if zonas[i][3] > zonas[j][3]:
                distanciaTemp = zonas[i]
                zonas[i] = zonas[j]
                zonas[j] = distanciaTemp 
    return(zonas[:2]) #retorna las 2 distancias menores  

def ordenarVector(vector):
    for i in range(len(vector) - 1):
        for j in range(i+1, len(vector)):
            if vector[i][2] > vector[j][2]:
                usuarioProm = vector[i]
                vector[i] = vector[j]
                vector[j] = usuarioProm
    return(vector) #Retorna el vector ordenado por usuarios de menor a mayor            


miLista = ["Cambiar contraseña" ,"Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]
contador = 0
primeraVez = 0
usuario1 = input("Ingrese el usuario: ")
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

                if opcion == 2021:
                    easteregglat=float(input("Dame una latitud y te diré cual hemisferio es…\n"))
                    if easteregglat > 0:
                        print("Usted está en hemisferio norte”,")
                        break
                    elif easteregglat < 0:
                        print("Usted está en hemisferio sur")
                        break
                    elif easteregglat == 0:
                        print("Usted está en el Ecuador" )
                        break

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

                elif 'Ubicar zona wifi' in miLista[opcion-1]:
                    zonasWifi = definirZonas() 
                    os.system("cls")
                    
                    result = True
                    m = 0
                    while result:
                        if coordenadas[m][0] == None or coordenadas[m][1] == None:
                            result = False
                            break 
                        elif m >= 2:
                            break
                        m += 1   
                    
                    if result == False:
                        print("Error sin registro de coordenadas")
                        exit() 
                    else:
                        mostrarCoordenadas(coordenadas)                        
                    
                    menuZona = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión"))
                    if menuZona >=1 and menuZona <=3:
                        corDistancia = distanciaZonas(zonasWifi,coordenadas[menuZona -1]) 
                        corDistancia = ordenarVector(corDistancia)  
                        print("Zonas wifi cercanas con menos usuarios")
                        for i in range(len(corDistancia)):
                            print("La zona wifi", i+1, "ubicada en",corDistancia[i][:2],"a", corDistancia[i][3],"metros , tiene en promedio",corDistancia[i][2],"usuarios" )
                        
                        guia = "Para llegar a la zona wifi dirigirse "
                        indicaciones = int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                        if indicaciones >=1 and indicaciones <=2:
                            if coordenadas[menuZona -1][1] < corDistancia[indicaciones -1][1]:
                                guia = guia + "primero al oriente"
                            elif coordenadas[menuZona -1][1] > corDistancia[indicaciones -1][1]:
                                guia = guia + "priemro al occidente"
                            if coordenadas[menuZona -1][0] < corDistancia[indicaciones -1][0]:
                                guia = guia + " y luego hacia el norte"       
                            elif coordenadas[menuZona -1][0] > corDistancia[indicaciones -1][0]:
                                guia = guia + " y luego hacia el sur" 
                            #4 moto y bici
                            tiempoMoto = math.floor((corDistancia[indicaciones-1][3]/velMoto)/60)
                            tiempoBici = math.floor((corDistancia[indicaciones-1][3]/velBici)/60)
                            print(guia)
                            print("El tiempo estimado en moto",tiempoMoto,"minutos") 
                            print("El tiempo estimado en bicicleta",tiempoBici,"minutos")
                            while True:
                                salirOpcion = input("Precione 0 para salir")
                                if salirOpcion == "0":
                                    break

                        else:
                            print("Error Zona wifi") 
                            exit()      

                        
                    else:
                        print("Error ubicación")
                        exit()
        


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

elif usuario1 == user:
    print("Este fue mi primer programa y vamos por más")
    exit()

else:
    print("Error")    
    exit()

  
