from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask import (
    Flask,
    render_template,
    redirect,
    request,
    session
)

from audio_converter import convert_audio
from analysis_engine import analyze_speech

import os
import sqlite3





BASE_DIR = os.path.abspath(
            os.path.dirname(__file__)
            )

DATABASE_PATH = os.path.join(
                BASE_DIR,
                "users.db"
                )


def get_connection():

    return sqlite3.connect(
            DATABASE_PATH
            )
def create_database():
    print(DATABASE_PATH)

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

    )

    """)

    connection.commit()

    connection.close()


app = Flask(__name__)
app.secret_key = "SpeechSense_AI_Project_2026"

create_database()


@app.route("/signup")
def signup_page():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    hashed_password = generate_password_hash(password)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users(
        username,
        email,
        password
        )
        VALUES(?,?,?)
        """,
        (
            username,
            email,
            hashed_password
        )
    )

    connection.commit()
    connection.close()

    return redirect("/login")


@app.route("/")
def root():
    return redirect("/login")


@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email=?
        """,
        (email,)
    )

    user = cursor.fetchone()
    connection.close()

    if user and check_password_hash(
        user[3],
        password
    ):
        session["username"] = user[1]
        return redirect("/home")

    return redirect("/login")


@app.route("/home")
def home():
    if "username" not in session:
        return redirect("/login")

    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


UPLOAD_FOLDER = os.path.join(
    os.getcwd(),
    "uploads"
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/upload", methods=["POST"])
def upload():
    if "username" not in session:
        return redirect("/login")

    audio = request.files.get("audio")

    if audio is None:
        return redirect("/home")

    if audio.filename == "":
        return redirect("/home")

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        audio.filename
    )

    audio.save(path)

    print("\n====================================")
    print("UPLOAD SUCCESSFUL")
    print("====================================")
    print("Filename :", audio.filename)
    print("Saved Path :", path)
    print("====================================\n")

    path = convert_audio(path)

    print("\nAFTER CONVERSION")
    print("Current Path :", path)
    print()

    session["filepath"] = os.path.abspath(path)

    return redirect("/processing")


@app.route("/processing")
def processing():
    if "username" not in session:
        return redirect("/login")

    if "filepath" not in session:
        return redirect("/home")

    return render_template("processing.html")


@app.route("/analyze")
def analyze():
        path=session["filepath"]

        text=speech_to_text(path)
   
        return text




if __name__ == "__main__":
    app.run(debug=True)