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
    


