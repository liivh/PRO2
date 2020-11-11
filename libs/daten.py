import json


# Funktion zum Speichern des Eintrags
def speichern(nummer, jahrgang, kurs, jahr):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    new_entry = {"Name": nummer, "Jahrgang": jahrgang, "Kurs": kurs, "Jahr": jahr}
    eintraege.append(new_entry)


    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank, indent=4)
    return "Daten gespeichert"



"""
import json


# testing
def speichern(nummer, jahrgang, kurs, jahr):
    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = {}

    eintraege[nummer] = {"Jahrgang": jahrgang, "Kurs": kurs, "Jahr": jahr}


    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank, indent=4)
    return "Daten gespeichert"


# end of testing
"""