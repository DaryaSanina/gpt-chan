from elevenlabslib import *
import sounddevice as sd
import soundfile as sf

user = None
voice = None
AUDIO_RESPONSE_FILENAME = 'media/audio/audio_response.wav'


def load_api(api_key: str, voice_name: str):
    global user, voice
    user = ElevenLabsUser(api_key)
    voice = user.get_voices_by_name(voice_name)[0]
    voice.generate_audio_bytes('text', 0.75)


def play(text: str):
    if type(voice) == ElevenLabsVoice:
        bytes_data = voice.generate_audio_bytes(text)
        update_audio_file(bytes_data)
        data, fs = sf.read(AUDIO_RESPONSE_FILENAME, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()


def update_audio_file(bytes_sound):
    with open(AUDIO_RESPONSE_FILENAME, mode='wb') as f:
        f.write(bytes_sound)
