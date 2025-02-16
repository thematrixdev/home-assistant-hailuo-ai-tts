""" Constants for Hailuo AI TTS custom component"""

DOMAIN = "hailuo_ai_tts"
CONF_GROUP_ID = "group_id"
CONF_API_KEY = 'api_key'
CONF_MODEL = 'model'
CONF_SPEED = 'speed'
CONF_VOL = 'vol'
CONF_PITCH = 'pitch'
CONF_VOICE = 'voice'
CONF_EMOTION = 'emotion'
CONF_ENGLISH_NORMALIZATION = 'english_normalization'
CONF_LANGUAGE = 'language'

# Display name constants
CONF_MODEL_NAME = 'model_name'
CONF_VOICE_NAME = 'voice_name'
CONF_EMOTION_NAME = 'emotion_name'
CONF_LANGUAGE_NAME = 'language_name'

UNIQUE_ID = 'unique_id'

# Model options
MODELS = {
    "speech-01-turbo": "Turbo",
    "speech-01-hd": "HD"
}

# Voice options - sorted by display name
VOICES = {
    "Abbess": "Abbess",
    "Calm_Woman": "Calm Woman",
    "Casual_Guy": "Casual Guy",
    "Decent_Boy": "Decent Boy",
    "Deep_Voice_Man": "Deep Voice Man",
    "Determined_Man": "Determined Man",
    "Elegant_Man": "Elegant Man",
    "Exuberant_Girl": "Exuberant Girl",
    "Friendly_Person": "Friendly Person",
    "Imposing_Manner": "Imposing Manner",
    "Inspirational_girl": "Inspirational Girl",
    "Lively_Girl": "Lively Girl",
    "Lovely_Girl": "Lovely Girl",
    "Patient_Man": "Patient Man",
    "Sweet_Girl_2": "Sweet Girl 2",
    "Wise_Woman": "Wise Woman",
    "Young_Knight": "Young Knight"
}

# Emotion options
EMOTIONS = {
    "": "None",
    "happy": "Happy",
    "sad": "Sad",
    "angry": "Angry",
    "fearful": "Fearful",
    "disgusted": "Disgusted",
    "surprised": "Surprised",
    "neutral": "Neutral"
}

# Language options
LANGUAGES = {
    "Spanish": "Spanish",
    "French": "French",
    "Portuguese": "Portuguese",
    "Korean": "Korean",
    "Indonesian": "Indonesian",
    "German": "German",
    "Japanese": "Japanese",
    "Italian": "Italian",
    "Chinese": "Chinese",
    "Chinese,Yue": "Cantonese",
    "auto": "Auto Detect"
}

# Defaults
DEFAULT_LANGUAGE = "auto"
DEFAULT_SPEED = 1.0
DEFAULT_VOL = 1.0
DEFAULT_PITCH = 0
DEFAULT_ENGLISH_NORMALIZATION = False
