import adafruit_dht
import RPi.GPIO as GPIO
import time
import board

dht_device = adafruit_dht.DHT22(board.D7)

while TRUE:
    try:
        temperatur_c =dht_device.temperatur
        humidity = dht_device.humidity

        print('Temp:{:.lf} C Humidity: {}%',format(temperatur_c, humidity))
    except RecursionError as err:
        print(err.args[0])

    time.sleep(2.0)