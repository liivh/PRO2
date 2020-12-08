from flask import Flask
from flask import render_template
from flask import request


from libs.daten import speichern

app = Flask("Kursfinder")

def load_data_json(pfad, standard_wert = []):
    #Quelle: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/ & https://www.programiz.com/python-programming/json
    #das JSONFile wird im read.modus "r" geöffnet, "w" würde das gesamte File löschen.
    #das JSONFile wird in ein Dict umgewandelt, damit mir der Sucheingabe darin gesucht werden kann.
    try:
        with open(pfad, "r") as datei:
            return json.load(datei)
    except Exception:
        return standard_wert

def write_data_to_json(pfad, daten):
    #Quelle: https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
    #dump dient zum in eine datei zum reinschreiben
    with open(pfad, "w") as datei:
        #Quelle: https://pynative.com/python-prettyprint-json-data/
        #ident=4 dient zum JSON File "schöner" anzuzeigen
        json.dump(daten, datei, indent=4)

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



@app.route('/empfehlung', methods=['POST', 'GET'])
def empfehlung():
    if request.method == 'POST':
        empfehlung = request.form['empfehlung']
        print (empfehlung)
        komplettes_kursangebot = load_data_json("kursdaten.json")
        """
        jahrgang = empfehlung['jahrgang']
        kurs = empfehlung['kurs']
        jahr = empfehlung['jahr']
        liste = []
"""
        for eintrag in komplettes_kursangebot:
            if eintrag == "empfehlung":
                """
        return "fortsetzung"
    return render_template('empfehlung.html', app_name="Kursfinder - Kursangebot")
"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)

