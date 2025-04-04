#Raspberry PI 4 LED switch controll

import RPi.GPIO as GPIO
import time

# GPIO-Initialisierung
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Physische PIN-Nummern
LED_PIN = 37 # Ersetzen Sie durch den von Ihnen verwendeten physischen PIN
BUTTON_PIN = 11 # Ersetzen Sie durch den von Ihnen verwendeten physischen PIN

# Setup
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
    # Lesen des Tasterzustands
    button_state = GPIO.input(BUTTON_PIN)

    if button_state == GPIO.HIGH:
        # LED einschalten
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        # LED ausschalten
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1) # Kurze Verzögerung zur Entprellung
except KeyboardInterrupt:
    GPIO.cleanup()
