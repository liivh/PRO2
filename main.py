from flask import Flask
from flask import render_template
from flask import request


from libs.daten import speichern

app = Flask("Kursfinder")


@app.route('/')
def start():
    ueberschrifts_text = "Willkommen auf der Kursfinder Website"
    einleitung_text = "Hier kannst du herausfinden, welchen Pfadikurs du als nächstes besuchen kannst"
    return render_template("start.html", app_name="Kursfinder", ueberschrift=ueberschrifts_text, einleitung=einleitung_text)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    if request.method == "POST":
        name = request.form['name_input']
        jahrgang = request.form['jahrgang']
        kurs = request.form['kurs']
        jahr = request.form['jahr']
        antwort = speichern(name, jahrgang, kurs, jahr)
        return 'Gespeicherete Daten: <br>' + str(antwort)
    return render_template('eingabe.html', app_name="Kursfinder - Eingabe")


"""
@app.route('/kursangebot', methods=['POST', 'GET'])
def kursangebot():
    if request.method == 'POST':
        kursangebot = request.form
        print (kursangebot)
        komplettes_kursangebot = read_data_from_json("datenbank.json")
        jahrgang = kursangebot['Jahrgang']
        kurs = kursangebot['Kurs']
        jahr = kursangebot['Jahr']
        liste = []

        for eintrag in komplettes_kursangebot:
            if eintrag["jahrgang"] == range(0,2004) and eintrag["kurs"] == 'Basiskurs':

"""




if __name__ == "__main__":
    app.run(debug=True, port=5000)

