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
        self.voice_error = 'Can you repeat?'
        self.request_error = 'Something went wrong, try again.'
        self.greet_user = 'Hello, how can i help you?'
        self.reset_message = 'Sum reseted.'
        self.assistant()


    def assistant(self):
        # Call the assistant to greet
        self.assistant_speak(self.greet_user)
        time.sleep(0.2)
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
            self.assistant_speak('Bye.')
            exit()
        if 'close' in request: 
            self.assistant_speak('Bye.')
            exit()
        if 'tell me the total' in request:
            self.assistant_speak('The sum is ' + str(self.sum))
        # Reset the Sum 
        if 'reset' in request:
            self.sum = 0
            self.assistant_speak(self.reset_message)
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
                voice_data = 'error'
            except sr.RequestError:
                self.assistant_speak(self.request_error)
                voice_data = 'error'
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
        # Ask if you want to add to the current sum
        self.assistant_speak('Add to the sum?')
        data = self.assistant_listen()
        while data == 'error':
            self.assistant_speak('Add to the sum?')
            data = self.assistant_listen()
        data = data.split()

        if 'yes' in data:
            self.assistant_speak('How much to add?')
            data = self.assistant_listen()
            while data == 'error':
                self.assistant_speak('Can you repeat?')
                data = self.assistant_listen()
            data = data.split()
            if len(data) == 1:
                self.sum += (int(data[0]))
            else:
                for iter, item in enumerate(data):
                    if item == '+' or item == 'plus':
                        self.sum += (int(data[iter + 1]))
            self.assistant_speak('The sum is ' + str(self.sum))
        elif 'no' in data:
            # Reset the sum
            self.sum = 0
            self.assistant_speak('What do you want to add?')
            data = self.assistant_listen()
            while data == 'error':
                self.assistant_speak('What do you want to add?')
                data = self.assistant_listen()
            data = data.split()
            added_first = True
            for iter, item in enumerate(data):
                if item == '+' or item == 'plus':
                    if added_first:
                        added_first = False
                        self.sum = (int(data[iter - 1]))
                    self.sum += (int(data[iter + 1]))
            self.assistant_speak('The sum is ' + str(self.sum))


    def subtraction(self):
        # Ask if you want to subtract from the current sum
        self.assistant_speak('Subtract from sum?')
        data = self.assistant_listen()
        while data == 'error':
            self.assistant_speak('Can you repeat?')
            data = self.assistant_listen()
        data = data.split()

        if 'yes' in data:
            self.assistant_speak('How much to subtract?')
            data = self.assistant_listen()
            while data == 'error':
                self.assistant_speak('Can you repeat?')
                data = self.assistant_listen()
            data = data.split()
            # print(data)
            # print(len(data))
            if len(data) == 1:
                '''
                If the len(data)==1 then given number is already negative
                so in order to subtract you have to add it
                '''
                self.sum += (int(data[0]))
            else:
                for iter, item in enumerate(data):
                    if item == '-' or item == 'minus':
                        self.sum -= (int(data[iter + 1]))
            self.assistant_speak('The sum is ' + str(self.sum))

        elif 'no' in data:
            # If want to subtract with sum = 0
            self.sum = 0
            self.assistant_speak('What do you want to subtract?')
            data = self.assistant_listen()
            # Loop while the voice has error
            while data == 'error':
                self.assistant_speak('Can you repeat?')
                data = self.assistant_listen()
            # Add the first number before the + ex. (1 - 2 - 3)
            data = data.split()
            added_first = True
            for iter, item in enumerate(data):
                if item == '-' or item == 'minus':
                    if added_first:
                        added_first = False
                        self.sum = (int(data[iter - 1]))
                    self.sum -= (int(data[iter + 1]))
            self.assistant_speak('The sum is ' + str(self.sum))

    def multiplication(self):
        # Ask if you want to subtract from the current sum
        self.assistant_speak('Multiply the sum?')
        data = self.assistant_listen()
        while data == 'error':
            self.assistant_speak('Can you repeat?')
            data = self.assistant_listen()
        data = data.split()

        if 'yes' in data:
            self.assistant_speak('How much to multiply?')
            data = self.assistant_listen()
            while data == 'error':
                self.assistant_speak('Can you repeat?')
                data = self.assistant_listen()
            data = data.split()
            # print('#####')
            # print(data)
            self.sum *= int(data[1])
            self.assistant_speak('The sum is ' + str(self.sum))

        elif 'no' in data:
            self.sum = 0
            self.assistant_speak('How much to multiply?')
            data = self.assistant_listen()
            while data == 'error':
                self.assistant_speak('Can you repeat?')
                data = self.assistant_listen()
            data = data.split()
            added_first = True
            for iter, item in enumerate(data):
                if item == '*' or item == 'times':
                    if added_first:
                        added_first = False
                        self.sum = int(data[iter - 1])
                    self.sum *= int(data[iter + 1])
            self.assistant_speak('The sum is ' + str(self.sum))


    def division(self):
        pass

if __name__ == "__main__":
    Calculator()
