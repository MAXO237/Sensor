import matplotlib.pyplot as plt
import numpy
import os

def leer_flotantes(archivo):
    """
    Lee un archivo de texto donde cada línea contiene un número flotante
    y devuelve una lista de floats.
    """
    numeros = []
    with open(archivo, "r") as f:
        for linea in f:
            linea = linea.strip()  # quitar espacios y saltos de línea
            if linea:  # ignorar líneas vacías
                try:
                    numeros.append(float(linea))
                except ValueError:
                    print(f"Línea no válida ignorada: {linea}")
    return numeros

# Ejemplo de uso
# Ruta de la carpeta "Mediciones" relativa al archivo actual
BASE_DIR = os.path.dirname(__file__)
ruta = os.path.join(BASE_DIR, "Mediciones")

y5 = leer_flotantes(f"{ruta}/5.txt")
y15 = leer_flotantes(f"{ruta}/15.txt")
y25 = leer_flotantes(f"{ruta}/25.txt")
y35 = leer_flotantes(f"{ruta}/35.txt")
y45 = leer_flotantes(f"{ruta}/45.txt")
y55 = leer_flotantes(f"{ruta}/55.txt")
y65 = leer_flotantes(f"{ruta}/65.txt")
y75 = leer_flotantes(f"{ruta}/75.txt")
y85 = leer_flotantes(f"{ruta}/85.txt")
y95 = leer_flotantes(f"{ruta}/95.txt")
y100 = leer_flotantes(f"{ruta}/100.txt")


x5 = [5.0 for i in range (10)]
x15 = [15.0 for i in range (10)]
x25 = [25.0 for i in range(10)]
x35 = [35.0 for i in range(10)]
x45 = [45.0 for i in range(10)]
x55 = [55.0 for i in range(10)]
x65 = [65.0 for i in range(10)]
x75 = [75.0 for i in range(10)]
x85 = [85.0 for i in range(10)]
x95 = [95.0 for i in range(10)]
x100 = [100.0 for i in range(10)]



x = x5 + x15 + x25 + x35 + x45 + x55 + x65 + x75 + x85 + x95 + x100
y = y5 + y15 + y25 + y35 + y45 + y55 + y65 + y75 + y85 + y95 + y100

std5 = numpy.std(y100)
print(std5)

plt.scatter(x, y, color='blue', label='Puntos')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfica de puntos')
plt.legend()
plt.grid(True)
plt.show()


