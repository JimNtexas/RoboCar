import paho.mqtt.client as mqtt
# based on:
# Simple two DC motor robot class usage example.
# Author: Tony DiCola
# License: MIT License https://opensource.org/licenses/MIT
import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot2

# Set the trim offset for each motor (left and right).  This is a value that
# will offset the speed of movement of each motor in order to make them both
# move at the same desired speed.  Because there's no feedback the robot doesn't
# know how fast each motor is spinning and the robot can pull to a side if one
# motor spins faster than the other motor.  To determine the trim values move the
# robot forward slowly (around 100 speed) and watch if it veers to the left or
# right.  If it veers left then the _right_ motor is spinning faster so try
# setting RIGHT_TRIM to a small negative value, like -5, to slow down the right
# motor.  Likewise if it veers right then adjust the _left_ motor trim to a small
# negative value.  Increase or decrease the trim value until the bot moves
# straight forward/backward.

MQTT_SERVER = "roboberry"
MQTT_PATH = "car_command"
LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot2.Robot2(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("msg: " + msg.topic + " " + str(msg.payload))
    # more callbacks, etc
    if(str(msg.payload) == "forward" ):
        leftspeed = 75
        rightspeed = 75
        print("speeds - left: " + str(leftspeed) + " right: " + str(rightspeed))
        robot.setboth(leftspeed,rightspeed,5, False)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()