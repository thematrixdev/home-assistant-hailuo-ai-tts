"""Constants for the Hailuo AI TTS integration."""

DOMAIN = "hailuo_ai_tts"

CONF_GROUP_ID = "group_id"
CONF_API_KEY = "api_key"
CONF_MODEL = "model"
CONF_SPEED = "speed"
CONF_VOL = "vol"
CONF_PITCH = "pitch"
CONF_VOICE = "voice"
CONF_EMOTION = "emotion"
CONF_ENGLISH_NORMALIZATION = "english_normalization"
CONF_LANGUAGE = "language"

# Display name constants
CONF_MODEL_NAME = "model_name"
CONF_VOICE_NAME = "voice_name"
CONF_EMOTION_NAME = "emotion_name"
CONF_LANGUAGE_NAME = "language_name"

# Default values
DEFAULT_LANGUAGE = "zh-HK"
DEFAULT_SPEED = 1.0
DEFAULT_VOL = 1.0
DEFAULT_PITCH = 0
DEFAULT_ENGLISH_NORMALIZATION = False

# Available models
MODELS = {
    "speech-01-hd": "HD",
    "speech-01-turbo": "Turbo",
}

# Available emotions
EMOTIONS = {
    "happy": "Happy",
    "sad": "Sad",
    "angry": "Angry",
    "fear": "Fear",
    "hate": "Hate",
    "surprise": "Surprise",
    "neutral": "Neutral",
}

# Language mappings
# Format: ISO code -> (API value, Display name)
LANGUAGE_MAPPINGS = {
    "es-ES": ("Spanish", "Spanish"),
    "fr-FR": ("French", "French"),
    "pt-PT": ("Portuguese", "Portuguese"),
    "ko-KR": ("Korean", "Korean"),
    "id-ID": ("Indonesian", "Indonesian"),
    "de-DE": ("German", "German"),
    "ja-JP": ("Japanese", "Japanese"),
    "it-IT": ("Italian", "Italian"),
    "zh-CN": ("Chinese", "Chinese"),
    "zh-HK": ("Chinese,Yue", "Cantonese"),
    "auto": ("auto", "Auto"),
}

# Language codes mapping (for backward compatibility)
LANGUAGE_CODES = {
    "spanish": "es-ES",
    "french": "fr-FR",
    "portuguese": "pt-PT",
    "korean": "ko-KR",
    "indonesian": "id-ID",
    "german": "de-DE",
    "japanese": "ja-JP",
    "italian": "it-IT",
    "chinese": "zh-CN",
    "cantonese": "zh-HK",
    "auto": "auto",
}

def get_language_api_value(iso_code: str) -> str:
    """Get the API language value from ISO code."""
    return LANGUAGE_MAPPINGS[iso_code][0]

def get_language_display_name(iso_code: str) -> str:
    """Get the display name from ISO code."""
    return LANGUAGE_MAPPINGS[iso_code][1]

# TTS voices per language
TTS_VOICES = {
    "zh-HK": {
        "Cantonese_ProfessionalHost（F)": "Professional Female Host",
        "Cantonese_GentleLady": "Gentle Lady",
        "Cantonese_ProfessionalHost（M)": "Professional Male Host",
        "Cantonese_PlayfulMan": "Playful Man",
        "Cantonese_CuteGirl": "Cute Girl",
        "Cantonese_KindWoman": "Kind Woman",
        "Cantonese_Narrator": "Narrator",
        "Cantonese_WiselProfessor": "Wise Professor",
        "Cantonese_IndifferentStaff": "Indifferent Staff"
    },
    "zh-CN": [
        "Abbess",
        "Calm_Woman",
        "Casual_Guy",
        "Decent_Boy",
        "Deep_Voice_Man",
        "Determined_Man",
        "Elegant_Man",
        "Exuberant_Girl",
        "Friendly_Person",
        "Imposing_Manner",
        "Inspirational_girl",
        "Lively_Girl",
        "Lovely_Girl",
        "Patient_Man",
        "Sweet_Girl_2",
        "Wise_Woman",
        "Young_Knight",
    ],
}
