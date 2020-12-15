from flask import Flask
from flask import render_template
from flask import request

import plotly.express as px
import plotly

from collections import Counter

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

@app.route('/grafik')
def grafik():
    alle_interessierte = alle_kurse()
    kurse = list(alle_interessierte.keys())
    anzahl = list(alle_interessierte.values())

    fig = px.bar(x=kurse, y=anzahl)
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)

    return render_template('grafik.html', app_name="Kursfinder", plotly_div=div)



if __name__ == "__main__":
    app.run(debug=True, port=5000)