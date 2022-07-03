import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def Speaktext(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while(1):
    try:
        print("Say")
        with sr.Microphone() as source1:

            r.adjust_for_ambient_noise(source1, duration=0.2)

            audio2 = r.listen(source1)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say "+MyText)
            Speaktext(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")