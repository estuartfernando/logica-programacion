import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    # Base de caracteres: minúsculas
    caracteres = string.ascii_lowercase

    # Variables para cada tipo de caracteres
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # Agregamos cada categoría según la preferencia
    if incluir_mayusculas:
        caracteres += mayusculas
    if incluir_numeros:
        caracteres += numeros
    if incluir_simbolos:
        caracteres += simbolos

    # Si no se agregó nada extra, caracteres solo son minúsculas

    # Generamos la contraseña eligiendo caracteres aleatorios
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña


LONGITUD_REQUERIDA = 10

while True:
    entrada = input(f"Ingrese la longitud de la contraseña (debe ser {LONGITUD_REQUERIDA}): ")
    try:
        longitud = int(entrada)
        if longitud != LONGITUD_REQUERIDA:
            print(f"❌ Error: La contraseña debe tener exactamente {LONGITUD_REQUERIDA} caracteres.")
        else:
            break
    except ValueError:
        print("❌ Error: Por favor, introduce un número válido.")

usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
usar_nums = input("¿Incluir números? (s/n): ").lower() == 's'
usar_simb = input("¿Incluir símbolos? (s/n): ").lower() == 's'

resultado = generar_contraseña(longitud, usar_mayus, usar_nums, usar_simb)
print("✅ Contraseña generada:", resultado)