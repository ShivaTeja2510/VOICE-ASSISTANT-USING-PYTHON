# ==== Importing all the necessary libraries
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk


# ==== Class Assistant
class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="images/frame_image.jpg")
        left = Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        # ====start button
        start = Button(self.root, text='START', font = ("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font = ("times new roman", 14), command=self.close_window).place(x=350, y=520)

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello Sir,' + wish+' I am your voice assistant. Please tell me how may I help you')
            # ==== Wish End

        # ==== Take Command
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except:
                pass

        # ==== Run command
        def run_command():
            instruction = take_command()
            print(instruction)
            try:
                if 'who are you' in instruction:
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is' + time)

                elif 'open google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('google.com')

                elif 'open youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                elif 'open linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                elif 'open stack overflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')

                elif 'how are you' in instruction:
                    speak('I am just a program, but I am functioning as expected!')

                elif 'tell me a joke' in instruction:
                    speak('Why did the computer show up at work late? It had a hard drive!')

                elif 'what is your name' in instruction:
                    speak('My name is Python Voice Assistant.')

                elif 'open twitter' in instruction:
                    speak('Opening Twitter')
                    webbrowser.open('twitter.com')

                elif 'open github' in instruction:
                    speak('Opening GitHub')
                    webbrowser.open('github.com')

                elif 'date today' in instruction or 'today\'s date' in instruction:
                    today = datetime.datetime.now().strftime('%B %d, %Y')
                    speak('Today is ' + today)

                elif 'thank you' in instruction:
                    speak('You are welcome!')

                elif 'exit' in instruction or 'quit' in instruction:
                    speak('Goodbye!')
                    self.close_window()
                    return False
                
                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    self.close_window()
                    return False

                elif 'thank you' in instruction:
                    speak('You are welcome!')

                elif 'who created you' in instruction:
                    speak('I was created by a Python developer.')

                elif 'what is the weather' in instruction:
                    speak('Sorry, I cannot check the weather right now.')

                elif 'sing a song' in instruction:
                    speak('I am not able to sing, but I can tell you a joke!')

                elif 'tell me something interesting' in instruction:
                    speak('Did you know? The first computer bug was an actual bug!')

                elif 'what is love' in instruction:
                    speak('Love is a complex set of emotions, but I am just a program!')

                elif 'repeat after me' in instruction:
                    speak('Sure! Please say what you want me to repeat.')

                elif 'good morning' in instruction:
                    speak('Good morning! I hope you have a wonderful day!')

                elif 'good night' in instruction:
                    speak('Good night! Sleep well!')

                elif 'how old are you' in instruction:
                    speak('I do not have an age, I exist in the digital world.')

                elif 'can you help me' in instruction:
                    speak('Of course! Please tell me how I can assist you.')

                elif 'exit' in instruction or 'quit' in instruction:
                    speak('Goodbye!')
                    self.close_window()
                    return False

                else:
                    speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True
        
                # ==== Wish Start
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            wish = "Good Morning!"
        elif hour >= 12 and hour < 18:
            wish = "Good Afternoon!"
        else:
            wish = "Good Evening!"
        speak('Hello Sir, ' + wish + ' I am your voice assistant. Please tell me how may I help you')
        # ==== Wish End

        # ====Default Start calling
        start()

        # ====To run assistance continuously
        while True:
            if run_command():
                run_command()
            else:
                break


    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== create tkinter window
root = Tk()


# === creating object for class
obj=assistance_gui(root)

# ==== start the gui
root.mainloop()