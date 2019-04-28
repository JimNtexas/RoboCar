import paho.mqtt.client as mqtt
import json
import Robot2

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

    payload = str(msg.payload)
    print(payload)
    jsonCmd = json.loads(payload)  # type: object
    cmd = jsonCmd['command']
    duration = jsonCmd['duration']
    if(cmd == "forward"):
        speed = jsonCmd["left_speed"]
        robot.forward(speed, duration)

    elif(cmd == "backwards"):
            speed = jsonCmd["left_speed"]
            robot.backward(speed, duration)

    elif(cmd == "left"):
        speed = jsonCmd["right_speed"]
        robot.right(speed, 1)

    elif (cmd == "right"):
        speed = jsonCmd["left_speed"]
        robot.left(speed, 1)

    elif (cmd == "stop"):
            robot.stop()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()