# importing


import random
import time
import webbrowser
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import datetime
import requests

# from pytube import YouTube

# importing

# introducing variables

HOUR = datetime.datetime.now().hour
week_day = datetime.datetime.today().isoweekday()
news_json = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=755192fc0bbe4efcaa982719dc1f0ed1")
source = news_json.json()["articles"][2]["title"]
listener = sr.Recognizer()
engine = pyttsx3.init()
__siri___ = True
# introducing variables

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 178)


# definitions


# Speak(text="I am Jarvis Sir. Please tell me how may I help you")


def Speak(**kwargs):
    for _ in kwargs.items():
        engine.say(**kwargs)
        engine.runAndWait()


Speak(text="Power on")
time.sleep(1)
Speak(text="Initializing Siri...............")


def Wish():
    if 0 <= HOUR < 12:
        Speak(text="Good Morning!")

    elif 12 <= HOUR < 18:
        Speak(text="Good Afternoon!")

    else:
        Speak(text="Good Evening!")


Wish()


def taking_command():
    try:
        with sr.Microphone() as SOURCE:
            voice = listener.listen(SOURCE)
            command = listener.recognize_google(voice)
            command = command.lower()

    except:
        pass
    return command


def take_command():
    try:
        with sr.Microphone() as SOURCE:
            Speak(text="waiting for your command.")
            print("Waiting for your command..............")
            voice = listener.listen(SOURCE)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "alexa" in command:
                command = command.replace("siri", " ")
                print(command)
    except KeyboardInterrupt:
        print(KeyboardInterrupt)
    return command


def Siri():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        Speak(text="playing " + song)
        pywhatkit.playonyt(song)
        if "download video" in command:
            pass
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        Speak(text="Current time is " + current_time)
        print(current_time)
    elif "random number" in command:
        random_num = random.randint(1, 100000)
        Speak(text=random_num)
        print(random_num)
    elif "What can you do ?" in command:
        Speak(text="I can search wikipedia for you, open youtube or google, I can let you know what is the current time, I can tell you a joke, I can play songs for you...........")
        Speak(text="What can I do for you ?")
    elif "open google" in command:
        webbrowser.open("google.com")
    elif "open youtube" in command:
        webbrowser.open("youtube")

    elif "stop" in command:
        Speak(text="power off.")
        Speak(text="This process has finished with exit code 0")
        quit()

    elif 'wikipedia' in command:
        Speak(text="Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        Speak(text="According to Wikipedia")
        print(results)
        Speak(text=results)

    elif "quote" in command:
        command.replace("quote", "")
        random_number = random.randint(1, 1642)
        quote = requests.get("https://type.fit/api/quotes").json()[random_number]["text"]
        author = requests.get("https://type.fit/api/quotes").json()[random_number]["author"]
        print(quote, " ", "-", author)
        Speak(text=quote)
        Speak(text=author)
    elif "list country" in command:
        countries = requests.get("https://countriesnow.space/api/v0.1/countries").json()["data"]
        capitals = requests.get("https://countriesnow.space/api/v0.1/countries/capital").json()["data"]
        for i in range(0, 229):
            print("Fetching data from api......")
            country = countries[i]["country"]
            capital = capitals[i]["capital"]
            print(i, country)
            Speak(text=country)
            print(i, capital)
            Speak(text=capital)

    elif "headlines" in command:
        for i in range(1, 20):
            news_json_link = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=755192fc0bbe4efcaa982719dc1f0ed1")
            source_of_news = news_json_link.json()["articles"][i]["title"]
            Speak(text="Today's headlines are as follows : ")
            print(source_of_news)
            Speak(text=source_of_news)

    elif "weather" in command:
        weather_api = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=13.082680&lon=80.270721&exclude=weekly&appid=a033095717e3d13b07057f3725502834")
        weather_today_in_json = weather_api.json()
        feels_like_weather = weather_today_in_json["daily"][week_day]

        print("Pressure in pascal : ")
        Speak(text="Pressure in pascal: ")
        print(feels_like_weather["pressure"])
        Speak(text=feels_like_weather["pressure"])

        print("Humidity in water vapor per kilogram of air : ")
        Speak(text="Humidity in water vapor per kilogram of air : ")
        print(feels_like_weather["humidity"])
        Speak(text=feels_like_weather["humidity"])

        print("Wind Speed in meters per second : ")
        Speak(text="Wind Speed in meters per second : ")
        print(feels_like_weather["wind_speed"])
        Speak(text=feels_like_weather["wind_speed"])

    # elif "get space photos" in command:
    #     for i in range(0, 10):
    #         space_pic_url = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()["photos"][i]["img_src"]
    #         space_pic_url_date = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()["photos"][i]["earth_date"]
    #         webbrowser.open_new_tab(space_pic_url)
    #         # print(space_pic_url_date)

    else:
        Speak(text="Please say the command again.")


# definitions


while __siri___:
    Siri()
