import wiotp.sdk.device
import time
import os
import datrtime
import random
myConfig = { 
    "identity": {
        "orgId": "vut8fi",
        "typeId": "NodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="motorON"):
     print("Motor is switched OFF")
    print("")

while True:
    temp=random.randint(-20,125)
    soil=random.randint(0,100)
    hum=random.randint(0,100)
    myData={'temperature':temp, 'soil_moisture':soil, 'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
    client.commandcallback=mycommandcallback
client.disconnect()
