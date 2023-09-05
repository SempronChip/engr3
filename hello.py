# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 1.0  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance > 5 and sonar.distance < 20:
            pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, 0) 
        if sonar.distance > 5 and sonar.distance < 20:
            pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, 0) 
        if sonar.distance > 5 and sonar.distance < 20:
            pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, 0) 
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
