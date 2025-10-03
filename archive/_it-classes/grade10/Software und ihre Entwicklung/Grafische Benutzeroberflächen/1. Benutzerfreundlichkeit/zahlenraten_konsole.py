from random import randint
genug = False
while not genug:
    print()
    antwort = input('Noch eine Zahl raten? (j/n): ')
    if antwort == 'n':
        genug = True
    elif antwort == 'j':
        print('WÃ¤hle den Zahlenbereich.')
        print('1..100: (A)')
        print('1..500: (B)')
        print('1..1000: (C)')
        wahl = input('Wahl (A/B/C): ')
        while not wahl in ['A', 'B', 'C']:
            wahl = input('Wahl (A/B/C): ')
        if wahl == 'A':
            obergrenze = 100
        elif wahl == 'B':
            obergrenze = 500
        elif wahl == 'C':
            obergrenze = 1000
        ratezahl = randint(1, obergrenze)
        anzahlRateversuche = 0
        gefunden = False
        while not gefunden:
            anzahlRateversuche = anzahlRateversuche + 1
            eingabeZahl = input(str(anzahlRateversuche) + '. Rateversuch: ')
            try:
                zahl = int(eingabeZahl)
                if zahl < 1 or zahl > obergrenze:
                    print('Die Zahl liegt nicht im vorgegebenen Bereich.')
                else:
                    if zahl < ratezahl:
                        print('zu klein')
                    elif zahl > ratezahl:
                        print('zu groÃŸ')
                    else:
                        print('Treffer')
                        gefunden = True
            except:
                print('Keine sinnvolle Eingabe!')
