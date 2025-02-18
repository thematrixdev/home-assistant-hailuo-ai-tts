"""Constants for the Hailuo AI TTS integration."""

DOMAIN = "hailuo_ai_tts"

CONF_GROUP_ID = "group_id"
CONF_API_KEY = "api_key"
CONF_SERVER = "server"
CONF_MODEL = "model"
CONF_SPEED = "speed"
CONF_VOL = "vol"
CONF_PITCH = "pitch"
CONF_VOICE = "voice"
CONF_EMOTION = "emotion"
CONF_ENGLISH_NORMALIZATION = "english_normalization"
CONF_LANGUAGE = "language"
CONF_MODEL_NAME = "model_name"
CONF_VOICE_NAME = "voice_name"
CONF_EMOTION_NAME = "emotion_name"
CONF_LANGUAGE_NAME = "language_name"
CONF_CUSTOM_VOICE_ID = "custom_voice_id"
CONF_CUSTOM_VOICE_NAME = "custom_voice_name"

# Default values
DEFAULT_LANGUAGE = "zh-HK"
DEFAULT_SERVER = "international"
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

# Format: ISO code -> (API value, Display name)
LANGUAGE_MAPPINGS = {
    "ar-EG": ("Arabic", "Arabic"),
    "de-DE": ("German", "German"),
    "en-UK": ("English", "English (UK)"),
    "en-US": ("English", "English (US)"),
    "es-ES": ("Spanish", "Spanish"),
    "fr-FR": ("French", "French"),
    "id-ID": ("Indonesian", "Indonesian"),
    "it-IT": ("Italian", "Italian"),
    "ja-JP": ("Japanese", "Japanese"),
    "ko-KR": ("Korean", "Korean"),
    "nl-NL": ("Dutch", "Dutch"),
    "pt-PT": ("Portuguese", "Portuguese"),
    "ru-RU": ("Russian", "Russian"),
    "tr-TR": ("Turkish", "Turkish"),
    "uk-UA": ("Ukrainian", "Ukrainian"),
    "vi-VN": ("Vietnamese", "Vietnamese"),
    "zh-CN": ("Chinese", "Chinese (Simplified)"),
    "zh-HK": ("Chinese,Yue", "Cantonese"),
    "auto": ("auto", "Auto"),
}

