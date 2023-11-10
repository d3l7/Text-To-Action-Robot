#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from time import sleep as sl
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
#test_motor = Motor(Port.B)

# Write your program here

ev3.screen.draw_text(40, 50, ("I am sentient"))
sl(5)

# Play a sound.
ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 90)
sl(5)
# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)