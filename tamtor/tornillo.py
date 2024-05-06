def clasificar_tornillo(tamano):
    if 1.0 <= tamano < 3.0:
        return "El tornillo es pequeno."
    elif 3.0 <= tamano < 5.0:
        return "El tornillo es mediano."
    elif 5.0 <= tamano < 6.5:
        return "El tornillo es grande."
    elif 6.5 <= tamano < 8.5:
        return "El tornillo es muy grande."
    elif tamano >= 8.5:
        return "El tornillo es gigante."
    else:
        return "El tamano ingresado no es valido"

# Solicitar entrada al usuario
try:
    tamano_tornillo = float(input("Ingresa el tamaño del tornillo en centímetros: "))
    print(clasificar_tornillo(tamano_tornillo))
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")
