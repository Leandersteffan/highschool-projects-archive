class Artikel:
    def __init__(self, artikelnummer, preis, beschreibung):
        self.artikelnummer = artikelnummer
        self.preis = preis
        self.beschreibung = beschreibung


class Warenkorb:
    def __init__(self):
        self.anzahl_artikel = 0
        self.gesamt_summe = 0
        self.artikel = []

    def artikel_hinzufügen(self, artikelnummer, preis, beschreibung):
        self.artikel.append(Artikel(artikelnummer, preis, beschreibung))

    def gesamt_summe_aktualisieren(self):
        self.gesamt_summe = 0
        for artikel in self.artikel:
            self.gesamt_summe += artikel.preis

    def anzahl_aktualisieren(self):
        self.anzahl_artikel = len(self.artikel)

    def artikel_löschen(self, nummer):
        for artikel in self.artikel:
            if artikel.artikelnummer == nummer:
                self.artikel.remove(artikel)


# Hauptprogramm
w = Warenkorb()
w.artikel_hinzufügen(123, 1.2, "Buch")
w.artikel_hinzufügen(12, 1.5, "Topf")
w.artikel_hinzufügen(56, 2, "Stift")

w.gesamt_summe_aktualisieren()
print(w.gesamt_summe) # 4.7

w.anzahl_aktualisieren()
print(w.anzahl_artikel) # 3

w.artikel_löschen(56)
w.gesamt_summe_aktualisieren()
print(w.gesamt_summe) # 2.7
