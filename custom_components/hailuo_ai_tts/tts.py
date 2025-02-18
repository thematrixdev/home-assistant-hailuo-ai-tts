"""
Setting up TTS entity.
"""
import logging
import binascii
import requests
from typing import Any
from homeassistant.components.tts import DOMAIN as TTS_DOMAIN
from homeassistant.components.tts import (
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import generate_entity_id

from .const import (
    CONF_API_KEY,
    CONF_SERVER,
    CONF_MODEL,
    CONF_SPEED,
    CONF_VOL,
    CONF_PITCH,
    CONF_VOICE,
    CONF_EMOTION,
    CONF_ENGLISH_NORMALIZATION,
    CONF_LANGUAGE,
    CONF_MODEL_NAME,
    CONF_VOICE_NAME,
    CONF_EMOTION_NAME,
    CONF_LANGUAGE_NAME,
    CONF_GROUP_ID,
    LANGUAGE_MAPPINGS,
    get_language_api_value,
    DEFAULT_LANGUAGE,
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

    def __init__(self, hass, config):
        """Initialize TTS entity."""
        self.hass = hass
        self._config = config
        self._attr_unique_id = config.unique_id
        
        # 初始化配置
        self._update_from_config()

        # 監聽配置變更
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
        self._speed = data[CONF_SPEED]
        self._vol = data[CONF_VOL]
        self._pitch = data[CONF_PITCH]
        self._emotion = data.get(CONF_EMOTION)
        self._english_normalization = data[CONF_ENGLISH_NORMALIZATION]
        self._language = data[CONF_LANGUAGE]

    async def _handle_config_update(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Handle config update."""
        self._config = entry
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
        return [Voice(voice_id, display_name) for voice_id, display_name in voices.items()]

    @property
    def name(self):
        """Return name of entity."""
        return f"Hailuo AI TTS"

    def get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._api_key}"
        }
        data = {
            "text": message,
            "model": self._model,
            "voice_setting": {
                "voice_id": self._voice,
                "speed": self._speed,
                "vol": self._vol,
                "pitch": self._pitch,
            },
            "language_boost": get_language_api_value(language or self._language),
        }
        if self._emotion:
            data["emotion"] = self._emotion
        if self._english_normalization:
            data["english_normalization"] = self._english_normalization

        endpoint = "https://api.minimaxi.chat/v1/t2a_v2" if self._server == "international" else "https://api.minimax.chat/v1/t2a_v2"
        _LOGGER.debug("Request endpoint: %s", endpoint)
        _LOGGER.debug("Request header: %s", headers)
        _LOGGER.debug("Request data: %s", data)

        response = requests.post(
            endpoint,
            headers=headers,
            json=data,
            timeout=30,
        )
        response.raise_for_status()
        response_json = response.json()
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
