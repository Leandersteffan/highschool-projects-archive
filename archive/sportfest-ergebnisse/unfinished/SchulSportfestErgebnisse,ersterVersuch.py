class Sportfest:
    def __init__(self):
        self.anzahlK=0
        self.anzahlS=0
        self.anzahlL=0
        self.anzahlW=0

    def Kugelstoßen(self):
        self.anzahlK+=1
        print("Ich habe mit der 5kg Kugel einen neuen Rekord von 9,35m aufgestellt.")
        self.spielen()

    def Srint(self):
        self.anzahlS+=1
        print("Ich habe meine ersten 100m unter 13sek geschafft und zwar in 12,7sek.")
        self.spielen()

    def Langlauf(self):
        self.anzahlL+=1
        print("Hier habe ich mich leider nicht verbessert bin aber immerhin die 1000m in 3:08min gelaufen.")
        self.spielen()

    def Weitsprung(self):
        self.anzahlW+=1
        print("Im Weitsprung habe ich eine sehr wichtige Benchmark gebrochen und zwar bin ich glatt 5m geflogen.")
        self.spielen()

    def spiele(self):
        if self.anzahlK=0 and self.anzahlS=0 and self.anzahlL=0 and self.anzahlW=0:
            print("Ich habe mich in allen Disciplinen außer Launglauf verbessert, zur Staffel kommen wir nachher.")
            eingabe=input("Welches Ergebniss möchten sie zuerst sehen? Kugelstoßen, Sprint, Langlauf oder Weitsprung? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=1 and self.anzahlS=0 and self.anzahlL=0 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Sprint, Langlauf oder Weitsprung? ")
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=1 and self.anzahlL=0 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen, Langlauf oder Weitsprung? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=0 and self.anzahlL=1 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen, Sprint oder Weitsprung? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=0 and self.anzahlL=0 and self.anzahlW=1:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen, Sprint oder Langlauf? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=1 and self.anzahlS=1 and self.anzahlL=0 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Langlauf oder Weitsprung? ")
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=1 and self.anzahlS=0 and self.anzahlL=1 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Sprint oder Weitsprung? ")
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=1 and self.anzahlS=0 and self.anzahlL=0 and self.anzahlW=1:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Sprint oder Langlauf? ")
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=1 and self.anzahlL=1 and self.anzahlW=0:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen oder Weitsprung? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Weitsprung" or "Weitsprung"==eingabe:
                self.Weitsprung()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=1 and self.anzahlL=0 and self.anzahlW=1:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen oder Langlauf? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Langlauf" or "Langlauf"==eingabe:
                self.Langlauf()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=0 and self.anzahlS=0 and self.anzahlL=1 and self.anzahlW=1:
            eingabe=input("Welches Ergebniss möchten sie jetzt sehen? Kugelstoßen oder Sprint? ")
            if eingabe=="Kugelstoßen" or "kugelstoßen"==eingabe:
                self.Kugelstoßen()
            if eingabe=="Sprint" or "sprint"==eingabe:
                self.Sprint()
            else:
                print("das ist keine Option")
                self.spielen()
        if self.anzahlK=1 and self.anzahlS=1 and self.anzahlL=1 and self.anzahlW=0:
            self.Weitsprung()
        if self.anzahlK=1 and self.anzahlS=1 and self.anzahlL=0 and self.anzahlW=1:
            self.Langlauf()
        if self.anzahlK=1 and self.anzahlS=0 and self.anzahlL=1 and self.anzahlW=1:
            self.Sprint()
        if self.anzahlK=0 and self.anzahlS=1 and self.anzahlL=1 and self.anzahlW=1:
            self.Kugelstoßen()
        if self.anzahlK=1 and self.anzahlS=1 and self.anzahlL=1 and self.anzahlW=1:
            print("Zum Schluss kommen wir jetzt nochmal zu dem Staffellauf. \n Ich war der Schlussläufer, bisher hat sich unsere Klasse gut geschlagen aber der erste Platz war uneinholbar un der zweite hatte zirka 20m Vorsprung. \n Ich wusste das ich alles für den zweiten Platz geben muss. \n Das habe ich! \n Ich bin so schnell wie ich könnte hinter ihm her und habe Ihn mit einem Meter Abstand im Ziel überholt.")
            eingabe=input("wenn wir jetzt zur Siegerehrung kommen wollen, schreiben sie `ja`: ")
            if eingabe=="ja" or "Ja"==eingabe:
                self.sieg()
            else:
                print("passiert trotzdem")
                self.sieg()

        def sieg(self):
            print("Ich wurde dazu gewählt die Urkunde für den Staffellauf abzuhollen da ich so gut war. \n Aufjeden fall stand ich auf dem zweiten Platz des Podium und habe die Urkunde entgegengenommen. \n Dann kamm die einzel Mehrkampf Siegerehrung. \n Der dritte und zweite Platz wurden als erste aufgerufen und waren mit sehr starken Leuten besetzt, so das ich kurz Zweifel hatte. \n dann war es so Weit, der erste Platz im Mehrkampf der Jungen der Jahrgangsstufe 10 geht mit 1969 Punkten an \n LEANDER STEFFAN.")
            print(" ")
            print("Ich bin sehr Stolz und hatte es mir genau so erträumt, Training zahlt sich aus.")



    def Ergebnisse(self):
        eingabe=input("Möchten sie zu den Ergebnissen von Leander Kommen? Scheriben sie `ja`: )
        if eingabe=="ja" or "Ja"==eingabe:
                      self.spiele()


#Hauptprogramm
Leander=Sportfest()
Leander.spiele()





