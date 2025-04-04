#Raspberry PI 4 LED controll

import RPi.GPIO as GPIO
import time
# GPIO-Initialisierung
GPIO.setmode(GPIO.BCM) # Verwenden Sie die BCM-Nummerierung
GPIO.setwarnings(False)
# Ersetzen Sie '26' durch den von Ihnen verwendeten GPIO-Pin
LED_PIN = 26
GPIO.setup(LED_PIN, GPIO.OUT)
try:
    
    while True:
        # LED einschalten
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(2) # 2 Sekunden an
        # LED ausschalten
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1) # 1 Sekunde aus
except KeyboardInterrupt:
    # Aufräumen bei Programmende
    GPIO.cleanup()
