import speech_recognition
import speech_recognition as sr


def recognize() -> str:
    '''
    The function accesses the microphone and returns the recognized speech as a string
    :return: recognized speech (str). If the speech was not recognized, returns an empty string.
    '''
    recognizer = sr.Recognizer()  # Initialize a recognizer
    try:
        with sr.Microphone() as mic:  # Get access to the microphone
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)  # Adjust the recognizer for ambient noise
            print("Listening...")
            audio_data = recognizer.listen(mic)  # Listen to the audio input
        recognized_data = recognizer.recognize_google(audio_data)  # Recognize the text

    except speech_recognition.UnknownValueError:  # There is a recognition error
        recognized_data = ""

    return recognized_data
