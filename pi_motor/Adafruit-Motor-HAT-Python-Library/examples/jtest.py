#import paho.mqtt.client as mqtt
import json


msg = '''
{
    "cmd":"forward"
    "duration":6
}
'''

jsonCmd = json.loads(msg)
print(jsonCmd)
