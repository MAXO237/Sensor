import serial
import time
import numpy as np

# Configuración del puerto serie
serial_port = '/dev/ttyACM0'  # Ajustar según tu SO
baud_rate = 9600
SERIAL_DATA_FILE = "output.txt"

# Abrir conexión
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# A veces Arduino reinicia al conectar, espera 2 segundos
time.sleep(2)

# Abrir archivo en modo escritura
with open(SERIAL_DATA_FILE, "w") as output_file:
    num_captures = 10
    print(f"Capturando {num_captures} valores desde Arduino...")

    while num_captures > 0:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            line = line[10:]
            if line:  # si no está vacío
                
                try:
                    num = float(line)  # intentar convertir a número
                
                    print(f"Dato válido: {num}")
                    
                    output_file.write(f"{num}\n")  # guardar con salto de línea
                    
                    output_file.flush()
                    num_captures -= 1
                except ValueError:
                    print(f"Dato no válido: {line}")
        except Exception as e:
            print(f"Error: {e}")
            break

# Cerrar puerto
ser.close()

print("\nLectura finalizada. Ahora leyendo con NumPy...")

# Leer archivo con NumPy
data = np.genfromtxt(SERIAL_DATA_FILE)
print("Datos guardados en numpy array:")
print(data)
