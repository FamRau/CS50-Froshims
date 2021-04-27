from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Running", "Soccer", "Basketball", "Swimming"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", sports=SPORTS)
    if request.method == "POST":
        if request.form.get("sport") not in SPORTS:
            return render_template("failure.html")
        else:    
            return render_template("success.html")


