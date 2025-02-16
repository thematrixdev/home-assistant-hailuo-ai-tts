"""Config flow for Hailuo AI TTS integration."""
from __future__ import annotations

import json
from pathlib import Path
import voluptuous as vol
import aiofiles
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
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


class HailuoAITTSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hailuo AI TTS."""

    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self._strings = None

    async def _load_strings(self) -> None:
        """Load strings.json file."""
        if self._strings is not None:
            return

        strings_path = Path(__file__).parent / "strings.json"
        try:
            async with aiofiles.open(strings_path, mode='r', encoding="utf-8") as f:
                content = await f.read()
                self._strings = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            self._strings = {}

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        await self._load_strings()
        languages = self._strings.get("languages", {})
        voices = self._strings.get("voices", {})

        if user_input is not None:
            # Store display names
            user_input[CONF_MODEL_NAME] = MODELS[user_input[CONF_MODEL]]
            user_input[CONF_VOICE_NAME] = voices.get(user_input[CONF_VOICE], user_input[CONF_VOICE])
            user_input[CONF_LANGUAGE_NAME] = languages.get(user_input[CONF_LANGUAGE], user_input[CONF_LANGUAGE])
            if user_input.get(CONF_EMOTION):
                user_input[CONF_EMOTION_NAME] = EMOTIONS[user_input[CONF_EMOTION]]

            return self.async_create_entry(
                title=f"{user_input[CONF_LANGUAGE_NAME]} - {user_input[CONF_VOICE_NAME]} ({user_input[CONF_MODEL_NAME]})",
                data=user_input,
            )

        data_schema = vol.Schema({
            vol.Required(CONF_GROUP_ID): cv.string,
            vol.Required(CONF_API_KEY): cv.string,
            vol.Required(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): vol.In({
                code: languages.get(code, code)
                for code in LANGUAGE_CODES.values()
            }),
            vol.Required(CONF_VOICE): vol.In(TTS_VOICES[DEFAULT_LANGUAGE]),
            vol.Required(CONF_MODEL): vol.In(MODELS),
            vol.Required(
                CONF_SPEED,
                default=DEFAULT_SPEED
            ): vol.All(
                vol.Coerce(float),
                vol.Range(min=0.5, max=2.0)
            ),
            vol.Required(
                CONF_VOL,
                default=DEFAULT_VOL
            ): vol.All(
                vol.Coerce(float),
                vol.Range(min=0.1, max=10.0)
            ),
            vol.Required(
                CONF_PITCH,
                default=DEFAULT_PITCH
            ): vol.All(
                vol.Coerce(int),
                vol.Range(min=-12, max=12)
            ),
            vol.Optional(CONF_EMOTION): vol.In(EMOTIONS),
            vol.Required(CONF_ENGLISH_NORMALIZATION, default=DEFAULT_ENGLISH_NORMALIZATION): cv.boolean,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
        )
