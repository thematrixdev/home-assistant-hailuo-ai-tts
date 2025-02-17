"""Config flow for Hailuo AI TTS integration."""
from __future__ import annotations

import logging
import json
from typing import Any, Final
from pathlib import Path
import voluptuous as vol
from homeassistant.core import callback
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
import homeassistant.helpers.config_validation as cv

from .const import (
    DOMAIN,
    CONF_GROUP_ID,
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
    MODELS,
    EMOTIONS,
    TTS_VOICES,
    LANGUAGE_CODES,
    DEFAULT_LANGUAGE,
    DEFAULT_SPEED,
    DEFAULT_VOL,
    DEFAULT_PITCH,
    DEFAULT_ENGLISH_NORMALIZATION,
)

_LOGGER = logging.getLogger(__name__)

def get_schema(languages: dict, language: str, defaults: dict | None = None) -> vol.Schema:
    """Get schema with the specified language and defaults."""
    if defaults is None:
        defaults = {}

    schema = {
        vol.Required(CONF_GROUP_ID, default=defaults.get(CONF_GROUP_ID)): cv.string,
        vol.Required(CONF_API_KEY, default=defaults.get(CONF_API_KEY)): cv.string,
        vol.Required(CONF_LANGUAGE, default=language): vol.In({
            code: languages.get(code, code)
            for code in LANGUAGE_CODES.values()
        }),
        vol.Required(CONF_VOICE, default=defaults.get(CONF_VOICE)): vol.In(TTS_VOICES[language]),
        vol.Required(CONF_MODEL, default=defaults.get(CONF_MODEL)): vol.In(MODELS),
        vol.Required(
            CONF_SPEED,
            default=defaults.get(CONF_SPEED, DEFAULT_SPEED)
        ): vol.All(
            vol.Coerce(float),
            vol.Range(min=0.5, max=2.0)
        ),
        vol.Required(
            CONF_VOL,
            default=defaults.get(CONF_VOL, DEFAULT_VOL)
        ): vol.All(
            vol.Coerce(float),
            vol.Range(min=0.1, max=10.0)
        ),
        vol.Required(
            CONF_PITCH,
            default=defaults.get(CONF_PITCH, DEFAULT_PITCH)
        ): vol.All(
            vol.Coerce(int),
            vol.Range(min=-12, max=12)
        ),
        vol.Optional(CONF_EMOTION, default=defaults.get(CONF_EMOTION, "")): vol.In({**EMOTIONS, "": ""}),
        vol.Required(
            CONF_ENGLISH_NORMALIZATION,
            default=defaults.get(CONF_ENGLISH_NORMALIZATION, DEFAULT_ENGLISH_NORMALIZATION)
        ): cv.boolean,
    }

    return vol.Schema(schema)


class HailuoAITTSConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hailuo AI TTS."""

    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self._strings = None
        self._entry = None

    async def _load_strings(self) -> None:
        """Load strings.json file."""
        if self._strings is not None:
            return

        strings_path = Path(__file__).parent / "strings.json"
        try:
            content = await self.hass.async_add_executor_job(
                lambda: strings_path.read_text(encoding="utf-8")
            )
            self._strings = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self._strings = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        await self._load_strings()
        languages = self._strings.get("languages", {})

        if user_input is not None:
            # Store display names
            user_input[CONF_MODEL_NAME] = MODELS[user_input[CONF_MODEL]]
            user_input[CONF_VOICE_NAME] = TTS_VOICES[user_input[CONF_LANGUAGE]][user_input[CONF_VOICE]]
            user_input[CONF_LANGUAGE_NAME] = languages.get(user_input[CONF_LANGUAGE], user_input[CONF_LANGUAGE])
            if user_input.get(CONF_EMOTION):
                user_input[CONF_EMOTION_NAME] = EMOTIONS[user_input[CONF_EMOTION]]

            return self.async_create_entry(
                title="Hailuo AI TTS",
                data=user_input,
            )

        current = self._entry.data if self._entry else {}
        language = current.get(CONF_LANGUAGE, DEFAULT_LANGUAGE)

        return self.async_show_form(
            step_id="user",
            data_schema=get_schema(languages, language, current),
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> HailuoAITTSOptionsFlow:
        """Get the options flow for this handler."""
        return HailuoAITTSOptionsFlow(config_entry)

class HailuoAITTSOptionsFlow(OptionsFlow):
    """Handle options flow for Hailuo AI TTS."""

    def __init__(self, config_entry: ConfigEntry):
        """Initialize options flow."""
        self.config_entry = config_entry
        self._strings = None

    async def _load_strings(self) -> None:
        """Load strings.json file."""
        if self._strings is not None:
            return

        strings_path = Path(__file__).parent / "strings.json"
        try:
            content = await self.hass.async_add_executor_job(
                lambda: strings_path.read_text(encoding="utf-8")
            )
            self._strings = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self._strings = {}

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        await self._load_strings()
        languages = self._strings.get("languages", {})

        if user_input is not None:
            user_input[CONF_MODEL_NAME] = MODELS[user_input[CONF_MODEL]]
            user_input[CONF_VOICE_NAME] = TTS_VOICES[user_input[CONF_LANGUAGE]][user_input[CONF_VOICE]]
            user_input[CONF_LANGUAGE_NAME] = languages.get(user_input[CONF_LANGUAGE], user_input[CONF_LANGUAGE])
            if user_input.get(CONF_EMOTION):
                user_input[CONF_EMOTION_NAME] = EMOTIONS[user_input[CONF_EMOTION]]

            updated_data = {**self.config_entry.data, **user_input}
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                data=updated_data,
            )
            return self.async_create_entry(data=updated_data)

        current = self.config_entry.data
        language = current.get(CONF_LANGUAGE, DEFAULT_LANGUAGE)

        return self.async_show_form(
            step_id="init",
            data_schema=get_schema(languages, language, current),
        )
