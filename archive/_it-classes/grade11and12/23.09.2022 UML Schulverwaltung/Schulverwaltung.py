class Schulverwaltung:
    def __init__(self, schulname):
        self.name = schulname
        self.schüler = []
        self.lehrer = []
        self.klassen = []
        self.kurse = []
        self.räume = []

class Schüler:
    def __init__(self, name, vorname, geburtsdatum, adresse_o, vertrauenslehrer_o="keiner"):
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.adresse_o = adresse_o
        self.noten_ol = []         # list of Prüfung objects
        self.vertrauenslehrer_o = vertrauenslehrer_o

class Lehrer:
    def __init__(self, name, vorname, geburtsdatum, adresse_o, erstfach, zweitfach):
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.adresse_o = adresse_o
        self.erstfach = erstfach
        self.zweitfach = zweitfach

class Klassen:
    def __init__(self):
        pass

class Räume:
    def __init__(self, raumnummer, schülerplatzanzahl, typ='normal'):
        self.raumnummer = raumnummer
        self.typ = typ
        self.schülerplatzanzahl = schülerplatzanzahl

class Kurse:
    def __init__(self, schüler_ol, lehrer_o, raum_o):
        self.schüler_ol = schüler_ol
        self.lehrer_o = lehrer_o
        self.raum_o = raum_o
        self.teilnehmeranzahl = len(schüler_ol)

class Adresse:
    def __init__(self, strasse, hausnummer, telefonnummer):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.telefonnummer = telefonnummer

class Prüfung:
    def __init__(self, schüler_o, kurs_o, note_o):
        self.schüler_o = schüler_o
        self.kurs_o = kurs_o
        self.note_o = note_o

