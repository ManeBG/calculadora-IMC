"""
Calculadora del Índice de Masa Corporal (IMC)
Autor: Manuel BG
Descripción: Este script calcula el Índice de Masa Corporal (IMC) basado en el peso 
y la altura proporcionados por el usuario.
"""

# Formulas para el calculo.


def calculo_IMC(peso, altura):
    """Operacion que calcula el IMC"""
    return peso / (altura ** 2)


def clasificacion_IMC(IMC):
    """Categorias del IMC"""
    if IMC < 18.5:
        return "Bajo peso, cuidar alimentacion."
    elif 18.5 <= IMC < 24.9:
        return "Peso normal, felicidades!"
    elif 25 <= IMC < 29.9:
        return "Sobrepeso, hay que cuidarse."
    else:
        return "Obesidad, debes hacer algo para mejorar."


# Solicitud de datos con manejo de errores.
while True:
    """
    Solicitar el nombre al usuario y asegurarse de que no haya espacios innecesario.
    Convertir la primera letra en mayuscula y el resto en minuscula
    """
    nombre = input("¿Cuál es tu nombre? ").strip()
    if nombre:
        nombre = nombre[0].upper() + nombre[1:].lower()
        break
    else:
        print("Por favor, ingresa tu nombre.")


while True:
    """
    Solicitar el peso al usuario y manejar errores si no se ingresa un valor numérico válido.
    """
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        break
    except ValueError:
        print("Error: Ingresa un valor numérico válido para el peso.")


while True:
    """
    Solicitar la altura al usuario y manejar errores si no se ingresa un valor numérico válido.
    """
    try:
        altura = float(input("Ingrese su altura en metros: "))
        break
    except ValueError:
        print("Error: Ingresa un valor numérico válido para la altura.")

# Solicitudes de datos del usuario.
# nombre = input("¿Cual es tu nombre? ").capitalize()
# peso = float(input("Ingrese su peso en kilogramos: "))
# altura = float(input("Ingrese su altura en metros: "))


# Magia para el calculo y clasificacion del IMC
IMC = calculo_IMC(peso, altura)
clasificacion = clasificacion_IMC(IMC)


# Salida de resultados.
print(f"{nombre}, su indice de masa corporal es: {IMC:.2f}")
print(f"Estado de salud según el IMC: {clasificacion}")