LANGUAGE_CODES = {
    "arabic": "ar-EG",
    "german": "de-DE",
    "english_uk": "en-UK",
    "english_us": "en-US",
    "spanish": "es-ES",
    "french": "fr-FR",
    "indonesian": "id-ID",
    "italian": "it-IT",
    "japanese": "ja-JP",
    "korean": "ko-KR",
    "dutch": "nl-NL",
    "portuguese": "pt-PT",
    "russian": "ru-RU",
    "turkish": "tr-TR",
    "ukrainian": "uk-UA",
    "vietnamese": "vi-VN",
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

TTS_VOICES = {
    "ar-EG": {
        "Arabic_CalmWoman": "Calm Woman",
        "Arabic_FriendlyGuy": "Friendly Guy",
    },
    "de-DE": {
        "German_FriendlyMan": "Friendly Man",
        "German_PlayfulMan": "Playful Man",
        "German_SweetLady": "Sweet Lady",
    },
    "en-UK": {
        "English_Comedian": "Comedian",
        "English_compelling_lady1": "Compelling Lady",
        "English_Deep-VoicedGentleman": "Deep-voiced Gentleman",
        "English_DecentYoungMan": "Decent Young Man",
        "English_expressive_narrator": "Expressive Narrator",
        "English_AnimeCharacter": "Female Narrator",
        "English_Graceful_Lady": "Graceful Lady",
        "English_ImposingManner": "Imposing Queen",
        "English_LovelyGirl": "Lovely Girl",
        "English_MaturePartner": "Mature Partner",
        "English_PatientMan": "Patient Man",
        "English_SadTeen": "Teen Boy",
        "English_SentimentalLady": "Sentimental Lady",
        "English_Strong-WilledBoy": "Strong-Willed Boy",
        "English_UpsetGirl": "Upset Girl",
        "English_Wiselady": "Wise Lady",
        "English_WiseScholar": "Wise Scholar",
    },
    "en-US": {
        "English_AssertiveQueen": "Assertive Queen",
        "English_BossyLeader": "Bossy Leader",
        "English_MatureBoss": "Bossy Lady",
        "English_captivating_female1": "Captivating Female",
        "English_CaptivatingStoryteller": "Captivating Storyteller",
        "English_CalmWoman": "Calm Woman",
        "English_ConfidentWoman": "Confident Woman",
        "English_Debator": "Male Debater",
        "English_FriendlyPerson": "Friendly Guy",
        "English_Gentle-voiced_man": "Gentle-voiced Man",
        "English_Jovialman": "Jovial Man",
        "English_Kind-heartedGirl": "Kind-Hearted Girl",
        "English_magnetic_voiced_man": "Magnetic-voiced Male",
        "English_ManWithDeepVoice": "Man With Deep Voice",
        "English_PassionateWarrior": "Passionate Warrior",
        "English_PlayfulGirl": "Playful Girl",
        "English_radiant_girl": "Radiant Girl",
        "English_ReservedYoungMan": "Reserved Young Man",
        "English_SereneWoman": "Serene Woman",
        "English_Soft-spokenGirl": "Soft-Spoken Girl",
        "English_Steadymentor": "Reliable Man",
        "English_StressedLady": "Stressed Lady",
        "English_Trustworth_Man": "Trustworthy Man",
        "English_Upbeat_Woman": "Upbeat Woman",
        "English_WhimsicalGirl": "Whimsical Girl",
        "English_Whispering_girl": "Whispering girl",
    },
    "es-ES": {
        "Spanish_AngryMan": "Angry Man",
        "Spanish_Arnold": "Arnold",
        "Spanish_AssertiveQueen": "Assertive Queen",
        "Spanish_CaringGirlfriend": "Caring Girlfriend",
        "Spanish_ChattyGirl": "Chatty Girl",
        "Spanish_Comedian": "Comedian",
        "Spanish_CompellingGirl": "Compelling Girl",
        "Spanish_Debator": "Debator",
        "Spanish_EnergeticBoy": "Energetic Boy",
        "Spanish_Ghost": "Ghost",
        "Spanish_HumorousElder": "Humorous Elder",
        "Spanish_Intonategirl": "Intonate Girl",
        "Spanish_Jovialman": "Jovial Man",
        "Spanish_PassionateWarrior": "Passionate Warrior",
        "Spanish_PowerfulSoldier": "Powerful Soldier",
        "Spanish_PowerfulVeteran": "Powerful Veteran",
        "Spanish_ReliableMan": "Reliable Man",
        "Spanish_RomanticHusband": "Romantic Husband",
        "Spanish_Rudolph": "Rudolph",
        "Spanish_SantaClaus": "Santa Claus",
        "Spanish_SensibleManager": "Sensible Manager",
        "Spanish_SereneElder": "Serene Elder",
        "Spanish_Steadymentor": "Steady Mentor",
        "Spanish_StrictBoss": "Strict Boss",
        "Spanish_ThoughtfulLady": "Thoughtful Lady",
        "Spanish_ToughBoss": "Tough Boss",
        "Spanish_WhimsicalGirl": "Whimsical Girl",
        "Spanish_Wiselady": "Wise Lady",
    },
    "fr-FR": {
        "French_CasualMan": "Casual Man",
        "French_Female Journalist": "Fluent Female Broadcaster",
        "French_Male_Speech_New": "Level-Headed Man",
        "French_MaleNarrator": "Male Narrator",
        "French_MovieLeadFemale": "Movie Lead Female",
        "French_Female_News Anchor": "Patient Female Presenter",
        "French_Female_Speech_New": "Persuasive Female Speaker",
        "French_FemaleAnchor": "Female Anchor",
    },
    "id-ID": {
        "Indonesian_BossyLeader": "Bossy Leader",
        "Indonesian_CalmWoman": "Calm Woman",
        "Indonesian_CaringMan": "Caring Man",
        "Indonesian_CharmingGirl": "Charming Girl",
        "Indonesian_ConfidentWoman": "Confident Woman",
        "Indonesian_DeterminedBoy": "Determined Boy",
        "Indonesian_GentleGirl": "Gentle Girl",
        "Indonesian_ReservedYoungMan": "Reserved Young Man",
        "Indonesian_SweetGirl": "Sweet Girl",
    },
    "it-IT": {
        "Italian_ArrogantPrincess": "Arrogant Princess",
        "Italian_AthleticStudent": "Athletic Student",
        "Italian_BraveHeroine": "Brave Heroine",
        "Italian_DiligentLeader": "Diligent Leader",
        "Italian_Narrator": "Narrator",
        "Italian_ReliableMan": "Reliable Man",
        "Italian_WanderingSorcerer": "Wandering Sorcerer",
    },
    "ja-JP": {
        "Japanese_CalmLady": "Calm Lady",
        "Japanese_ColdQueen": "Cold Queen",
        "Japanese_DecisivePrincess": "Decisive Princess",
        "Japanese_DependableWoman": "Dependable Woman",
        "Japanese_DominantMan": "Dominant Man",
        "Japanese_GenerousIzakayaOwner": "Generous Izakaya Owner",
        "Japanese_GentleButler": "Gentle Butler",
        "Japanese_GracefulMaiden": "Graceful Maiden",
        "Japanese_InnocentBoy": "Innocent Boy",
        "Japanese_IntellectualSenior": "Intellectual Senior",
        "Japanese_KindLady": "Kind Lady",
        "Japanese_LoyalKnight": "Loyal Knight",
        "Japanese_OptimisticYouth": "Optimistic Youth",
        "Japanese_SeriousCommander": "Serious Commander",
        "Japanese_SportyStudent": "Sporty Student",
    },
    "ko-KR": {
        "Korean_AthleticStudent": "Athletic Student",
        "Korean_BossyMan": "Bossy Man",
        "Korean_BraveAdventurer": "Brave Adventurer",
        "Korean_BraveFemaleWarrior": "Brave Female Warrior",
        "Korean_BraveYouth": "Brave Youth",
        "Korean_CalmGentleman": "Calm Gentleman",
        "Korean_CalmLady": "Calm Lady",
        "Korean_CharmingSister": "Charming Sister",
        "Korean_CheerfulBoyfriend": "Cheerful Boyfriend",
        "Korean_CheerfulCoolJunior": "Cheerful Cool Junior",
        "Korean_ChildhoodFriendGirl": "Childhood Friend Girl",
        "Korean_ColdYoungMan": "Cold Young Man",
        "Korean_DecisiveQueen": "Decisive Queen",
        "Korean_ElegantPrincess": "Elegant Princess",
        "Korean_EnchantingSister": "Enchanting Sister",
        "Korean_EnthusiasticTeen": "Enthusiastic Teen",
        "Korean_InnocentBoy": "Innocent Boy",
        "Korean_IntellectualSenior": "Intellectual Senior",
        "Korean_LonelyWarrior": "Lonely Warrior",
        "Korean_MatureLady": "Mature Lady",
        "Korean_MysteriousGirl": "Mysterious Girl",
        "Korean_PlayboyCharmer": "Playboy Charmer",
        "Korean_PowerfulGirl": "Powerful Girl",
        "Korean_ReliableSister": "Reliable Sister",
        "Korean_SassyGirl": "Sassy Girl",
        "Korean_ShyGirl": "Shy Girl",
        "Korean_SoothingLady": "Soothing Lady",
        "Korean_StrictBoss": "Strict Boss",
        "Korean_SweetGirl": "Sweet Girl",
        "Korean_WiseElf": "Wise Elf",
    },
    "nl-NL": {
        "Dutch_bossy_leader": "Bossy leader",
        "Dutch_kindhearted_girl": "Kind-hearted girl",
    },
    "pt-PT": {
        "Portuguese_AngryMan": "Angry Man",
        "Portuguese_AnimeCharacter": "Anime Character",
        "Portuguese_AnxiousMan": "Anxious Man",
        "Portuguese_AttractiveGirl": "Attractive Girl",
        "Portuguese_BossyLeader": "Bossy Leader",
        "Portuguese_CaptivatingStoryteller": "Captivating Storyteller",
        "Portuguese_ConfidentWoman": "Confident Woman",
        "Portuguese_CuteElf": "Cute Elf",
        "Portuguese_Debator": "Debator",
        "Portuguese_Deep-tonedMan": "Deep-toned Man",
        "Portuguese_Deep-VoicedGentleman": "Deep-voiced Gentleman",
        "Portuguese_EnergeticGirl": "Energetic Girl",
        "Portuguese_FunnyGuy": "Funny Guy",
        "Portuguese_Godfather": "Godfather",
        "Portuguese_Grinch": "Grinch",
        "Portuguese_Kind-heartedGirl": "Kind-hearted Girl",
        "Portuguese_Matureresearcher": "Mature Researcher",
        "Portuguese_Nuttylady": "Nutty Lady",
        "Portuguese_Optimisticyouth": "Optimistic youth",
        "Portuguese_PassionateWarrior": "Passionate Warrior",
        "Portuguese_PlayfulGirl": "Playful Girl",
        "Portuguese_Pompouslady": "Pompous lady",
        "Portuguese_ReservedYoungMan": "Reserved Young Man",
        "Portuguese_SentimentalLady": "Sentimental Lady",
        "Portuguese_SmartYoungGirl": "Smart Young Girl",
        "Portuguese_Strong-WilledBoy": "Strong-willed Boy",
        "Portuguese_SweetGirl": "Sweet Girl",
        "Portuguese_ThoughtfulMan": "Thoughtful Man",
        "Portuguese_UpsetGirl": "Upset Girl",
        "Portuguese_Wiselady": "Wise lady",
    },
    "ru-RU": {
        "Russian_AmbitiousWoman": "Ambitious Woman",
        "Russian_AttractiveGuy": "Attractive Guy",
        "Russian_Bad-temperedBoy": "Bad-tempered Boy",
        "Russian_BrightHeroine": "Bright Queen",
        "Russian_CrazyQueen": "Crazy Girl",
        "Russian_HandsomeChildhoodFriend": "Handsome Childhood Friend",
        "Russian_PessimisticGirl": "Pessimistic Girl",
        "Russian_ReliableMan": "Reliable Man",
    },
    "tr-TR": {
        "Turkish_CalmWoman": "Calm Woman",
        "Turkish_Trustworthyman": "Trustworthy Man",
    },
    "uk-UA": {
        "Ukrainian_CalmWoman": "Calm Woman",
        "Ukrainian_WiseScholar": "Wise Scholar",
    },
    "vi-VN": {
        "Vietnamese_kindhearted_girl": "Kind-hearted girl",
    },
    "zh-CN": {
        "Arrogant_Miss": "Arrogant Miss",
        "Chinese (Mandarin)_Crisp_Girl": "Crisp Girl",
        "Chinese (Mandarin)_Cute_Spirit": "Cute Spirit",
        "Chinese (Mandarin)_Gentleman": "Gentleman",
        "Chinese (Mandarin)_Gentle_Senior": "Gentle Senior",
        "Chinese (Mandarin)_Gentle_Youth": "Gentle Youth",
        "Chinese (Mandarin)_HK_Flight_Attendant": "HK Flight Attendant",
        "Chinese (Mandarin)_Humorous_Elder": "Humorous Elder",
        "Chinese (Mandarin)_IntellectualGirl": "Intellectual Girl",
        "Chinese (Mandarin)_Kind-hearted_Antie": "Kind-hearted Antie",
        "Chinese (Mandarin)_Kind-hearted_Elder": "Kind-hearted Elder",
        "Chinese (Mandarin)_Lyrical_Voice": "Lyrical Voice",
        "Chinese (Mandarin)_Male_Announcer": "Male Announcer",
        "Chinese (Mandarin)_Mature_Woman": "Mature Woman",
        "Chinese (Mandarin)_News_Anchor": "News Anchor",
        "Chinese (Mandarin)_Pure-hearted_Boy": "Pure-hearted Boy",
        "Chinese (Mandarin)_Radio_Host": "Radio Host",
        "Chinese (Mandarin)_Refreshing_Young_Man": "Refreshing Young Man",
        "Chinese (Mandarin)_Reliable_Executive": "Reliable Executive",
        "Robot_Armor": "Robot Armor",
        "Chinese (Mandarin)_Sincere_Adult": "Sincere Adult",
        "Chinese (Mandarin)_Soft_Girl": "Soft Girl",
        "Chinese (Mandarin)_Southern_Young_Man": "Southern Young Man",
        "Chinese (Mandarin)_Straightforward_Boy": "Straightforward Boy",
        "Chinese (Mandarin)_Stubborn_Friend": "Stubborn Friend",
        "Chinese (Mandarin)_Sweet_Lady": "Sweet Lady",
        "Chinese (Mandarin)_Unrestrained_Young_Man": "Unrestrained Young Man",
        "Chinese (Mandarin)_Warm_Bestie": "Warm Bestie",
        "Chinese (Mandarin)_Warm_Girl": "Warm Girl",
        "Chinese (Mandarin)_Wise_Women": "Wise Women",
    },
    "zh-HK": {
        "Cantonese_CuteGirl": "Cute Girl",
        "Cantonese_GentleLady": "Gentle Lady",
        "Cantonese_IndifferentStaff": "Indifferent Staff",
        "Cantonese_KindWoman": "Kind Woman",
        "Cantonese_Narrator": "Narrator",
        "Cantonese_PlayfulMan": "Playful Man",
        "Cantonese_ProfessionalHost（F)": "Professional Female Host",
        "Cantonese_ProfessionalHost（M)": "Professional Male Host",
        "Cantonese_WiselProfessor": "Wise Professor",
    },
}