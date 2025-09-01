import serial
import time
import numpy as np

class ArduinoReader:
    def __init__(self, port='/dev/ttyACM0', baud_rate=9600, output_file="output.txt"):
        """
        Inicializa la configuración del puerto serie y archivo de salida.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.output_file = output_file
        self.ser = None

    def connect(self):
        """Conecta al Arduino y espera 2 segundos para estabilizar la comunicación."""
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=1)
        time.sleep(2)

    def read_data(self, num_captures=10, prefix_length=10):
        """
        Lee num_captures datos del Arduino, quita los primeros prefix_length caracteres,
        convierte a float y los guarda en el archivo.
        """
        if self.ser is None:
            raise Exception("Puerto serie no conectado. Usa connect() primero.")

        with open(self.output_file, "w") as f:
            captured = 0
            print(f"Capturando {num_captures} valores desde Arduino...")
            while captured < num_captures:
                try:
                    line = self.ser.readline().decode("utf-8", errors="ignore").strip()
                    if line:
                        # Quitar prefijo
                        line = line[prefix_length:]
                        try:
                            num = float(line)
                            print(f"Dato válido: {num}")
                            f.write(f"{num}\n")
                            f.flush()
                            captured += 1
                        except ValueError:
                            print(f"Dato no válido: {line}")
                except Exception as e:
                    print(f"Error: {e}")
                    break

    def close(self):
        """Cierra la conexión con Arduino."""
        if self.ser is not None:
            self.ser.close()
            self.ser = None

    def read_file(self):
        """Lee los datos guardados en el archivo usando NumPy."""
        data = np.genfromtxt(self.output_file)
        return data
