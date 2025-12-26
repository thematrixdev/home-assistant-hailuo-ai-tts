"""Config flow for Hailuo AI TTS integration."""
from __future__ import annotations

import homeassistant.helpers.config_validation as cv
import json
import logging
import voluptuous as vol
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.core import callback
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
)
from pathlib import Path
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
    CONF_EMOTION,
    CONF_ENGLISH_NORMALIZATION,
    CONF_LANGUAGE,
    CONF_VOICE_NAME,
    CONF_CUSTOM_VOICE_ID,
    CONF_CUSTOM_VOICE_NAME,
    MODELS,
    EMOTIONS,
    TTS_VOICES,
    LANGUAGE_MAPPINGS,
    DEFAULT_LANGUAGE,
    DEFAULT_SPEED,
    DEFAULT_VOL,
    DEFAULT_PITCH,
    DEFAULT_ENGLISH_NORMALIZATION,
    DEFAULT_SERVER,
    DEFAULT_MODEL,
)

_LOGGER = logging.getLogger(__name__)

def get_schema_step1(languages: dict, language: str, defaults: dict | None = None) -> vol.Schema:
    """Get schema for step 1 (all options except voice)."""
    if defaults is None:
        defaults = {}

    schema = {
        vol.Required(CONF_SERVER, default=defaults.get(CONF_SERVER, DEFAULT_SERVER)): SelectSelector(
            SelectSelectorConfig(
                options=[
                    SelectOptionDict(value="international", label="International"),
                    SelectOptionDict(value="china", label="China"),
                ]
            )
        ),
        vol.Required(CONF_API_KEY, default=defaults.get(CONF_API_KEY)): cv.string,
        vol.Required(CONF_LANGUAGE, default=language): SelectSelector(
            SelectSelectorConfig(
                options=[
                    SelectOptionDict(
                        value=iso_code,
                        label=languages.get(iso_code, display_name),
                    )
                    for iso_code, (_, display_name) in LANGUAGE_MAPPINGS.items()
                ]
            )
        ),
        vol.Required(CONF_MODEL, default=defaults.get(CONF_MODEL, DEFAULT_MODEL)): SelectSelector(
            SelectSelectorConfig(
                options=[
                    SelectOptionDict(value=model_id, label=model_name)
                    for model_id, model_name in MODELS.items()
                ]
            )
        ),
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
        vol.Optional(CONF_EMOTION, default=defaults.get(CONF_EMOTION, "")): SelectSelector(
            SelectSelectorConfig(
                options=[
                    SelectOptionDict(value="", label="None"),
                    *[SelectOptionDict(value=emotion_id, label=emotion_name)
                      for emotion_id, emotion_name in EMOTIONS.items()]
                ]
            )
        ),
        vol.Required(
            CONF_ENGLISH_NORMALIZATION,
            default=defaults.get(CONF_ENGLISH_NORMALIZATION, DEFAULT_ENGLISH_NORMALIZATION)
        ): cv.boolean,
    }

    return vol.Schema(schema)

def get_schema_step2(language: str, defaults: dict | None = None) -> vol.Schema:
    """Get schema for step 2 (voice selection)."""
    if defaults is None:
        defaults = {}

    schema = {
        vol.Optional(CONF_VOICE, default=defaults.get(CONF_VOICE, "")): SelectSelector(
            SelectSelectorConfig(
                options=[
                    *[SelectOptionDict(value=voice_id, label=voice_name) for voice_id, voice_name in TTS_VOICES[language].items()],
                    SelectOptionDict(value="custom", label="Custom Voice")
                ]
            )
        ),
        vol.Optional(CONF_CUSTOM_VOICE_ID, default=defaults.get(CONF_CUSTOM_VOICE_ID, "")): cv.string,
        vol.Optional(CONF_CUSTOM_VOICE_NAME, default=defaults.get(CONF_CUSTOM_VOICE_NAME, "")): cv.string,
    }

    return vol.Schema(schema)


class HailuoAITTSConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hailuo AI TTS."""

    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self._strings = None
        self._entry = None
        self._user_input = {}

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
        """Handle the initial step."""
        await self._load_strings()
        languages = self._strings.get("languages", {})
        current = self._entry.data if self._entry else {}

        if user_input is not None:
            self._user_input.update(user_input)
            return await self.async_step_voice()

        return self.async_show_form(
            step_id="user",
            data_schema=get_schema_step1(languages, DEFAULT_LANGUAGE, current),
        )

    async def async_step_voice(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the voice selection step."""

        if user_input is not None:
            if not user_input.get(CONF_VOICE) and not user_input.get(CONF_CUSTOM_VOICE_ID):
                return self.async_show_form(
                    step_id="voice",
                    data_schema=get_schema_step2(self._user_input[CONF_LANGUAGE], user_input),
                    errors={"base": "voice_required"},
                    description_placeholders={
                        "language": self._strings.get("languages", {}).get(
                            self._user_input[CONF_LANGUAGE],
                            self._user_input[CONF_LANGUAGE]
                        )
                    }
                )

            if user_input.get(CONF_VOICE):
                if user_input[CONF_VOICE] != "custom":
                    user_input[CONF_VOICE_NAME] = TTS_VOICES[self._user_input[CONF_LANGUAGE]][user_input[CONF_VOICE]]
                else:
                    user_input[CONF_VOICE_NAME] = "Custom"

            if user_input.get(CONF_CUSTOM_VOICE_ID):
                user_input[CONF_CUSTOM_VOICE_NAME] = user_input.get(CONF_CUSTOM_VOICE_NAME) or "Custom Voice"

            self._user_input.update(user_input)
            return self.async_create_entry(
                title="Hailuo AI TTS",
                data=self._user_input,
            )

        current = self._entry.data if self._entry else {}
        return self.async_show_form(
            step_id="voice",
            data_schema=get_schema_step2(self._user_input[CONF_LANGUAGE], current),
            description_placeholders={
                "language": self._strings.get("languages", {}).get(
                    self._user_input[CONF_LANGUAGE],
                    self._user_input[CONF_LANGUAGE]
                )
            }
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

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        super().__init__()
        self._strings = None
        self._user_input = {}

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
        """Handle the initial step."""
        await self._load_strings()
        languages = self._strings.get("languages", {})
        data = self.config_entry.data
        options = self.config_entry.options
        defaults = {**data, **options}

        if user_input is not None:
            self._user_input.update(user_input)
            return await self.async_step_voice()

        return self.async_show_form(
            step_id="init",
            data_schema=get_schema_step1(languages, defaults.get(CONF_LANGUAGE, DEFAULT_LANGUAGE), defaults),
        )

    async def async_step_voice(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the voice selection step."""

        if user_input is not None:
            if not user_input.get(CONF_VOICE) and not user_input.get(CONF_CUSTOM_VOICE_ID):
                return self.async_show_form(
                    step_id="voice",
                    data_schema=get_schema_step2(self._user_input[CONF_LANGUAGE], user_input),
                    errors={"base": "voice_required"},
                    description_placeholders={
                        "language": self._strings.get("languages", {}).get(
                            self._user_input[CONF_LANGUAGE],
                            self._user_input[CONF_LANGUAGE]
                        )
                    }
                )
            
            if user_input.get(CONF_VOICE):
                if user_input[CONF_VOICE] != "custom":
                    user_input[CONF_VOICE_NAME] = TTS_VOICES[self._user_input[CONF_LANGUAGE]][user_input[CONF_VOICE]]
                else:
                    user_input[CONF_VOICE_NAME] = "Custom"

            if user_input.get(CONF_CUSTOM_VOICE_ID):
                user_input[CONF_CUSTOM_VOICE_NAME] = user_input.get(CONF_CUSTOM_VOICE_NAME) or "Custom Voice"

            self._user_input.update(user_input)

            return self.async_create_entry(
                title="Hailuo AI TTS",
                data=self._user_input,
            )

        data = self.config_entry.data
        options = self.config_entry.options
        defaults = {**data, **options}
        
        voice_defaults = defaults if defaults.get(CONF_LANGUAGE) == self._user_input[CONF_LANGUAGE] else None
        return self.async_show_form(
            step_id="voice",
            data_schema=get_schema_step2(self._user_input[CONF_LANGUAGE], voice_defaults),
            description_placeholders={
                "language": self._strings.get("languages", {}).get(
                    self._user_input[CONF_LANGUAGE],
                    self._user_input[CONF_LANGUAGE]
                )
            }
        )
