class Ampel(object):
    def __init__(self, anfangszustand, anfangszeit):
        self.zustand = anfangszustand
        self.tageszeit = anfangszeit

    def setZustand(self, anfangszustand, anfangszeit):
        self.zustand = anfangszustand
        self.tageszeit = anfangszeit

    def schalten(self):
        if self.tageszeit == 'tag':
            if self.zustand == 'rot':
                self.zustand = 'rotgelb'
            elif self.zustand == 'rotgelb':
                self.zustand = 'gruen'
            elif self.zustand == 'gruen':
                self.zustand = 'gelb'
            elif self.zustand == 'gelb':
                self.zustand = 'rot'
        elif self.tageszeit == 'nacht':
            if self.zustand == 'gelb':
                self.zustand = 'aus'
            elif self.zustand == 'aus':
                self.zustand = 'gelb'
            else:
                self.zustand = 'gelb'

    def tageszeitWechseln(self):
        if self.tageszeit == 'nacht':
            self.tageszeit = 'tag'
        elif self.tageszeit == 'tag':
            self.tageszeit = 'nacht'

    def getLampen(self):
        if self.zustand == 'rot':
            lampen = (True, False, False)
        elif self.zustand == 'rotgelb':
            lampen = (True, True, False)
        elif self.zustand == 'gruen':
            lampen = (False, False, True)
        elif self.zustand == 'gelb':
            lampen = (False, True, False)
        elif self.zustand == 'aus':
            lampen = (False, False, False)
        return lampen