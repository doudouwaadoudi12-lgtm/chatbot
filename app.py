from flask import Flask, render_template, request

app = Flask(__name__)

# Base de données FAQ
faq = {
    "horaires": "Nous sommes ouverts de 8h à 18h.",
    "contact": "Appelez-nous au 0550 00 00 00.",
    "adresse": "Nous sommes situés à Blida.",
    "services": "Nous offrons des solutions digitales."
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        question = request.form.get("question")
        result = faq.get(question, "Je n'ai pas compris votre question.")

    return render_template("index.html", result=result)

if name == "__main__":
    app.run(debug=True)
