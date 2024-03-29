# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [CircuirPython_LED](#CircuitPython_LED)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Ultrasonic](#CircuitPython_Ultrasonic)
* [CircuitPython_Motor_Control](#CircuitPython_Motor_Control)
* [CircuitPython_Photointerrupter](#CircuitPythontor_Control)
* [NextAssignmentGoesHere](#NextAssignment)
* [Hanger](#hanger)
* [Swing Arm](#swing-arm)
---

## CircuitPython_LED

### Description & Code Snippets
The goal for this assignment was to get the LED working the same as we could on the arduino. However, due to some unforseen problems with circuit python we ended up using the neopixel instead. This code assigns the necessary values to the neopixel and then output the rainbow to the neopixel.


**Lastly, please end this section with a link to your code or file.**  
```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.NEOPIXEL

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 10

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
```

### Evidence


https://github.com/SempronChip/engr3/assets/143545309/e74b0bae-ce39-4a23-b4f0-3eb728cfd7ae

Credit goes to 
[Gaby D.](https://github.com/gdaless20/Circuitpython)

### Wiring

There is no wiring for this assignment.

### Reflection
Getting the circuit python setup was difficult, and if I were to do this again I would skip the step of using Mu. Overall, it wasn't hard to complete this assignment because the code was supplied to us and there was no wiring.

---

## CircuitPython_Servo

### Description & Code Snippets
The goal of this assignment was to wire a servo to move with capacitive touch from two wires. The overall idea was vague, but it wasn't to hard to find and modify two pieces of code from adafruit to achieve our goal.

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch on two pins example. Does not work on Trinket M0!"""
import time
import board
import touchio
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

touch_A4 = touchio.TouchIn(board.A4)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

while True:
    my_servo.throttle = 0.0
    while touch_A4.value:
        my_servo.throttle = 1.0
        time.sleep(.5)
    while touch_A5.value:
        my_servo.throttle = -1.0
        time.sleep(.5)
```

 


### Evidence




https://github.com/SempronChip/engr3/assets/143545309/1ec9ff0a-86fa-490e-8872-825861b4730b
Credit goes to Chris



### Wiring



### Reflection
It wasn't too challanging to complete this assignment, especially when I released that all I needed to do was combine two pieces of code that were availible online.

---
## CircuitPython_DistanceSensor

### Description & Code Snippets
The goal of this assignment is to make the neopixel change color based on the distances reported by the ultrasonic sensor. This assignment was accomplished by modifying the previous code we had for the neopixel to include the if statements and distance sensor.
```python
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
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255, 0,0)
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()
             
        if sonar.distance > 20 and sonar.distance < 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, (sonar.distance - 5 / 15 * 255), 255-(sonar.distance - 5 / 15 * 255))
                pixels.show()
        if sonar.distance > 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, 255, 0)
                pixels.show()   
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

**Lastly, please end this section with a link to your code or file.**  


### Evidence



https://github.com/SempronChip/engr3/assets/143545309/ccb16e40-9ffd-4550-babf-442d1a91b850
Credit goes to Chris


### Wiring
![](https://github.com/SempronChip/engr3/blob/v1/images/134725601-72db0fcb-0d50-486c-aff5-9e0ec1772057.png?raw=true)

Image credit goes to [Gaby D](https://github.com/gdaless20/Circuitpython/blob/main/README.md)

### Reflection
The table that Mr. H provided helped me greatly in writing the if statements for the neopixels. Otherwise, the project really wasn't that difficult and I was able to complete it quite easily.

---


## CircuitPython_Motor_Control

### Description & Code Snippets
The code wasn't too hard, as it is only a few lines. This takes the value from the potentiometer and sends it to the motor. 

```python
import board
import analogio

motor = analogio.AnalogOut(board.A0)
pot = analogio.AnalogIn(board.A1)
while True:
    speed = pot.value
    motor.value = speed
```

**Lastly, please end this section with a link to your code or file.**  

### Evidence


https://github.com/SempronChip/engr3/assets/143545309/15a4333c-a8c2-4cba-8b52-bf43765f76a8
Credit goes to Chris


### Wiring
![277456149-4862d20c-f2ed-4b43-95a4-555abaf82cd6](https://github.com/SempronChip/engr3/assets/143545309/6fb0ca37-a0aa-448e-a162-6938d98fd2b8)


Image credit goes to [Raffi Chen](https://github.com/Raffi-Chen/engr3)
### Reflection
The hardest part of this assignment was getting the wiring right. Eventhough I had gotten it checked by Mr. Miller, it still wouldn't work. Finally, I got it to work by rewiring a couple times in a couple different ways.

---

## CircuitPython_Photointerrupter

### Description & Code Snippets
The photointerrupter was quite easy because I remembered how wire it from last year. The code works by counting the number of times the photointerrupter is interrupted and prints this to the console every four seconds.

```python
from digitalio import DigitalInOut, Direction, Pull
import time
import board
initial = time.monotonic()
interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    now = time.monotonic()
    if now - initial >= 4:
        print("Number of interrupts:", str(counter))
        initial = now 
    time.sleep(0.1)
```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
![](https://github.com/SempronChip/engr3/blob/v1/images/149255410-87310b2a-6b4f-47cb-8991-7d1b8a96b390.png?raw=true)
Image credit goes to [Gaby D](https://github.com/gdaless20/Circuitpython/blob/main/README.md)
### Reflection
The code is quite simple when you use the provided time.monotonic(). Personally, I think that every four seconds is too short and I would prefer it to only update when the photo interrupter is interrupted. 

---
## Onshape_Assignments


## Hanger
### Assignment Description

The goal of this assignment was to follow the design documents to make a hanger with a mass matching the specified mass when it is the specified material.

### Evidence

![](https://github.com/SempronChip/engr3/blob/v1/images/hanger1.PNG?raw=true)
![](https://github.com/SempronChip/engr3/blob/v1/images/hanger2.PNG?raw=true)
![](https://github.com/SempronChip/engr3/blob/v1/images/hanger3.PNG?raw=true)

### Part Link 

[Part link](https://cvilleschools.onshape.com/documents/8057ebd5d9b38c8f2430aecc/w/067bc3ddabf178a107c83aec/e/69e7dbda5d55beacc3def062?renderMode=0&uiState=65318020be43fe7ca907add7)


### Reflection

After a whole summer using Fusion 360, I was surprised at how unintuitive onshape is. However, once I got acclimated to the oddities of onshape I was able to complete this assignment with ease.

---
## Swing Arm

### Assignment Description

The goal of this assignment was to recreate the part detailed in the design documents. The difference being this assignment had variables for certain values which would need to be changed in the second step. These variables would also change the mass of part for the second step. 

### Evidence
![](https://github.com/SempronChip/engr3/blob/v1/images/swing%20arm2.PNG?raw=true)
![](https://github.com/SempronChip/engr3/blob/v1/images/swing%20arm1.PNG?raw=true)

### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/560705bc2a50c2e2a6ef6800/w/fe33308f69e8a464a53700c8/e/09e967bfbe2ea9cb0f361a7d?renderMode=0&uiState=6536c69cea508a73f24262ce)

### Reflection

The swing arm wasn't very hard for me once I got the first sketch correct, as many problems can arise from the variables if you don't make the first sketch correctly. I ended up helping numerous people complete the assignment when they ran into problems as well.

---

&nbsp;
## CAD - Onshape Certification 1: Single Part

### Assignment Description

The goal of this assignment was to create a V-Block based on the given drawings. Then one would modify the part based on the instructions, to produce a part with the desired ms

### Evidence

![](images/O'NeillRossouwJ_20240326_ENGR_0006.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0007.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0008.png)

### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/d1887646d8bd37cf0571a8e1/w/c4f78c61437348b9a080d421/e/01c05bfbd124e63968bffdd8)

### Reflection

The part was very easy to create using the documents and was a good reintroduction to using onshape for CAD. One problem I did run into was getting the angle correct between iterations. However, I eventually was able to correct my mistake in my second attempt at the assignment which allowed me to complete the assignment.

---

&nbsp;
## CAD - Onshape Certification 2: Multi-Part

### Assignment Description

The goal of this assignment is to create a mic stand using multiple parts in one studio. This was an important introduction to making multiple parts in one studio instead of multiple different studios which don't have any shared dimensions.

### Evidence

![](images/O'NeillRossouwJ_20240326_ENGR_0004.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0005.png)


### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/9b2602dc4f0b56b5cc27ce6a/w/ebcd7ead231ea9063dc1c773/e/4228cf218bf42de18b0073d8)

### Reflection

This assignment was simple to make the first time through. However, for the second drawing, I realized that my base was incorrectly dimensioned and I had to go back and redo the sketches for the base. After redoing the sketch I realized that my original mass was slightly off from the actual mass, so I had designed the part incorrectly the first time.

---

&nbsp;
## CAD - Onshape Certification 3: Assemblies

### Assignment Description

The goal of this assignment to assemble a locking plier assembly to match the drawings with the provided parts. This assignment was an important practice for assembling the parts so that they can interact in their intended way.
### Evidence

![](images/O'NeillRossouwJ_20240326_ENGR_0000.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0001.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0002.png)

### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/4ad6c147d972284340a55101/w/b63db74e90ddff8caad7b651/e/bb2b58a578fe3bf00d50f4c3)

### Reflection

I originally struggled with getting the mates between the parts to match the intended ones. However, I eventually reached a solution that produced the desired results, only to find out in later parts that it wasn't the correct mate. Overall, this assignment was very important for understanding how to use mates to produce the desired interactions between parts.

---

&nbsp;
## CAD - Onshape Multi-Part

### Assignment Description

The goal of this assignment to create a cylinder assembly using multiple parts within one studio. This was important for practicing how to make multiple parts from their shared dimensions.

### Evidence

![](images/O'NeillRossouwJ_20240326_ENGR_0009.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0010.png)
![](images/O'NeillRossouwJ_20240326_ENGR_0011.png)

### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/9b2602dc4f0b56b5cc27ce6a/w/ebcd7ead231ea9063dc1c773/e/4228cf218bf42de18b0073d8)

### Reflection

The first part of this assignment was relatively easy, as constructing the parts from their shared geometry was simple. However, I would run into trouble in the next drawings because the way that I constructed the parts in the first drawings didn't allow me to make the changes I needed to make in the subsequent drawings. Overall, this assignment was important for me to understand that I need to design the parts the most efficient way the first time so I don't have to go back and make changes.
&nbsp;
## Code - Rotary Encoder + LCD

### Assignment Description

This assignment aimed to create a menu-controlled traffic light using an Arduino, rotary encoder, and the onboard neopixel. The menu needed to have items for stop, go, and caution and be able to switch to the corresponding light color on the neopixel.

### Evidence

### Wiring Diagram


### Code
```python
# Rotary Encodare light thingksf;ja             # [lines 1-7] Import and set up neccesary libraries
import time
import rotaryio
import neopixel
import board
from lcd import LCD
from i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull


encoder = rotaryio.IncrementalEncoder(board.D4, board.D3) # [lines 9-24] Start all Variables and define INs and OUTs
last_position = 0
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Button = 1
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .3
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)





while True:                #[lines 27-38] Set up varible for encoder, limit it to >0 and <3
    position = encoder.position
    if position != last_position:
        state = position % 3
        if state == 0:     #[lines 39-47] Print to LCD based on Encoder Var
            lcd.clear()
            lcd.set_cursor_pos(0, 0) # [39
            lcd.print("Don't stop")
        elif state == 1:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Speed up")
        elif state == 2:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Slam on brakes")
    if btn.value == 0 and Button == 1: #[lines 48-63] If the button is pressed make the Encoder Var match the lights.
        print("buttion")
        if state == 0: 
            print('g')
            led[0] = (0, 255, 0)
        elif state == 1:
            print('y')
            led[0] = (255, 234, 0)
        elif state == 2:
            print('r')
            led[0] = (250, 0, 0)
        Button = 0       #[lines 64-68] Resets and delay
    if btn.value == 1:
        time.sleep(.1)
        Button = 1
    last_position = position
```

### Reflection

This assignment was the product of a collaborative effort between me and Asher. This allowed us to hammer out this assignment in the course of one class, but we did run into a few problems with the method for tracking the location of the rotary encoder. I found it very interesting that this assignment was a repeat from last year, but written in circuit Python instead of Arduino code.

---

&nbsp;
## Code - Stepper Motor + Limit Switch

### Assignment Description

The goal of this assignment was to program a stepper motor to rotate until it touches the limit switch and then rotate 180 degrees in reverse when it contacts with the motor arm. This assignment was important as it teaches one to use the stepper motor which will come in handy for the robot arm project.

### Evidence

### Wiring Diagram
![](images/Steppermotor.jpeg)

### Code
```python

import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper


DELAY = 0.01  
STEPS = 100
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)


for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):

    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        motor_task = asyncio.create_task(run_motor())
        await asyncio.gather(interrupt_task, motor_task)

asyncio.run(main())
```

### Reflection

This assignment was the product of a collaborative effort between me and Asher. This allowed us to hammer out this assignment in the course of one class, but we did run into a few problems with the method for tracking the location of the rotary encoder. I found it very interesting that this assignment was a repeat from last year, but written in circuit Python instead of Arduino code.

---

&nbsp;
## Code - IR Sensor

### Assignment Description

### Evidence

### Wiring Diagram
![](images/Steppermotor.jpeg)

### Code
```python
# Import libraries
import board
import digitalio
import neopixel 

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

# Set up the IR Sensor using digital pin 2. 
ir_sensor = digitalio.DigitalInOut(board.D2)
ir_sensor.direction = digitalio.Direction.INPUT # Set the IR sensor as an input.
ir_sensor.pull = digitalio.Pull.UP              # Use the internal pull-up resistor.


# While loop runs the code inside continuously. 
while True:
    print(ir_sensor.value)
    if ir_sensor.value == False:
        led[0] = (255, 0, 0)
    if ir_sensor.value == True:
        led[0] = (0, 255, 0)
```
### Reflection

&nbsp;
## Grabber

### Assignment Description

The goal of this assignment was to create a robot arm that could function with one actuator and could be animated in onshape. In addition, a bill of materials needed to be created that depicted the named parts. 

### Evidence
![](https://github.com/SempronChip/engr3/blob/3b37db9194ab76754ea50a50e871ed8d5153c0e2/images/gripperView1.PNG)
![](https://github.com/SempronChip/engr3/blob/3b37db9194ab76754ea50a50e871ed8d5153c0e2/images/ezgif.com-video-to-gif-converter.gif)
![](https://github.com/SempronChip/engr3/blob/3b37db9194ab76754ea50a50e871ed8d5153c0e2/images/bom.PNG)
### Part Link 

[Part Link](https://cvilleschools.onshape.com/documents/c487340cfe2371c24836f18d/w/8b0571f6a2cf9f4be29b6a26/e/dcde9d44d2c86d2fafb08966?renderMode=0&uiState=65cbc4ea52a1742c99078fe2)

### Reflection

The grabber was simple enough to create because it didn't have any specific size dimensions. The hardest part was finding a feature that worked correctly to create the desired globoid gears.

---

&nbsp;


