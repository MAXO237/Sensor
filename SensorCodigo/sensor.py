# Requiere pySerial:
# Instalar con: pip install pyserial

import serial
import numpy as np
from numpy import genfromtxt

# Ajusta este puerto según tu sistema:
#   - En Linux suele ser: /dev/ttyACM0 o /dev/ttyUSB0
#   - En Windows suele ser: COM3, COM4, etc.
serial_port = '/dev/ttyACM0'
baud_rate = 9600   # Debe coincidir con Serial.begin(9600) en Arduino
SERIAL_DATA_FILE = "output.txt"

# Abrir archivo para guardar los datos
output_file = open(SERIAL_DATA_FILE, "w")

# Conectar al puerto serial
ser = serial.Serial(serial_port, baud_rate)

num_captures = 10  # cuántos datos quieres capturar
print(f"Inicia lectura de {num_captures} datos:")

while num_captures > 0:
    line = ser.readline()  # Lee una línea desde Arduino
    line = line.decode("utf-8", errors="ignore").strip() # Convertir de bytes a string

    print(line)

    # A veces llegan datos incompletos, intentamos convertirlos
    try:
        num = float(line)  # Convertir a número
        print(num)
        numstr = str(num)
        output_file.write(line)  # Guardar en el archivo
        output_file.flush()
        num_captures -= 1
    except:
        pass


# Cerrar conexiones
ser.close()
output_file.close()

ent = input("Presione una tecla para leer el archivo")

# Leer el archivo con NumPy
data = np.genfromtxt(SERIAL_DATA_FILE)
print(data)
