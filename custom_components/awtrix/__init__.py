"""Awtrix."""

from __future__ import annotations

import copy

import json
import logging
from typing import TYPE_CHECKING

from homeassistant.components import mqtt
from homeassistant.const import Platform
from homeassistant.helpers.entity_registry import async_entries_for_device, async_get
from homeassistant.util.read_only_dict import ReadOnlyDict

from custom_components.awtrix.const import DOMAIN

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant, ServiceCall

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.BINARY_SENSOR]


async def async_setup(hass: HomeAssistant, config: dict):

    async def update_settings(call: ServiceCall):
        device = call.data.get("device")
        payload = json.dumps(call.data)
        prefix = await _get_prefix(hass, device)

        await mqtt.async_publish(hass, f"{prefix}/settings", payload)


    async def notification(call: ServiceCall):
        device = call.data.get("device")
        data = _color_points(call.data)
        payload = json.dumps(data)
        prefix = await _get_prefix(hass, device)

        await mqtt.async_publish(hass, f"{prefix}/notify", payload)

    async def custom_app(call: ServiceCall):
        device = call.data.get("device")
        app = call.data.get("app")
        data = _color_points(call.data)
        payload = json.dumps(data)
        prefix = await _get_prefix(hass, device)

        await mqtt.async_publish(hass, f"{prefix}/custom/{app}", payload)


    hass.services.async_register(DOMAIN, "settings", update_settings)
    hass.services.async_register(DOMAIN, "notification", notification)
    hass.services.async_register(DOMAIN, "custom_app", custom_app)

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Initialise entry configuration."""
    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Remove entry after unload component."""
    return True


async def _get_prefix(hass, device_id: str) -> str | None:
    entity_registry = async_get(hass)
    entities = async_entries_for_device(entity_registry, device_id, True)

    for e in entities:
        if e.original_name == 'Device topic':
            return hass.states.get(e.entity_id).state

    return None

def _color_points(payload: ReadOnlyDict) -> dict:
    color_points = payload.get('color_points')
    if color_points is None:
        return payload

    data = dict(payload)
    offset = 8 if data.get('icon') else 0
    draw = json.loads(data.get('draw', '[]'))
    for index, color in enumerate(color_points):
        draw.append({'dp': [index+offset, 7, color]})

    data['draw'] = json.dumps(draw)
    return data
