#Escribe un programa que verifique si un número es par o impar utilizando if

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Verificar si el número es impar o par
if (numero % 2 == 0):
 print(f"El número {numero} es par..")
else :
 print(f"El número {numero} no es par.")