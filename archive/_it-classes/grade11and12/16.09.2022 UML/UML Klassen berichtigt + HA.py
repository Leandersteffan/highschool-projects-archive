class Polyeder:
    def __init__(self, polyID, flaechenliste):
        self.polyID = polyID
        self.flaechen = flaechenliste # Datentyp Liste von Flaechen
        '''komposition
        self.flaechen = [Flaechen([kante1, kante2, kante3]), Flaechen([kante1, kante4, kante5]), Flaechen([kante2, kante4, kante6]), Flaechen([kante3, kante5, kante6])]'''
    def ausgabeFlaechen(self):
        return self.flaechen

class Flaechen:
    def __init__(self, kantenlist):
        self.kanten = kantenlist # Datentyp Liste von Kanten

class Kanten:
    def __init__(self, punktelist):
        self.punkte = punktelist # Datentyp Liste von Punkten
#        self.punkt1 = punktelist[0]
#        self.punkt2 = punktelist[1]

class Punkte:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def get_x(tetraeder):
    had_punkte = []
    alle_punkte = []
    for flaechen in tetraeder.flaechen:
        for kanten in flaechen.kanten:
            for punkte in kanten.punkte:
                if not punkte in had_punkte:
                    alle_punkte.append(f"(x = {punkte.x}, y = {punkte.y}, z = {punkte.z})")
                    had_punkte.append(punkte)
    return alle_punkte


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

tetraeder = Polyeder("tetraeder", [flaeche1, flaeche2, flaeche3, flaeche4]) # Containerklasse

print(get_x(tetraeder))