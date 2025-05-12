###########################################
####### Print Function - HackerRank #######
###########################################

#Imprimir los numeros consecutivos desde el 1 hasta el numero que se ingrese por consola
if __name__ == '__main__':
    n = int(input())
#Sin ningun metodo de cadena, se usa un un para y se convierete el resultado en cadena(string)
#Se guarda en la variable llamada resultado

resultado=("")
for i in range (1,n+1):

    resultado+=str(i)
print(resultado)

#Se imprime el resultado

# Developed by: Maria Alejandra Gomez Archila - ID.1005234916

