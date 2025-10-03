class Polyeder:
    def __init__(self, flaechenliste):
        self.flaechen = flaechenliste # Datentyp Liste von Flaechen

class Flaechen:
    def __init__(self, kantenlist):
        self.kanten = kantenlist # Datentyp Liste von Kanten

class Kanten:
    def __init__(self, punktelist):
        self.KantenID = punktelist # Datentyp Liste von Punkten

class Punkte:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Hauptprogramm
punkt1 = Punkte(0, 0, 4)
punkt2 = Punkte(5, 0, 0)
punkt3 = Punkte(0, 3, 0)
punkt4 = Punkte(0, 0, 0)

kante1 = Kanten([punkt1, punkt2])
kante2 = Kanten([punkt1, punkt3])
kante3 = Kanten([punkt2, punkt3])
kante4 = Kanten([punkt1, punkt4])
kante5 = Kanten([punkt2, punkt4])
kante6 = Kanten([punkt3, punkt4])

flaeche1 = Flaechen([kante1, kante2, kante3])
flaeche2 = Flaechen([kante1, kante4, kante5])
flaeche3 = Flaechen([kante2, kante4, kante6])
flaeche4 = Flaechen([kante3, kante5, kante6])

tetraeder = Polyeder([flaeche1, flaeche2, flaeche3, flaeche4]) # Containerklasse
