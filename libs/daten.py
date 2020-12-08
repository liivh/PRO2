import json


# Funktion zum Speichern des Eintrags
def speichern(name, jahrgang, kurs, jahr):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    new_entry = {"Name": name, "Jahrgang": jahrgang, "Kurs": kurs, "Jahr": jahr}
    eintraege.append(new_entry)


    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank, indent=4)
    return "Daten gespeichert"

def laden_datenbank():
    try:
        with open("datenbank.json", "r") as datenbank_datenbank:
            eintraege_datenbank = json.load(datenbank_datenbank)
    except:
        eintraege_datenbank = {}

    return eintraege_datenbank

def laden_kursdaten():
    try:
        with open("kursdaten.json", "r") as datenbank_kursdaten:
            eintraege_kursdaten = json.load(datenbank_kursdaten)
    except:
        eintraege_kursdaten = {}
    return eintraege_kursdaten

def filter():
    eintraege_datenbank = laden()
    eintraege_kursdaten = laden()



