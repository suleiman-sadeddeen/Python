#!/usr/bin/python3

# einkaufsliste = [ 'Mich', 'Butter', 'Eier', 'Brot', 'Saft', 'Honig', 'Käse', 'Wurst' ]


produkt0 = {'Name': 'Milch',
           'Preis': 1,
           'Gewicht': 1000,
           'Anzahl': 4}

produkt1 = {'Name': 'Butter',
           'Preis': 1,
           'Gewicht': 250,
           'Anzahl': 2}

produkt2 = {'Name': 'Eier',
           'Preis': 3,
           'Gewicht': 300,
           'Anzahl': 1}

produkt3 = {'Name': 'Brot',
           'Preis': 2,
           'Gewicht': 200,
           'Anzahl': 1}

produkt4 = {'Name': 'Saft',
           'Preis': 1,
           'Gewicht': 1100,
           'Anzahl': 5}

produkt5 = {'Name': 'Honig',
           'Gewicht': 500,
           'Preis': 4,
           'Anzahl': 1}

produkt6 = {'Name': 'Käse',
           'Preis': 2,
           'Gewicht': 250,
           'Anzahl': 2}

produkt7 = {'Name': 'Wurst',
           'Gewicht': 300,
           'Preis': 5,
           'Anzahl': 1}

produkt8 = {'Name': 'Wasser',
           'Gewicht': 1000,
           'Preis': 10,
           'Anzahl': 1}

produkt9 = {'Name': 'Salat',
           'Preis': 1,
           'Gewicht': 200,
           'Anzahl': 2}


einkaufsliste = [ produkt0, produkt1, produkt2, produkt3, produkt4, produkt5, produkt6, produkt7, produkt8, produkt9 ]


geld = input('Wieviel Geld wollen Sie heute ausgeben: ')
geld = int(geld)
traglast = input('Wieviel Gewicht können Sie tragen: ')
traglast = int(traglast)
zaehler = 0
kosten = 0
gesamtgewicht = 0
for nahrungsmittel in einkaufsliste:
    produktkosten = nahrungsmittel['Anzahl'] * nahrungsmittel['Preis']
#    produktkosten =  anzahl[zaehler] * preise[zaehler]
    kosten = kosten + produktkosten
    produktgewicht = nahrungsmittel['Anzahl'] * nahrungsmittel['Gewicht']
    gesamtgewicht = gesamtgewicht + produktgewicht
    zaehler = zaehler + 1 

    if gesamtgewicht > traglast or kosten > geld:
        break
#    if gesamtgewicht > traglast:
#        break  
#    if kosten > geld:
#        break
    print(f'Sie kauften {nahrungsmittel["Anzahl"]} * {nahrungsmittel["Name"]} a`{nahrungsmittel["Preis"]}€ für {produktkosten}€, Gesamtpreis: {kosten}€ {gesamtgewicht}')
#    print(zaehler)
#    print(kosten)
#    print(nahrungsmittel)
    a = input('weiter?')

print('Ende Einkauf')






















#print(name[0:5])
#print(name[6:])
#print(name[2:5])


