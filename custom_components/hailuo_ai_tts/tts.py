"""
Setting up TTS entity.
"""
import logging
import binascii
import asyncio
from homeassistant.components.tts import TextToSpeechEntity, DOMAIN as TTS_DOMAIN
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
    UNIQUE_ID,
    DEFAULT_LANGUAGE,
)
from homeassistant.exceptions import MaxLengthExceeded
from .engine import HailuoAITTSEngine
from homeassistant.components import persistent_notification

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Hailuo AI TTS entry."""
    engine = HailuoAITTSEngine(
        group_id=config_entry.data[CONF_GROUP_ID],
        api_key=config_entry.data[CONF_API_KEY],
        model=config_entry.data[CONF_MODEL],
        speed=config_entry.data[CONF_SPEED],
        vol=config_entry.data[CONF_VOL],
        pitch=config_entry.data[CONF_PITCH],
        voice=config_entry.data[CONF_VOICE],
        emotion=config_entry.data.get(CONF_EMOTION, ""),
        english_normalization=config_entry.data[CONF_ENGLISH_NORMALIZATION],
        language=config_entry.data[CONF_LANGUAGE],
        model_name=config_entry.data[CONF_MODEL_NAME],
        voice_name=config_entry.data[CONF_VOICE_NAME],
        emotion_name=config_entry.data[CONF_EMOTION_NAME],
        language_name=config_entry.data[CONF_LANGUAGE_NAME],
    )
    async_add_entities([HailuoAITTSEntity(hass, config_entry, engine)])


class HailuoAITTSEntity(TextToSpeechEntity):
    """The Hailuo AI TTS entity."""

    def __init__(self, hass, config, engine):
        """Initialize TTS entity."""
        self.hass = hass
        self._config = config
        self._engine = engine

        self._attr_unique_id = config.data.get(UNIQUE_ID)
        # Generate entity_id in format tts.hailuo_ai_voice_name
        self.entity_id = generate_entity_id(
            f"{TTS_DOMAIN}.{{}}", 
            f"hailuoaitts_{self._config.data[CONF_LANGUAGE_NAME].lower()}_{self._config.data[CONF_VOICE_NAME].lower()}_{self._config.data[CONF_MODEL_NAME].lower()}",
            hass=hass
        )

    @property
    def default_language(self):
        """Return the default language."""
        return DEFAULT_LANGUAGE

    @property
    def supported_languages(self):
        """Return the list of supported languages."""
        return self._engine.get_supported_langs()

    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self._attr_unique_id)},
            "name": self.name,
        }

    @property
    def name(self):
        """Return name of entity."""
        return f"Hailuo AI TTS ({self._config.data[CONF_LANGUAGE_NAME]}, {self._config.data[CONF_VOICE_NAME]}, {self._config.data[CONF_MODEL_NAME]})"

    async def async_get_tts_audio(self, message, language, options=None):
        """Convert a given text to speech and return it as bytes."""
        try:
            response = await self.hass.async_add_executor_job(
                self._engine.get_tts, message
            )

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

            audio_data = binascii.unhexlify(response_json["data"]["audio"])
            await asyncio.sleep(0.1)

            audio_format = response_json["extra_info"]["audio_format"]
            return (audio_format, audio_data)

        except Exception as err:
            persistent_notification.create(
                self.hass,
                message=str(err),
                title="Hailuo AI TTS Error",
                notification_id=f"{DOMAIN}_error"
            )
            raise
