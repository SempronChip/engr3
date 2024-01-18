"""
Engineering 3 
Limit Switch + Stepper Motor STARTER CODE

"""

# Imports the needed libraries for your board. 
import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper


DELAY = 0.01   # Sets the delay time for in-between each step of the stepper motor.
STEPS = 100    # Sets the number of steps. 100 is half a full rotation for the motor we're using. 

# Set up the digital pins used for the four wires of the stepper motor. 
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

# Sets each of the digital pins as an output.
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

# Creates an instance of the stepper motor so you can send commands to it (using the Adafruit Motor library). 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


async def catch_pin_transitions(pin):
    # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    # FILL THIS IN: MAKE THE MOTOR ARM SPIN BACKWARDS. 
                

                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        # FILL THIS IN: 
        # MAKE THE MOTOR SPIN FORWARD.


            await asyncio.sleep(0)

async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))

        # FILL THIS IN: 
        # CREATE ANOTHER TASK CALLED: motor_task.
        # USE asyncio.create_task() to call the run_motor() function you wrote.

        await asyncio.gather(interrupt_task, motor_task)

asyncio.run(main())
