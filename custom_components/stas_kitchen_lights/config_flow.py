from homeassistant import config_entries

class ExampleConfigFlow(config_entries.ConfigFlow, domain='stas_kitchen_lights'):

    VERSION = 1