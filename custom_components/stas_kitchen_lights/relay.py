from homeassistant.core import HomeAssistant

class Relay:
    def __init__(self, hass: HomeAssistant) -> None:
        self.devices = getDevices()
        self.hass:HomeAssistant = hass

def getDevices():
    devices = []
    devices.append({'_device_name': 'Весь свет','model_name': 'lamp', '_id': 0})
    devices.append({'_device_name': 'Верхний свет', 'model_name': 'lamp', '_id': 1})
    devices.append({'_device_name': 'Нижний левый свет', 'model_name': 'lamp', '_id': 2})
    devices.append({'_device_name': 'Нижний правый свет', 'model_name': 'lamp', '_id': 3})
    return devices