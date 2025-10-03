class Ampel(object):
    def __init__(self, anfangszustand):
        self.zustand = anfangszustand

    def setZustand(self, anfangszustand):
        self.zustand = anfangszustand

    def schalten(self):
        if self.zustand == 'rot':
            self.zustand = 'gruen'
        elif self.zustand == 'gruen':
            self.zustand = 'rot'

    def getLampen(self):
        if self.zustand == 'rot':
            lampen = (True, False)
        elif self.zustand == 'gruen':
            lampen = (False, True)
        return lampen