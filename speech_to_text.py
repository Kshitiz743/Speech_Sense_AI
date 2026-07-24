import speech_recognition as sr



def speech_to_text(filepath):


    print("\n")
    print("============================")
    print("CURRENT FILE")
    print(filepath)
    print("============================")


    recognizer = sr.Recognizer()


    with sr.AudioFile(filepath) as source:

        audio = recognizer.record(source)



    try:

        text = recognizer.recognize_google(audio)


        print("\n")
        print("RECOGNIZED TEXT")
        print(text)
        print("\n")


        return text



    except Exception as e:


        print("\n")
        print("ERROR OCCURED")
        print(e)
        print("\n")


        return "Speech could not be recognized."