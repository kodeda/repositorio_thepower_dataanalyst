# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Solicita al usuario la temperatura en grados Celsius
temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convierte la temperatura a grados Fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Muestra el resultado
print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")
