class Ampel(object):
    def __init__(self, anfangszustand):
        self.zustand = anfangszustand

    def schalten(self):
        if self.zustand == 'rot':
            self.zustand = 'rotgelb'
        elif self.zustand == 'rotgelb':
            self.zustand = 'gruen'
        elif self.zustand == 'gruen':
            self.zustnd = 'gelb'
        elif self.zustand == 'gelb':
            self.zustand = 'rot'

    def getLampen(self):
        if self.zustand == 'rot':
            lampen = (True, False, False)
        elif self.zustand == 'rotgelb':
            lampen = (True, True, False)
        elif self.zustand == 'gruen':
            lampen = (False, False, True)
        elif self.zustand == 'gelb':
            lampen = (False, True, False)
        return lampen

    def getZustand(self):
        return self.zustand

    def setZustand(self, z):
        self.zustand = z
