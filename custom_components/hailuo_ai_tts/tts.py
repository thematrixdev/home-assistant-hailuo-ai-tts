"""
Setting up TTS entity.
"""
import logging
import binascii
import asyncio
from homeassistant.helpers.issue_registry import IssueSeverity, async_create_issue
from typing import Any
from homeassistant.components.tts import DOMAIN as TTS_DOMAIN
from homeassistant.components.tts import (
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import generate_entity_id
from .const import (
    CONF_API_KEY,
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
    DOMAIN,
    LANGUAGES,
    UNIQUE_ID,
    DEFAULT_LANGUAGE,
    VOICES,
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
        self._attr_unique_id = config.data.get(UNIQUE_ID)

        # Generate entity_id in format tts.hailuo_ai_voice_name
        self.entity_id = generate_entity_id(
            f"{TTS_DOMAIN}.{{}}", 
            f"hailuoaitts_{self._config.data[CONF_LANGUAGE_NAME].lower()}_{self._config.data[CONF_VOICE_NAME].lower()}_{self._config.data[CONF_MODEL_NAME].lower()}",
            hass=hass
        )

        # Store configuration
        self.group_id = config.data[CONF_GROUP_ID]
        self._api_key = config.data[CONF_API_KEY]
        self._model = config.data[CONF_MODEL]
        self._voice = config.data[CONF_VOICE]
        self._speed = config.data[CONF_SPEED]
        self._vol = config.data[CONF_VOL]
        self._pitch = config.data[CONF_PITCH]
        self._language = config.data[CONF_LANGUAGE]
        self._emotion = config.data.get(CONF_EMOTION, "")
        self._english_normalization = config.data[CONF_ENGLISH_NORMALIZATION]
        self._model_name = config.data[CONF_MODEL_NAME]
        self._voice_name = config.data[CONF_VOICE_NAME]
        self._emotion_name = config.data.get(CONF_EMOTION_NAME, "")
        self._language_name = config.data[CONF_LANGUAGE_NAME]

    @property
    def default_language(self):
        """Return the default language."""
        return DEFAULT_LANGUAGE

    @property
    def supported_languages(self):
        """Return the list of supported languages."""
        return list(LANGUAGES.keys())

    def async_get_supported_voices(self, language: str) -> list[Voice]:
        """Return a list of supported voices for a language."""
        return list(VOICES.keys())

    @property
    def name(self):
        """Return name of entity."""
        return f"Hailuo AI TTS ({self._config.data[CONF_LANGUAGE_NAME]}, {self._config.data[CONF_VOICE_NAME]}, {self._config.data[CONF_MODEL_NAME]})"

    async def async_get_tts_audio(
        self, message: str, language: str, options: dict[str, Any]
    ) -> TtsAudioType:
        """Convert a given text to speech and return it as bytes."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._api_key}"
        }

        data = {
            "model": self._model,
            "text": message,
            "voice_setting": {
                "voice_id": self._voice,
                "speed": self._speed,
                "vol": self._vol,
                "pitch": self._pitch,
            },
            "audio_setting": {
                "format": "mp3",
            }
        }

        if self._language:
            data["language_boost"] = self._language

        if self._english_normalization:
            data["english_normalization"] = True

        if self._emotion:
            data["voice_setting"]["emotion"] = self._emotion

        _LOGGER.debug("Request header: %s", headers)
        _LOGGER.debug("Request data: %s", data)

        websession = async_get_clientsession(self.hass)
        try:
            async with asyncio.timeout(30):
                response = await websession.post(
                    f"https://api.minimaxi.chat/v1/t2a_v2?GroupId={self.group_id}",
                    headers=headers,
                    json=data,
                )

                _LOGGER.debug("Response headers: %s", response.headers)

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
        except Exception as err:
            _LOGGER.error(str(err))

            async_create_issue(
                self.hass,
                DOMAIN,
                str(err),
                is_fixable=False,
                is_persistent=True,
                severity=IssueSeverity.WARNING,
            )
            
            return (None, None)

        return (audio_format, audio_data)
