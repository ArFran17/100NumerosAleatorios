import math

# Método de Centros al Cuadrado
def centros_al_cuadrado(semilla, n_digitos, cantidad):
    numeros = []
    for _ in range(cantidad):
        # Elevar al cuadrado la semilla
        semilla_cuadrada = str(semilla ** 2).zfill(2 * n_digitos)
        
        # Obtener los dígitos centrales
        mitad = len(semilla_cuadrada) // 2
        inicio = mitad - n_digitos // 2
        fin = inicio + n_digitos
        semilla = int(semilla_cuadrada[inicio:fin])
        
        # Normalizar el valor (hacerlo entre 0 y 1)
        numeros.append(semilla / (10 ** n_digitos))
        
    return numeros

# Método de los Medios Cuadrados
def medios_cuadrados(semilla1, semilla2, n_digitos, cantidad):
    numeros = []
    for _ in range(cantidad):
        # Multiplicar las dos semillas
        producto = str(semilla1 * semilla2).zfill(2 * n_digitos)
        
        # Obtener los dígitos centrales
        mitad = len(producto) // 2
        inicio = mitad - n_digitos // 2
        fin = inicio + n_digitos
        nuevo_valor = int(producto[inicio:fin])
        
        # Almacenar el número generado
        numeros.append(nuevo_valor / (10 ** n_digitos))
        
        # Actualizar las semillas
        semilla1, semilla2 = semilla2, nuevo_valor
        
    return numeros

# Parámetros
semilla_centros = 1234
semilla_medios1 = 1234
semilla_medios2 = 5678
n_digitos = 4
cantidad = 100

# Generar los 100 números con cada método
numeros_centros = centros_al_cuadrado(semilla_centros, n_digitos, cantidad)
numeros_medios = medios_cuadrados(semilla_medios1, semilla_medios2, n_digitos, cantidad)

# Mostrar los resultados
print("Números generados por el método de Centros al Cuadrado:")
print(numeros_centros)

print("\nNúmeros generados por el método de Medios Cuadrados:")
print(numeros_medios)