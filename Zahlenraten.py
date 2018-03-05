# zahlenraten

import random
zufallszahl = random.randint(1,2)
anzahlDerVersuche = 0


title = "Willkommen beim Zahlenraten!"
text = "bitte geben sie eine zahl ein die zahl ist zwischen 1-100"
eingabeText = "DeinVersuch: "

print(title)
print(text)

fertig = False


while fertig == False:
    zahl = int(input(eingabeText))
    anzahlDerVersuche = anzahlDerVersuche + 1
    if(zahl == zufallszahl):
        print("gewonnen")
        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte Zahl ist größer")
    else:
        (zahl > zufallszahl)
        print("die gesuchte Zahl ist kleiner")



print("super du hast nur ", anzahlDerVersuche, " benötigt")




print("ende")
