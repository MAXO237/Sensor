import matplotlib.pyplot as plt
import numpy
import os
import statistics as stats

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

desv_poblacional5 = stats.pstdev(y5)
desv_poblacional15 = stats.pstdev(y15)
desv_poblacional25 = stats.pstdev(y25)
desv_poblacional35 = stats.pstdev(y35)
desv_poblacional45 = stats.pstdev(y45)
desv_poblacional55 = stats.pstdev(y55)
desv_poblacional65 = stats.pstdev(y65)
desv_poblacional75 = stats.pstdev(y75)
desv_poblacional85 = stats.pstdev(y85)
desv_poblacional95 = stats.pstdev(y95)
desv_poblacional100 = stats.pstdev(y100)

meany5 = stats.mean(y5)
meany15 = stats.mean(y15)
meany25 = stats.mean(y25)
meany35 = stats.mean(y35)
meany45 = stats.mean(y45)
meany55 = stats.mean(y55)
meany65 = stats.mean(y65)
meany75 = stats.mean(y75)
meany85 = stats.mean(y85)
meany95 = stats.mean(y95)
meany100 = stats.mean(y100)


y5 = y5 + [stats.mean(y5)]
y15 = y15 + [stats.mean(y15)]
y25 = y25 + [stats.mean(y25)]
y35 = y35 + [stats.mean(y35)]
y45 = y45 + [stats.mean(y45)]
y55 = y55 + [stats.mean(y55)]
y65 = y65 + [stats.mean(y65)]
y75 = y75 + [stats.mean(y75)]
y85 = y85 + [stats.mean(y85)]
y95 = y95 + [stats.mean(y95)]
y100 = y100 + [stats.mean(y100)]




x5 = [5.0 for i in range (11)]
x15 = [15.0 for i in range (11)]
x25 = [25.0 for i in range(11)]
x35 = [35.0 for i in range(11)]
x45 = [45.0 for i in range(11)]
x55 = [55.0 for i in range(11)]
x65 = [65.0 for i in range(11)]
x75 = [75.0 for i in range(11)]
x85 = [85.0 for i in range(11)]
x95 = [95.0 for i in range(11)]
x100 = [100.0 for i in range(11)]



x = x5 + x15 + x25 + x35 + x45 + x55 + x65 + x75 + x85 + x95 + x100
y = y5 + y15 + y25 + y35 + y45 + y55 + y65 + y75 + y85 + y95 + y100




# Dos puntos por los que pasará la línea
iniciolinea5 = (5,meany5-desv_poblacional5)
finlinea5 = (5, meany5+desv_poblacional5)

iniciolinea15 = (15, meany15 - desv_poblacional15)
finlinea15 = (15, meany15 + desv_poblacional15)

iniciolinea25 = (25, meany25 - desv_poblacional25)
finlinea25 = (25, meany25 + desv_poblacional25)

iniciolinea35 = (35, meany35 - desv_poblacional35)
finlinea35 = (35, meany35 + desv_poblacional35)

iniciolinea45 = (45, meany45 - desv_poblacional45)
finlinea45 = (45, meany45 + desv_poblacional45)

iniciolinea55 = (55, meany55 - desv_poblacional55)
finlinea55 = (55, meany55 + desv_poblacional55)

iniciolinea65 = (65, meany65 - desv_poblacional65)
finlinea65 = (65, meany65 + desv_poblacional65)

iniciolinea75 = (75, meany75 - desv_poblacional75)
finlinea75 = (75, meany75 + desv_poblacional75)

iniciolinea85 = (85, meany85 - desv_poblacional85)
finlinea85 = (85, meany85 + desv_poblacional85)

iniciolinea95 = (95, meany95 - desv_poblacional95)
finlinea95 = (95, meany95 + desv_poblacional95)

iniciolinea100 = (100,meany100-desv_poblacional100)
finlinea100 = (100, meany100+desv_poblacional100)

# Extraer coordenadas
x_linea5 = [iniciolinea5[0], finlinea5[0]]
y_linea5 = [iniciolinea5[1], finlinea5[1]]

x_linea15 = [iniciolinea15[0], finlinea15[0]]
y_linea15 = [iniciolinea15[1], finlinea15[1]]

x_linea25 = [iniciolinea25[0], finlinea25[0]]
y_linea25 = [iniciolinea25[1], finlinea25[1]]

x_linea35 = [iniciolinea35[0], finlinea35[0]]
y_linea35 = [iniciolinea35[1], finlinea35[1]]

x_linea45 = [iniciolinea45[0], finlinea45[0]]
y_linea45 = [iniciolinea45[1], finlinea45[1]]

x_linea55 = [iniciolinea55[0], finlinea55[0]]
y_linea55 = [iniciolinea55[1], finlinea55[1]]

x_linea65 = [iniciolinea65[0], finlinea65[0]]
y_linea65 = [iniciolinea65[1], finlinea65[1]]

x_linea75 = [iniciolinea75[0], finlinea75[0]]
y_linea75 = [iniciolinea75[1], finlinea75[1]]

x_linea85 = [iniciolinea85[0], finlinea85[0]]
y_linea85 = [iniciolinea85[1], finlinea85[1]]

x_linea95 = [iniciolinea95[0], finlinea95[0]]
y_linea95 = [iniciolinea95[1], finlinea95[1]]

x_linea100 = [iniciolinea100[0], finlinea100[0]]
y_linea100 = [iniciolinea100[1], finlinea100[1]]


plt.scatter(x, y, color='blue', label='Puntos')

plt.plot(x_linea5, y_linea5, color='red')
plt.plot(x_linea15, y_linea15, color='red')
plt.plot(x_linea25, y_linea25, color='red')
plt.plot(x_linea35, y_linea35, color='red')
plt.plot(x_linea45, y_linea45, color='red')
plt.plot(x_linea55, y_linea55, color='red')
plt.plot(x_linea65, y_linea65, color='red')
plt.plot(x_linea75, y_linea75, color='red')
plt.plot(x_linea85, y_linea85, color='red')
plt.plot(x_linea95, y_linea95, color='red')
plt.plot(x_linea100, y_linea100, color='red')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfica de puntos')
plt.legend()
plt.grid(True)
plt.show()









