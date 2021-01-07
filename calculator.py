import time
import speech_recognition as sr
import os
import random
import playsound
from gtts import gTTS

class Calculator():
    """
    Voice Calculator with voice recognition and text-to-speech
    """
    def __init__(self):
        self.sum = 0
        self.voice_error = 'Sorry, can\'t understand you.'
        self.request_error = 'Something went wrong, try again.'
        self.greet_user = 'Hello, how can i help you?'
        self.assistant()
    
    def assistant(self):
        # Call the assistant to greet
        self.assistant_speak(self.greet_user)
        self.greet_user = 0
        time.sleep(0.5)
        # Loop until input audio = (exit, bye)
        while True:
            action = self.assistant_listen()
            try:
                # Split the text to get the numbers instant
                print(action.split())
            except AttributeError:
                pass
            self.assistant_action(action)
            ''' 
            DEBUG: Repeat the voice recording
            self.assistant_speak(action)
            '''
    
    def assistant_action(self, request):
        # If request is exit, program stops running
        if 'exit' in request: 
            self.assistant_speak('GoodBye.')
            exit()
        if 'close' in request: 
            self.assistant_speak('GoodBye.')
            exit()
        if 'addition' in request:
            self.addition()
        elif 'subtract' in request:
            self.subtraction()
        elif 'multiply' in request:
            self.multiplication()
        elif 'divide' in request:
            self.division() 

    def assistant_listen(self):
        voice_data = []
        # Create a recognizer
        r = sr.Recognizer()
        # Start the recording from the mic
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                self.assistant_speak(self.voice_error)
            except sr.RequestError:
                self.assistant_speak(self.request_error)
        return voice_data

    def assistant_speak(self, audio_string):
        try:
            # Start the Text To Speech 
            tts = gTTS(text=audio_string, lang='en')
            # Create random name for the file
            text_name = random.randint(1, 10_000_000)
            audio_file = 'audio-' + str(text_name) + '.mp3'
            # Save the file
            tts.save(audio_file)
            # Play the file
            playsound.playsound(audio_file)
            # Print the file data
            print(audio_string)
            # Delete the file from OS
            os.remove(audio_file)
        except AssertionError:
            pass

    def addition(self):
        # Ask for the 1st & 2nd number
        self.assistant_speak('What\'s the first number?')
        temp1 = self.assistant_listen()
        self.assistant_speak('What\'s the second number?')
        temp2 = self.assistant_listen()
        result = temp1 + temp2
        self.assistant_speak(result)

    def subtraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass

if __name__ == "__main__":
    Calculator()
