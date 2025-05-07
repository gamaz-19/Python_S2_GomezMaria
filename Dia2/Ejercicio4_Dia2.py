###################
#### Clase dia 2 ##
###################

# Evaluar si un numero es primo

print("Bienvenido al portal para verificar si un numero es primo  ")
num=(int(input("Ingrese el numero que quiere evaluar  ")))

divisores=0
cantidadDivisores=0


for i in range(1,num,1):
    divisores=divisores+1
    resultado=num % divisores

    if resultado==0:
        cantidadDivisores =    cantidadDivisores+1
    
    if cantidadDivisores>2:
        print ("el numero no es primo")

else: 
    print("El numero es primo") 
    
 #Desarrollado por: Maria Alejandra Gomez Archila - CC.1005234916


