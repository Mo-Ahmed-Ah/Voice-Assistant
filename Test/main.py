import warnings
import pyttsx3
import speech_recognition as sr


warnings.filterwarnings("ignore")


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        talk("say anything")
        print("Listening..... ")
        audio = recog.listen(source)
    
    data = ""

    try:
        data= recog.recognize_google_cloud(audio)
        print("You said : " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Rewustes Error : " + ex)
    return data

rec_audio()