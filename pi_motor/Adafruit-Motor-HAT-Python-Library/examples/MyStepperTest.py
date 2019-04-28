#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    print("motor release")
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
print("setup")
myStepper = mh.getStepper(500, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(900)             # 30 RPM


print("wiggle test")
while (True):
    print("forward")
    myStepper.step(500, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
    #print("backward")
    #myStepper.step(10, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    #time.sleep(1)
    # print("Single coil steps")
    # myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    # myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

    #print("Double coil steps")
    #myStepper.step(500, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
    # myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

    # print("Interleaved coil steps")
    # myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
    # myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

    # print("Microsteps")
    # myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
    # myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
