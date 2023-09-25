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