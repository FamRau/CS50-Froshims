from flask import Flask, redirect, render_template, request, session
from flask_mail import Mail, Message
from flask_session import Session
import sqlite3 as sql
import os
app = Flask(__name__)



SPORTS = ["Running", "Soccer", "Basketball", "Swimming"]



@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    if not email:
        return render_template("error.html", message="Missing email")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    with sql.connect("froshims.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO registrants (name, sport) VALUES (?, ?)", (email, sport))
        con.commit()
  
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    # with sql.connect("froshims.db") as con:
    #     cur = con.cursor()
    #     rows = cur.execute("select * FROM registrants")
    #     return render_template("registrants.html", rows=rows)
    con = sql.connect("froshims.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM registrants")

    rows = cur.fetchall()
    return render_template("registrants.html", rows = rows)
