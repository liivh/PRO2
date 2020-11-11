from flask import Flask
from flask import render_template
from flask import request

from libs.daten import speichern

app = Flask("Kursfinder")

# git test

@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Kursfinder Website"
    einleitung_text = "Hier kannst du herausfinden, welchen Pfadikurs du als nächstes besuchen kannst"
    return render_template("start.html", app_name="Kursfinder", ueberschrift=ueberschrifts_text,
                           einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    if request.method == "POST":
        nummer = request.form['nummer_input']
        jahrgang = request.form['jahrgang']
        kurs = request.form['kurs']
        jahr = request.form['jahr']
        antwort = speichern(nummer, jahrgang, kurs, jahr)
        return 'Gespeicherete Daten: <br>' + str(antwort)
    return render_template('eingabe.html', app_name="Kursfinder - Eingabe")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
