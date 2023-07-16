from homeassistant import config_entries
import voluptuous as vol

DATA_SCHEMA = vol.Schema({("ip"): str})



class ConfigFlow(config_entries.ConfigFlow, domain='stas_kitchen_lights'):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        errors = {}

        # If there is no user input or there were errors, show the form again, including any errors that were found with the input.
        return self.async_show_form(
            step_id="ip", data_schema=DATA_SCHEMA, errors=errors
        )