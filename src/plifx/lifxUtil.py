import os
import json
import sys
import requests as req

class lightUtils:
    def __init__(self, bearer):
        self.headers = {
                "Authorization": "Bearer %s" % bearer,
                }

    """
    returns the id's of all lights in a list
    """
    def getIDs(self):
        ids = []
        re = req.get('https://api.lifx.com/v1/lights/all', headers=self.headers)
        for item in re.json():
            ids.append(item.get("id"))
        return ids

#****************************Singular lights************************
    """
    sets the color of the specified light with hue (0 - 360), saturation (0.0 - 1.0) and brightness (0.0 - 1.0)
    """
    def setColor(self, ID,  hue, saturation, brightness):
        if brightness < 0 or brightness > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()
        if saturation < 0 or saturation > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()
        payload = {
            "states": [
                {
                    "selector": "id:{}".format(ID),
                    "color": "hue:{} saturation:{} brightness:{}".format(hue, saturation, brightness)
                }
            ],
            "defaults": {
                "power": "on"
            }
        }
        re = req.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=self.headers)

    def setWhite(self, ID, kelvin, brightness):
        if kelvin < 1500 or kelvin > 9000:
            sys.stderr.write("Error: value of kelvin is outside of accepted range (1500 - 9000)\n")
            quit()
        if brightness < 0 or brightness > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()
        payload = {
            "states": [
                {
                    "selector": "id:{}".format(ID),
                    "color": "kelvin:{} brightness:{}".format(kelvin, brightness)
                }
            ],
            "defaults": {
                "power": "on"
            }
        }
        re = req.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=self.headers)









#*********************************All lights************************
    """
    toggles all lights
    """
    def toggleAll(self):
        re = req.post('https://api.lifx.com/v1/lights/all/toggle', headers=self.headers)

    """
    sets the color of all lights with hue (0 - 360), saturation (0.0 - 1.0) and brightness (0.0 - 1.0)
    """
    def setColorAll(self, hue, saturation, brightness):
        if brightness < 0 or brightness > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()
        if saturation < 0 or saturation > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()
        payload = {
                "power" : "on",
                "color" : "hue:{} saturation:{} brightness:{}".format(hue % 360, saturation, brightness)
                }
        re = req.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=self.headers)




    def setWhiteAll(self, kelvin, brightness):
        if kelvin < 1500 or kelvin > 9000:
            sys.stderr.write("Error: value of kelvin is outside of accepted range (1500 - 9000)\n")
            quit()
        if brightness < 0 or brightness > 1:
            sys.stderr.write("Error: value of brightness is outside of accepted range (0.0 - 1.0)\n")
            quit()

        payload = {
                "power" : "on",
                "color" : "kelvin:{} brightness:{}".format(kelvin, brightness)
                }
        re = req.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=self.headers)


#***************************Effects*********************************
    def setBreathe(self):
        #TODO
        payload = {
                "color": "green",
                "persist": True,
                }
        re = req.put('https://api.lifx.com/v1/lights/all/effects/breathe', data=payload, headers=self.headers)
        self.__printStatus(re)


    def __printStatus(self, re):
        print(re.status_code)
