"""Config flow for Hailuo-AI TTS integration."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv

from .const import (
    DOMAIN,
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
    UNIQUE_ID,
    MODELS,
    VOICES,
    EMOTIONS,
    LANGUAGES,
    DEFAULT_LANGUAGE,
    DEFAULT_SPEED,
    DEFAULT_VOL,
    DEFAULT_PITCH,
    DEFAULT_ENGLISH_NORMALIZATION,
    CONF_GROUP_ID,
)


def generate_unique_id(user_input: dict) -> str:
    """Generate a unique id from user input."""
    return f"{user_input[CONF_API_KEY]}_{user_input[CONF_LANGUAGE]}_{user_input[CONF_VOICE]}_{user_input[CONF_MODEL]}"


async def validate_user_input(user_input: dict):
    """Validate user input fields."""
    if user_input.get(CONF_API_KEY) is None:
        raise ValueError("API Key is required")

    if user_input.get(CONF_MODEL) is None:
        raise ValueError("Model is required")

    if user_input.get(CONF_VOICE) is None:
        raise ValueError("Voice is required")
    
    speed = user_input.get(CONF_SPEED, DEFAULT_SPEED)
    if not 0.5 <= speed <= 2.0:
        raise ValueError("Speed must be between 0.5 and 2.0")
    
    vol = user_input.get(CONF_VOL, DEFAULT_VOL)
    if not 0 <= vol <= 10:
        raise ValueError("Volume must be between 0 and 10")
    
    pitch = user_input.get(CONF_PITCH, DEFAULT_PITCH)
    if not -12 <= pitch <= 12:
        raise ValueError("Pitch must be between -12 and 12")


class HailuoAITTSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hailuo-AI TTS."""

    VERSION = 1

    data_schema = vol.Schema({
        vol.Required(CONF_GROUP_ID): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): vol.In(LANGUAGES),
        vol.Required(CONF_VOICE): vol.In(VOICES),
        vol.Required(CONF_MODEL): vol.In(MODELS),
        vol.Required(CONF_SPEED, default=DEFAULT_SPEED): vol.All(
            vol.Coerce(float),
            vol.Range(min=0.5, max=2.0)
        ),
        vol.Required(CONF_VOL, default=DEFAULT_VOL): vol.All(
            vol.Coerce(float),
            vol.Range(min=0, max=10)
        ),
        vol.Required(CONF_PITCH, default=DEFAULT_PITCH): vol.All(
            vol.Coerce(int),
            vol.Range(min=-12, max=12)
        ),
        vol.Optional(CONF_EMOTION): vol.In(EMOTIONS),
        vol.Required(CONF_ENGLISH_NORMALIZATION, default=DEFAULT_ENGLISH_NORMALIZATION): cv.boolean,
    })

    async def async_step_user(
        self, user_input: dict[str, any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                await validate_user_input(user_input)

                unique_id = generate_unique_id(user_input)
                user_input[UNIQUE_ID] = unique_id
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()

                user_input[CONF_MODEL_NAME] = MODELS[user_input[CONF_MODEL]]
                user_input[CONF_VOICE_NAME] = VOICES[user_input[CONF_VOICE]]
                user_input[CONF_LANGUAGE_NAME] = LANGUAGES[user_input[CONF_LANGUAGE]]
                
                if CONF_EMOTION in user_input and user_input[CONF_EMOTION]:
                    user_input[CONF_EMOTION_NAME] = EMOTIONS[user_input[CONF_EMOTION]]
                else:
                    user_input[CONF_EMOTION_NAME] = EMOTIONS[""]

                return self.async_create_entry(
                    title=f"Hailuo AI TTS ({user_input[CONF_LANGUAGE_NAME]}, {user_input[CONF_VOICE_NAME]}, {user_input[CONF_MODEL_NAME]})",
                    data=user_input,
                )
            except Exception as e:
                errors["base"] = str(e)

        return self.async_show_form(
            step_id="user",
            data_schema=self.data_schema,
            errors=errors,
        )
