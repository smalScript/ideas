import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# GPIO-Initialisierung
GPIO.setmode(GPIO.BOARD) # Verwenden Sie die physische Pin-Nummerierung
GPIO.setwarnings(False)

# Sensor- und Pin-Konfiguration
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7 # Physischer Pin 7 entspricht GPIO 4 in BCM
try:
    while True:
        # Lesen der Temperatur und Luftfeuchtigkeit
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            # Ausgabe der Werte auf der Kommandozeile
            print(f"Temperatur: {temperature:.1f}°C Luftfeuchtigkeit: {humidity:.1f}%")

        else:
            print("Fehler beim Auslesen des Sensors")
            # Wartezeit zwischen den Messungen
            time.sleep(2)

except KeyboardInterrupt:
    print("Programm beendet")

finally:
    # GPIO-Pins aufräumen
    GPIO.cleanup()
