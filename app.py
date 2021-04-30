from flask import Flask, redirect, render_template, request
import sqlite3 as sql
app = Flask(__name__)

SPORTS = ["Running", "Soccer", "Basketball", "Swimming"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    with sql.connect("froshims.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO registrants (name, sport) VALUES (?, ?)", (name, sport))
        con.commit()
        return render_template("success.html", message="Succesfully registered")
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    with sql.connect("froshims.db") as con:
        cur = con.cursor()
        registrants = cur.execute("select * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
    close(con)
