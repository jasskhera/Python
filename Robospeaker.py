import pyttsx3
engine = pyttsx3.init()
print("Welcome to Robospeaker")
while True:
    x = input("Enter text to speak:")
    if x == "q":
        engine.say("Invalid Input, Try Again")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()

