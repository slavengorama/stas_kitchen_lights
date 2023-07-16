from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from . import relay

PLATFORMS: list[str] = [ "switch"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    #Создать объект с подключением к сервису
    relay1 = relay.Relay(hass)
    hass.data.setdefault('stas_kitchen_lights', {})[entry.entry_id] = relay1

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data['stas_kitchen_lights'].pop(entry.entry_id)

    return unload_ok
