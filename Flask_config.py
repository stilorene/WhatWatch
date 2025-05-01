from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "0890980800"

@app.route("/", methods=["GET", "POST"])
def home():
    question_number = 1

    if request.method == "POST":

        nav = request.form.get("navigation")
        if nav == "next" and question_number < 3:
            question_number += 1

        elif nav == "prev" and question_number > 1:
            question_number = -1


    block = f"blocks_to_include/question{question_number}.html"
    return render_template("index.html", block_to_include=block, question_number=question_number)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

