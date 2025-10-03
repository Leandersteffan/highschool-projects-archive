class Schulverwaltung:
    def __init__(self, schulname):
        self.name = schulname
        self.schueler_ol = []
        self.lehrer_ol = []
        self.kurse_ol = []
        self.raeume_ol = []

    def neuerSchueler(self, name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, vertrauenslehrer_o=None):
        self.schueler_ol.append(Schueler(name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, vertrauenslehrer_o))

    def neuerRaum(self, nr, typ, plaetze):
        self.raeume_ol.append(Raum(nr, typ, plaetze))

    def neuerLehrer(self, name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, erstfach, zweitfach):
        self.lehrer_ol.append(Lehrer(name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, erstfach, zweitfach))


class Adresse:
    def __init__(self, strasse, hausnummer, telefonnummer):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.telefonnummer = telefonnummer


class Person:
    def __init__(self, name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a):
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.adresse_o = Adresse(strasse_a, hausnummer_a, telefonnummer_a)


class Schueler(Person):
    def __init__(self, name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, vertrauenslehrer_o=None):
        super().__init__(name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a)
        self.pruefungen_ol = []  # list of Prüfung objects
        self.vertrauenslehrer_o = vertrauenslehrer_o


class Lehrer(Person):
    def __init__(self, name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a, erstfach, zweitfach):
        super().__init__(name, vorname, geburtsdatum, strasse_a, hausnummer_a, telefonnummer_a)
        self.erstfach = erstfach
        self.zweitfach = zweitfach


class Kurs:
    def __init__(self, name, typ, lehrer_o, raum_o):
        self.lehrer_o = lehrer_o
        self.raum_o = raum_o
        self.schueler_ol = []
        self.pruefungen_ol = []  # list of Prüfung objects
        self.name = name
        self.typ = typ

    def einfuegenschueler(self, schueler_o):
        self.schueler_ol.append(schueler_o)

    def schueleranzahl(self):
        anzahl = len(self.schueler_ol)
        pass
        return anzahl


class Pruefung:
    def __init__(self, kurs_o, punkte, schueler_o):
        self.kurs_o = kurs_o
        self.schueler_o = schueler_o
        self.punkte = punkte


class Raum:
    def __init__(self, nr, typ, plaetze):
        self.nr = nr
        self.typ = typ
        self.plaetze = plaetze


# Hauptprogramm
schulverwaltungs_o = Schulverwaltung("Primo-Levi-Gymnasium")

schulverwaltungs_o.neuerSchueler("Steffan", "Leander", 20220403, "Gäblerstrasse", 3, "017683050697", "Tewes")
# print(schulverwaltungs_o.schueler_ol[0].vertrauenslehrer_o)

schulverwaltungs_o.neuerRaum(202, "Computerraum", 15)
#print(schulverwaltungs_o.raeume_ol[0].nr)

schulverwaltungs_o.neuerLehrer("Einstein", "Albert", 18790314, "Mercer St.", 112, "02265-9929 0", "Physik", "Quantenmechanik")
print(schulverwaltungs_o.lehrer_ol[0].adresse_o.telefonnummer)