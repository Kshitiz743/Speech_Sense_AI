from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import session
from audio_converter import convert_audio
import os


from analysis_engine import analyze_speech
app = Flask(__name__)
app.secret_key = "SpeechSense_AI_Project_2026"

UPLOAD_FOLDER = os.path.join(
                    os.getcwd(),
                    "uploads"
                    )


os.makedirs(
            UPLOAD_FOLDER,
            exist_ok=True
            )


app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    

    audio = request.files.get("audio")

    if audio is None:
        return redirect("/")

    if audio.filename == "":
        return redirect("/")


    path = os.path.join(

            app.config["UPLOAD_FOLDER"],

            audio.filename

            )


    audio.save(path)
    print("\n")
    print("====================================")

    print("UPLOAD SUCCESSFUL") 
    print("====================================")
    print("Filename :", audio.filename)
    print("Saved Path :", path) 
    print("====================================")
    print("\n")


    path = convert_audio(path)
    print("\n")
    print("AFTER CONVERSION")
    print("Current Path :", path)
    print("\n")



    session["filepath"] = os.path.abspath(path)


    return redirect("/processing")
@app.route("/processing")
def processing():

    return render_template(
            "processing.html"
            )
@app.route("/analyze")
def analyze():

    path = session["filepath"]


    results = analyze_speech(path)


    return render_template(

            "result.html",

            result=results

            )

if __name__ == "__main__":
    app.run(debug=True)