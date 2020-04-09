#!/usr/bin/python3

types = { 'name': 'string', 'preis': 'int', 'gewicht': 'int', 'menge': 'int' }

def datei_einlesen(Datei):
    _einkaufsliste = []
    firstline = True
    # einlesen der Daten aus einer CSV Datei
    with open(Datei, 'r') as fh:
        for line in fh.readlines():
            if firstline is True:
                firstline = False
                continue
            items = line.split(',')
            name = items[0][1:]
            name = name[:-1]
            preis = int(items[1])
            gewicht = int(items[2])
            anzahl = items[3]
            anzahl = int(anzahl[:-1])
            nahrungsmittel = {'Name': name, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl}
            _einkaufsliste.append(nahrungsmittel)
    return _einkaufsliste

#einkaufsliste = datei_einlesen('/home/tn/bin/einkaufliste.csv')
einkaufsliste = datei_einlesen('/home/tn/bin/ekliste.csv')


geld = input('Wieviel Geld wollen Sie heute ausgeben: ')
geld = int(geld)
traglast = input('Wieviel Gewicht können Sie tragen: ')
traglast = int(traglast)
zaehler = 0
kosten = 0
gesamtgewicht = 0
# hier wird eingekauft
for nahrungsmittel in einkaufsliste:
    produktkosten = nahrungsmittel['Anzahl'] * nahrungsmittel['Preis']
    kosten = kosten + produktkosten
    produktgewicht = nahrungsmittel['Anzahl'] * nahrungsmittel['Gewicht']
    gesamtgewicht = gesamtgewicht + produktgewicht
    zaehler = zaehler + 1 

    if gesamtgewicht > traglast or kosten > geld:
        break
    print(f'Sie kauften {nahrungsmittel["Anzahl"]} * {nahrungsmittel["Name"]} a`{nahrungsmittel["Preis"]}€ für {produktkosten}€, Gesamtpreis: {kosten}€ {gesamtgewicht}')
    a = input('weiter?')

print('Ende Einkauf')


