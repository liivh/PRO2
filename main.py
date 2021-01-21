# Damit die Applikation funktioniert müssen sämtliche Module importiert werden.

from flask import Flask
from flask import render_template
from flask import request, url_for, redirect

import plotly.express as px
import plotly

# Import aller Daten aus dem libs Ordner
from libs.daten import *


app = Flask("Kursfinder")

# Startseite der Webapplikation
@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Kursfinder Website"
    einleitung_text = "Hier kannst du herausfinden, welchen Pfadikurs du als nächstes besuchen kannst"
    # Start.html Template wird gerendert, um diese anzuzeigen
    return render_template("start.html", app_name="Kursfinder", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)

# Eingabeseite der Webapplikation
@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    # Werte des Formulars aus eingabe.html werden abgefangen und gespeichert
    if request.method == "POST":
        email = request.form['input_email']
        name = request.form['input_name']
        jahrgang = request.form['input_jahrgang']
        kurs = request.form['input_kurs']
        jahr = request.form['input_jahr']
        speichern(str(email), name, jahrgang, kurs, jahr)
        # Erfasst der Benutzer seine Daten wird er dann direkt mit redirect auf die Empfehlungseite (empfehlung) weitergeleitet
        return redirect(url_for('empfehlung', email=email))
    return render_template('eingabe.html', app_name="Kursfinder - Eingabe", kurse=laden_kursdaten())

# Empfehlungen der Webapplikation
@app.route('/empfehlung', methods=['POST', 'GET'])
def empfehlung():
    # diese Funktion wird ausgeführt, wenn der Benutzer noch nicht registriert ist (email)
    email = request.args.get('email')
    if request.method == "POST":
        input_email = request.form['input_email']
        # diese Funktion wird ausgeführt, wenn der Benutzer bereits registriert ist (input_email)
        if check_email(input_email) is False:
            return render_template('eingabe.html', kurse=laden_kursdaten(), app_name="Kursfinder - Empfehlung", error="E-Mail nicht vorhanden. Zuerst registrieren!")
        recs_list = get_recs(input_email)
        # dieses Template wird returned, wenn der Benutzer bereits registriert ist (input_email)
        return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung", recs_list=recs_list, email=input_email,
                               db=laden_datenbank(), kurse=laden_kursdaten())
    # dieses Template wird returned, wenn der Benutzer noch nicht registriert war (email)
    return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung", recs_list=get_recs(email), email=email,
                               db=laden_datenbank(), kurse=laden_kursdaten())

# Funktion, wenn der Benutzer seine Benutzerdaten anpasst
@app.route('/empfehlung/edit/<email>', methods=['POST', 'GET'])
# URL-Parameter -> damit Applikation weiss, welche Benutzerdaten angepasst werden
def kurs_edit(email):
    if request.method == "POST":
        # Werte des Formulars werden abgefangen
        name = request.form['edit_name']
        jahrgang = request.form['edit_jahrgang']
        kurs = request.form['edit_kurs']
        jahr = request.form['edit_jahr']
        # Daten werden gespeichert
        speichern(str(email), name, jahrgang, kurs, jahr)
        recs_list = get_recs(email)
        return render_template('empfehlung.html', app_name="Kursfinder - Empfehlung", recs_list=recs_list,
                               email=email, db=laden_datenbank(), kurse=laden_kursdaten())

# Register "Neuer Kurs" der Webapplikation
@app.route('/neuer_kurs', methods=['POST', 'GET'])
def neuer_kurs():
    # Kursinformationen werden abgefragt und abgefangen
    if request.method == "POST":
        name = request.form['input_name']
        jahrgang = request.form['input_jahrgang']
        gueltigkeit = request.form['input_gueltigkeit']
        voraussetzung = request.form['input_voraussetzung']
        fortsetzung = request.form['input_fortsetzung']
        # Kursangaben werden gespeichert
        kurs_speichern(name, jahrgang, gueltigkeit, voraussetzung, fortsetzung)
        # Sobald der Kurs erfolgreich gespeichert wurde, werden dem Nutzer die eingegeben Daten angezeigt
        success = f"Kurs gespeichert: Kursname: {name}, Jahrgang: {jahrgang}, Gültigkeit: {gueltigkeit}, Voraussetzung: {voraussetzung}, Fortsetzung: {fortsetzung}"
        return render_template('neuer_kurs.html', app_name="Kursfinder - Neuer Kurs", success=success)
    return render_template('neuer_kurs.html', app_name="Kursfinder - Neuer Kurs")

# Balkengrafik der Webapplikation
@app.route('/grafik')
def grafik():
    # die Funktion alle_kurse() wird geladen
    alle_interessierte = alle_kurse()
    # Die Keys werden geladen
    kurse = list(alle_interessierte.keys())
    # Die Values werden geladen
    anzahl = list(alle_interessierte.values())

    # mit plotly wird die Visualisierung erstellt
    fig = px.bar(x=kurse, y=anzahl)
    # Visualisierung wird in html Element umgewandelt
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)
    # Daten werden in grafik.html gerendert und div mitgegeben
    return render_template('grafik.html', app_name="Kursfinder", plotly_div=div)



if __name__ == "__main__":
    app.run(debug=True, port=5000)