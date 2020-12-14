from flask import Flask
from flask import render_template
from flask import request

from libs.daten import *

app = Flask("Kursfinder")


@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Kursfinder Website"
    einleitung_text = "Hier kannst du herausfinden, welchen Pfadikurs du als nächstes besuchen kannst"
    return render_template("start.html", app_name="Kursfinder", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    if request.method == "POST":
        email = request.form['input_email']
        name = request.form['input_name']
        jahrgang = request.form['input_jahrgang']
        kurs = request.form['input_kurs']
        jahr = request.form['input_jahr']
        speichern(str(email), name, jahrgang, kurs, jahr)
        recs_list = get_recs(email)
        return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung", recs_list=recs_list)
    return render_template('eingabe.html', app_name="Kursfinder - Eingabe", kurse=laden_kursdaten())


@app.route('/empfehlung', methods=['POST', 'GET'])
def empfehlung():
    if request.method == "POST":
        email = request.form['input_email']
        if check_email(email) is False:
            return render_template('eingabe.html', app_name="Kursfinder - Empfehlung", error="E-Mail nicht vorhanden. Zuerst registrieren!")
        recs_list = get_recs(email)
        return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung", recs_list=recs_list)
    return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung")


@app.route('/neuer_kurs', methods=['POST', 'GET'])
def neuer_kurs():
    if request.method == "POST":
        name = request.form['input_name']
        jahrgang = request.form['input_jahrgang']
        gueltigkeit = request.form['input_gueltigkeit']
        voraussetzung = request.form['input_voraussetzung']
        fortsetzung = request.form['input_fortsetzung']
        kurs_speichern(name, jahrgang, gueltigkeit, voraussetzung, fortsetzung)
        success = f"Kurs gespeichert: Kursname: {name}, Jahrgang: {jahrgang}, Gültigkeit: {gueltigkeit}, Voraussetzung: {voraussetzung}, Fortsetzung: {fortsetzung}"
        return render_template('neuer_kurs.html', app_name="Kursfinder - Neuer Kurs", success=success)
    return render_template('neuer_kurs.html', app_name="Kursfinder - Neuer Kurs")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

