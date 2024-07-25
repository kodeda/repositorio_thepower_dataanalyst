# Función para calcular el monto total incluyendo propina
def calcular_total_con_propina(monto_cuenta, porcentaje_propina=15):
    propina = monto_cuenta * (porcentaje_propina / 100)
    total = monto_cuenta + propina
    return total

# Solicitar al usuario el monto de la cuenta
monto_cuenta = float(input("Introduce el monto de la cuenta en el restaurante: "))

# Calcular el monto total con propina
monto_total = calcular_total_con_propina(monto_cuenta)

# Mostrar el resultado
print(f"El monto total a pagar, incluyendo una propina del 15%, es: {monto_total:.2f}")
