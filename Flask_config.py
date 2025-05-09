#Das Skript hier macht vorerst mal nichts, habe hiermit versucht zu arbeiten, zum Teil super aber 
#Main sollte im Web mehr auf Javascript setzen, das funktioniert einfacher und ohne unötige Umwege
#ich verwende dieses hier vl später nochmal wenn es ans Backend und der TMDB-Api geht




from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "0890980800"

questions = ["question1.html", 
             "question2.html",
             "question3.html"]


@app.route("/", methods=["GET", "POST"])
def home():
    if "q_idx" not in session:
        session["q_idx"] = 1 #nötig für die Buttons
        # return render_template("index.html", block_to_include=f"blocks_to_include/question1.html")

    if request.method == "POST":
        nav = request.form.get("navigation")

        # Checkboxen auslesen
        streamprovider = request.form.getlist("Streaming")  # getlist() gibt alle ausgewählten Werte zurück aus dem html

        # Die Buttonlogik ist hier implementiert
        if nav == "next" and session["q_idx"] < 2:
            session["q_idx"] += 1
        
        elif nav == "prev" and session["q_idx"] > 1:
            session["q_idx"] -= 1


        # Lade die gespeicherten Interessen aus der Session
        saved_streamprovider = session.get("interessen", [])
        return render_template("index.html", block_to_include=f"blocks_to_include/question{session["q_idx"]}.html")
    return render_template("index.html", block_to_include=f"blocks_to_include/question1.html")

if __name__ == "__main__":
    app.run(debug=True)

