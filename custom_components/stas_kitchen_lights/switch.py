import requests
from homeassistant.components.switch import SwitchEntity


class MyKitchenTopSwitch(SwitchEntity):
    _attr_has_entity_name = True
    _attr_icon = "mdi:light-flood-up"

    def __init__(self):
        self._is_on = False


    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        data = {
            'relay': 1,
            'status': 1
        }
        requests.post("http://192.168.1.100/relay/",data)
        self._is_on = True

    def turn_off(self, **kwargs):
        data = {
            'relay': 1,
            'status': 0
        }
        requests.post("http://192.168.1.100/relay/",data)
        self._is_on = False

    @property
    def name(self):
        """Name of the entity."""
        return "Верхний свет"