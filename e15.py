# Solicitar el salario bruto y el país de residencia al usuario
salario_bruto = float(input("Introduce tu salario bruto: "))
pais_residencia = input("Introduce tu país de residencia (País A, País B, País C): ")

# Usar match para aplicar el porcentaje de impuestos según el país
match pais_residencia:
    case "País A":
        impuesto = 0.20
    case "País B":
        impuesto = 0.15
    case "País C":
        impuesto = 0.10
    case _:
        impuesto = 0.25  # Impuesto para países no listados

# Calcular el salario neto
salario_neto = salario_bruto * (1 - impuesto)

# Mostrar el resultado
print(f"Tu salario neto después de impuestos es: {salario_neto:.2f}")
