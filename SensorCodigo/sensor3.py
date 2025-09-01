# Crear objeto
from ArduinoReader import ArduinoReader


# Distancia 5cm

arduino = ArduinoReader(port='/dev/ttyACM0', baud_rate=9600, output_file="100.txt")

# Conectar al Arduino
arduino.connect()

# Leer 10 datos y guardar
arduino.read_data(num_captures=10, prefix_length=10)

# Cerrar conexión
arduino.close()

# Leer los datos guardados con NumPy
datos100 = arduino.read_file()                    #Datos 5 es un arreglo de numpy
print("Datos leídos desde el archivo:", datos100)



