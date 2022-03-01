import requests


def toggle(bearer):
    headers = {
        "Authorization": "Bearer %s" % bearer,
    }
    response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)

def setColor(bearer, hue, saturation, brightness):
    headers = {
        "Authorization": "Bearer %s" % bearer,
    }
    payload = {
        "power":        "on",
        "color":        "hue:{} saturation:{} brightness:{}".format(hue, saturation/100, brightness/100),
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    