from elevenlabs.client import ElevenLabs
from elevenlabs import save

AUDIO_RESPONSE_FILENAME = 'media/audio/audio_response.wav'

client = None
voice = None


def load_api(api_key: str, voice_name: str):
    global client, voice
    client = ElevenLabs(api_key=api_key)
    voice = voice_name


def generate_sound(text: str):
    audio = client.generate(text=text, voice=voice, model="eleven_multilingual_v2")
    save(audio, AUDIO_RESPONSE_FILENAME)
    return AUDIO_RESPONSE_FILENAME
