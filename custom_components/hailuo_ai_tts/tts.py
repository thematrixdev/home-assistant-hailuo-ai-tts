"""
Setting up TTS entity.
"""
import aiohttp
import asyncio
import binascii
import logging
from homeassistant.components.tts import (
    ATTR_VOICE,
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from typing import Any

from .const import (
    DOMAIN,
    CONF_API_KEY,
    CONF_SERVER,
    CONF_MODEL,
    CONF_SPEED,
    CONF_VOL,
    CONF_PITCH,
    CONF_VOICE,
    CONF_VOICE_NAME,
    CONF_CUSTOM_VOICE_ID,
    CONF_CUSTOM_VOICE_NAME,
    CONF_EMOTION,
    CONF_ENGLISH_NORMALIZATION,
    CONF_LANGUAGE,
    LANGUAGE_MAPPINGS,
    MODELS,
    get_language_api_value,
    get_language_display_name,
    TTS_VOICES,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Hailuo AI TTS entry."""
    async_add_entities([
        HailuoAITTSEntity(
            hass,
            config_entry,
        )
    ])

class HailuoAITTSEntity(TextToSpeechEntity):
    """The Hailuo AI TTS entity."""

    _attr_supported_options = [ATTR_VOICE]

    def __init__(self, hass, config):
        """Initialize TTS entity."""
        self.hass = hass
        self._config = config
        self._attr_unique_id = config.entry_id
        self.entity_id = f"tts.{DOMAIN}_{config.entry_id}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self._attr_unique_id)},
            entry_type=DeviceEntryType.SERVICE,
        )
        self._update_from_config()
        config.add_update_listener(self._handle_config_update)

    def _update_from_config(self) -> None:
        """Update local variables from config entry."""
        data = {
            **self._config.data,
            **self._config.options
        }
        self._api_key = data[CONF_API_KEY]
        self._server = data[CONF_SERVER]
        self._model = data[CONF_MODEL]
        self._voice = data[CONF_VOICE]
        self._custom_voice_id = data[CONF_CUSTOM_VOICE_ID]
        self._custom_voice_name = data[CONF_CUSTOM_VOICE_NAME]
        self._speed = data[CONF_SPEED]
        self._vol = data[CONF_VOL]
        self._pitch = data[CONF_PITCH]
        self._emotion = data.get(CONF_EMOTION)
        self._english_normalization = data[CONF_ENGLISH_NORMALIZATION]
        self._language = data[CONF_LANGUAGE]

        language_name = get_language_display_name(self._language)
        voice_name = data.get(CONF_VOICE_NAME, self._voice)
        if self._custom_voice_id:
            voice_name = data.get(CONF_CUSTOM_VOICE_NAME, self._custom_voice_id)
        model_name = MODELS.get(self._model, self._model)
        self._attr_name = f"Hailuo AI TTS ({language_name}, {voice_name}, {model_name})"

    async def _handle_config_update(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Handle config update."""
        self._update_from_config()
        self.async_write_ha_state()

    @property
    def default_language(self):
        """Return the default language."""
        return self._language

    @property
    def supported_languages(self):
        """Return the list of supported languages."""
        return list(LANGUAGE_MAPPINGS.keys())

    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice]:
        """Return a list of supported voices for a language."""
        _LOGGER.debug("Supported voices for language: %s", language)
        voices = TTS_VOICES.get(language, {})
        voice_list = [Voice(voice_id, display_name) for voice_id, display_name in voices.items()]
        if hasattr(self, '_custom_voice_id') and self._custom_voice_id:
            voice_list.append(Voice(
                voice_id=self._custom_voice_id,
                name=self._custom_voice_name
            ))

        _LOGGER.debug("Voice list: %s", voice_list)
        
        return voice_list

    @property
    def name(self):
        """Return name of entity."""
        return self._attr_name

    async def async_get_tts_audio(
        self,
        message: str,
        language: str,
        options: dict[str, Any],
    ) -> TtsAudioType:
        """Load TTS audio file from the engine."""
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._api_key}"
            }

            if self._voice == "custom" and self._custom_voice_id != "":
                voice_id = self._custom_voice_id
            elif self._voice != "custom":
                voice_id = self._voice
            else:
                voice_id = list(TTS_VOICES[language].keys())[0]
            
            data = {
                "text": message,
                "model": self._model,
                "voice_setting": {
                    "voice_id": voice_id,
                },
                "language_boost": get_language_api_value(language or self._language),
            }
            
            if self._speed != 1:
                data["voice_setting"]["speed"] = self._speed

            if self._vol != 1:
                data["voice_setting"]["vol"] = self._vol

            if self._pitch != 0:
                data["voice_setting"]["pitch"] = self._pitch

            if self._emotion:
                data["voice_setting"]["emotion"] = self._emotion

            if self._english_normalization:
                data["voice_setting"]["english_normalization"] = self._english_normalization

            endpoint = "https://api.minimaxi.chat/v1/t2a_v2" if self._server == "international" else "https://api.minimaxi.chat/v1/t2a_v2"
            _LOGGER.debug("Request endpoint: %s", endpoint)
            _LOGGER.debug("Request header: %s", headers)
            _LOGGER.debug("Request data: %s", data)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    endpoint,
                    headers=headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    response.raise_for_status()
                    response_json = await response.json()
                    
                    _LOGGER.debug("API Response: %s", {
                        **response_json,
                        "data": {
                            **response_json.get("data", {}),
                            "audio": "[REDACTED]" if "audio" in response_json.get("data", {}) else None
                        }
                    })

                    if response_json["base_resp"]["status_code"] != 0:
                        raise RuntimeError(response_json['base_resp']['status_msg'])

                    audio_format = response_json["extra_info"]["audio_format"]
                    audio_data = binascii.unhexlify(response_json["data"]["audio"])
                    return (audio_format, audio_data)

        except asyncio.CancelledError:
            _LOGGER.debug("TTS task was cancelled")
            raise
        except aiohttp.ClientError as exc:
            _LOGGER.error("Error communicating with API: %s", exc)
            raise HomeAssistantError(f"API request failed: {exc}") from exc
        except Exception as exc:
            _LOGGER.error("Unexpected error during TTS generation: %s", exc)
            raise HomeAssistantError(str(exc)) from exc
