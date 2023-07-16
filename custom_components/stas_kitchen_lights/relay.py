from homeassistant.core import HomeAssistant

class Relay:
    def __init__(self, hass: HomeAssistant) -> None:
        self.devices = getDevices()
        self.hass:HomeAssistant = hass

def getDevices():
    devices = []
    devices.append({'name': 'Весь свет', 'id': 0})
    devices.append({'name': 'Верхний свет', 'id': 1})
    devices.append({'name': 'Нижний левый свет', 'id': 2})
    devices.append({'name': 'Нижний правый свет', 'id': 3})
    return devices