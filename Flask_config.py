from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "0890980800"

@app.route("/")
def home():
    return render_template("index.html", content = "LOL")

# @app.route("/")
# def home():
#     return render_template("base.html", content = "LOL")

if __name__ == "__main__":
    app.run(debug=True)

