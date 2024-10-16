# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
# Pedir al usuario que ingrese una operación (+, -, *, /)
operacion = input("Ingrese la operación (+, -, *, /): ")

# Usar match para realizar la operación correspondiente
match operacion:
    case "+":
        resultado = numero1 + numero2
        print(f"El resultado de {numero1} + {numero2} es {resultado}")
    case "-":
        resultado = numero1 - numero2
        print(f"El resultado de {numero1} - {numero2} es {resultado}")
    case "*":
        resultado = numero1 * numero2
        print(f"El resultado de {numero1} * {numero2} es {resultado}")
    case "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de {numero1} / {numero2} es {resultado}")
        else:
            print("Error: División por cero no permitida.")
    case _:
        print("Operación no válida.")
