import random
import string

def generar_contraseña(longitud, opciones):
    tipos_caracteres = {
        "minusculas": list(string.ascii_lowercase),
        "mayusculas": list(string.ascii_uppercase),
        "numeros": list(string.digits),
        "simbolos": list(string.punctuation)
    }

    caracteres_permitidos = tipos_caracteres["minusculas"][:]  # Copia para incluir siempre minúsculas

    if opciones["mayusculas"]:
        caracteres_permitidos.extend(tipos_caracteres["mayusculas"])
    if opciones["numeros"]:
        caracteres_permitidos.extend(tipos_caracteres["numeros"])
    if opciones["simbolos"]:
        caracteres_permitidos.extend(tipos_caracteres["simbolos"])

    contraseña = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud))
    return contraseña

# Longitud fija requerida
LONGITUD_REQUERIDA = 16

# Solicitar longitud al usuario
longitud = 0
while longitud != LONGITUD_REQUERIDA:
    entrada = input(f"Ingrese la longitud de la contraseña (debe ser {LONGITUD_REQUERIDA}): ")
    try:
        longitud = int(entrada)
        if longitud != LONGITUD_REQUERIDA:
            print(f"❌ Error: La contraseña debe tener exactamente {LONGITUD_REQUERIDA} caracteres.")
    except ValueError:
        print("❌ Error: Por favor, introduce un número válido.")

# Función para validar entrada 's' o 'n'
def pedir_opcion(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("❌ Error: Responde solo con 's' (sí) o 'n' (no).")

# Pedir opciones al usuario con validación
opciones_usuario = {
    "mayusculas": pedir_opcion("¿Incluir mayúsculas? (s/n): "),
    "numeros": pedir_opcion("¿Incluir números? (s/n): "),
    "simbolos": pedir_opcion("¿Incluir símbolos? (s/n): ")
}

# Generar y mostrar la contraseña
contraseña_final = generar_contraseña(longitud, opciones_usuario)
print("✅ Contraseña generada:", contraseña_final)
