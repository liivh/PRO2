import json

from collections import Counter

# Funktion zum Speichern des Eintrags
def speichern(email, name, jahrgang, kurs, jahr):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = {}

    eintraege[email] = {"name": name, "jahrgang": jahrgang, "kurs": kurs, "jahr": jahr}


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


def get_recs(email):
    kurse = laden_kursdaten()
    abfrage = laden_datenbank()[email]
    abfrage_kurs = abfrage["kurs"]
    abfrage_jahrgang = int(abfrage["jahrgang"])

    recs_list = []

    if abfrage_kurs == "keiner":
        recs_list.append("Futurakurs")
    elif abfrage_kurs == "Futurakurs":
       recs_list.append("Basiskurs")
    else:
        for kurs in kurse:
            if kurs["voraussetzung"] == abfrage_kurs and int(kurs["jahrgang"]) >= abfrage_jahrgang:
                recs_list.append(kurs["name"])
        recs_list.append("Sicherheitsmodul")

    return recs_list

def alle_kurse():
    kurse = laden_datenbank()
    kurs_liste = []
    for kurs in kurse.values():
        kurs_liste.append(kurs["kurs"])
    ergebnis=Counter(kurs_liste)
    return ergebnis



def kurs_speichern(name, jahrgang, gueltigkeit, voraussetzung, fortsetzung):
    kurse = laden_kursdaten()
    neuer_kurs = {
    "name": name,
    "jahrgang": jahrgang,
    "gueltigkeit": gueltigkeit,
    "voraussetzung": voraussetzung,
    "fortsetzung": fortsetzung
  }
    kurse.append(neuer_kurs)
    with open("kursdaten.json", "w") as datenbank_kursdaten:
        json.dump(kurse, datenbank_kursdaten, indent=4)


def check_email(email):
    teilnehmende = laden_datenbank()
    if email not in teilnehmende.keys():
        return False
    else:
        pass
