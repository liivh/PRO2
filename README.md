# Projekt Livia Hebeisen

Diese Projekt ist im Rahmen der Projektarbeit des Moduls "Programmierung 2" des Studienganges "Digital Business Management" der Fachhochschule Graubünden entstanden. 

__Name Github:__ liivh <br>
__Webapplikation:__ Kursfinder <br>


## Ausgangslage:
Als Pfadfinder hat man die Möglichkeit verschiedene Ausbildungskurse zu machen. Sobald man ein gewisses Alter erreicht hat, kann man J+S Ausbildungskurse für Lagersport / Trekking besuchen. Nach dem Basiskurs können verschiedenste Aus- und Weiterbildungen gemacht werden. Dabei ist es für viele immer sehr verwirrend, welcher Kurs wann und mit welchen Vorbedingungen besucht werden kann. Da dies Abhängig vom Alter, Ausbildungskurs und Datum des besuchten Kurs abhängt.

## Funktion / Projektidee
Meine Projektidee soll diesem Problem entgegen wirken. Der/Die Pfadfinder/in kann sein/ihr Alter, besuchte Kurse und Jahr der Kurse in das Tool eingeben und es wird eine Liste mit möglichen Kursen ausgegeben. 


## Installationen
Damit der Kursfinder funktioniert, müssen folgende Module installiert werden:
- Flask (Flask, render_template, request, url_for)
- Collections (Counter) zum die Kurse zu zählen
- Plotly (plotly.express as px) für die Darstellung des Diagramms
- Pandas, damit Plotly ausgeführt werden kann

## Ablauf

### Start
Auf der Startseite wird der Nutzer begrüsst und kommt anhand des Links "Eingabeformular" oder durck Klick auf das Register "Eingabe" auf die Eingabeseite.

### Eingabe
Ist der Nutzer noch nicht registriert, gibt er seine Daten in das linke Formular ein. Folgende Angaben werden benötigt:
- E-Mail Adresse
- Pfadiname
- Jahrgang
- Letzter Kurs

Mit dem Button "Eingabe speichern" können die Inputs gespeichert werden. Danach werden dem Nutzer die empfohlenen Kurse angezeigt

## Neuer Kurs
Im Register "Neuer Kurs" kann der Nutzer einen neuen Kurs anlegen, welcher in der Datenbank fehlt. 
Dafür müssen folgenden Angaben gemacht werden:
- Kursname
- Benötigter Jahrgang
- Voraussetzung
- Fortsetzung

Mit dem Button "Kurs speichern" wird der Kurs in der Datenbank gespeichert.

## Ausbildungsstand Kanton
Anhand der Grafik im Register "Ausbildungsstand Katon" kann analysiert werden, wie gut die Leitenden im Kanton ausgebildet sind. Daraus lässt sich schliessen, wo noch in der Ausbildung in der Pfadi investiert und Leitende gefördert werden müssen.

## Flussdiagramm
![alt text]
(https://github.com/liivh/PRO2/tree/master/images)

## Funktionen 
### Dateneingabe:
- Persönliche Daten im Eingabeformular, zum Registrieren
- E-Mail Adresse, wenn bereits registriert
- neuer Kurs anlegen


### Datenverarbeitung / Speichern
- Bearbeitung der persönlichen Daten, um eine Empfehlung abgeben zu können

### Datenausgabe:
- Empfehlungen / Nutzerdaten
- Balkendiagramm

## Mögliche Erweiterung
Um den Umfang dieser Projektarbeit nicht zu sprengen, wurden die Gültigkeitsjahre nicht berücksichtigt. Dies ist eine mögliche Erweiterung der Erstellerin, um nach der Projektarbeit ihre Pyhthon Kenntnisse weiter auszubauen. 

