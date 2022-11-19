import json
import collections
import wiotp.sdk.device
import time
myConfig = {
    "identity" : {
        "orgId" :"cri1at",
        "typeId" : "NodeMCU",
        "deviceId" : "12345"
    },
    "auth":{
        "token":"12345678"
        }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig ,logHandlers=None)
client.connect()
while True:

    #Dumster location Thanjavur Big Temple
    #latitude = 10.7828
    #longitude = 79.1318
    #weight=0

    
    #dumsterLocation SARANATHAN COLLEGE OF ENGINEERING
    latitude = 10.7560
    longitude = 78.6513
    weight=57

    
    #dumsterLocation Trichy central bus stand
    #latitude = 10.798523
    #longitude = 78.680381
    #weight=80

    
    #dumsterLocation Thanjavur new bustand
    #latitude = 10.749894
    #longitude = 79.112159
    #weight=60


    
    myData = {'latitude' :latitude, 'longitude':longitude,'weight':weight}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform : ",myData)
    time.sleep(20)
client.disconnect()
    
