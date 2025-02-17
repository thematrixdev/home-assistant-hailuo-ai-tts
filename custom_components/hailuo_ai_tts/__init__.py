"""The Hailuo AI TTS integration."""
from __future__ import annotations

import json
from pathlib import Path
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

PLATFORMS = [Platform.TTS]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Hailuo AI TTS from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Load translations from strings.json
    strings_path = Path(__file__).parent / "strings.json"
    try:
        content = await hass.async_add_executor_job(
            lambda: strings_path.read_text(encoding="utf-8")
        )
        strings = json.loads(content)
        hass.data[DOMAIN]["languages"] = strings.get("languages", {})
        hass.data[DOMAIN]["voices"] = strings.get("voices", {})
    except (FileNotFoundError, json.JSONDecodeError):
        hass.data[DOMAIN]["languages"] = {}
        hass.data[DOMAIN]["voices"] = {}

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
