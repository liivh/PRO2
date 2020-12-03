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

def laden ():
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    return eintraege
"""
def kursangebot_oeffnen():
    try:
        with open("datenbank.json", "r", encoding="utf-8") as datenbank_kursangebot:
            kursangebot = json.load(datenbank_kursangebot)
    except:
        kursangebot = {}
    return kursangebot

def kursangebot_speichern(kursname_kursangebot_antwort,
                          jahrgang_antwort,
                          gueltigkeit_antwort,
                          voraussetzung_antwort,
                          fortsetzung_antwort):
    kursangebot = kursangebot_oeffnen()

    kursangebot = {
        name_kursangebot_antwort:{
            "kursname": kursname_kursangebot_antwort,
            "jahrgang": jahrgang_antwort,
            "voraussetzung": voraussetzung_antwort,
            "fortsetzung": fortsetzung_antwort,
        }
    }
kursangebot_update(kursangebot)

with open("datenbank.json", "w") as datenbank_kursangebot:
    json.dump(kursangebot, datenbank)

return
    name_kursangebot_antwort, \
    jahrgang_antwort, \
    gueltigkeit_antwort, \
    voraussetzung_antwort, \
    fortsetzung_antwort

"""

