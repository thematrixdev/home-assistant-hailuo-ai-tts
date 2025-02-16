"""Hailuo AI TTS Engine."""
import logging
import json
import requests

_LOGGER = logging.getLogger(__name__)

class HailuoAITTSEngine:
    """Hailuo AI TTS engine."""

    def __init__(
        self,
        group_id: str,
        api_key: str,
        model: str,
        voice: str,
        speed: float,
        vol: float,
        pitch: int,
        language: str,
        emotion: str,
        english_normalization: bool,
        model_name: str,
        voice_name: str,
        emotion_name: str,
        language_name: str,
    ):
        """Initialize Hailuo AI TTS engine."""
        self.group_id = group_id
        self._api_key = api_key
        self._model = model
        self._voice = voice
        self._speed = speed
        self._vol = vol
        self._pitch = pitch
        self._language = language
        self._emotion = emotion
        self._english_normalization = english_normalization
        self._model_name = model_name
        self._voice_name = voice_name
        self._emotion_name = emotion_name
        self._language_name = language_name

    def get_tts(self, text: str) -> requests.Response:
        """Get TTS response from API."""
        try:
            if len(text) > 4096:
                raise ValueError("Text length exceeds maximum of 4096 characters")

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._api_key}"
            }

            data = {
                "model": self._model,
                "text": text,
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

            _LOGGER.debug("TTS request header: %s", headers)
            _LOGGER.debug("TTS request data: %s", data)

            response = requests.post(
                f"https://api.minimaxi.chat/v1/t2a_v2?GroupId={self.group_id}",
                headers=headers,
                json=data,
                timeout=30,
            )
            response.raise_for_status()
            return response

        except requests.exceptions.RequestException as err:
            _LOGGER.error("Failed to get TTS: %s", str(err))
            raise

    @staticmethod
    def get_supported_langs() -> list:
        """Return list of supported languages."""
        from .const import LANGUAGES
        return list(LANGUAGES.keys())
