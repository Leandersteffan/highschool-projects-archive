from tkinter import *


class Springer:
    def __init__(self):
        self.dimensionen = (5, 8)
        self.offsets = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

        self.zuege = []
        self.position = 0

    def reset(self):
        self.zuege = []
        self.position = 0

    def gueltig(self, position):
        return 0 <= position[0] < self.dimensionen[0] and 0 <= position[1] < self.dimensionen[1] and position not in self.zuege

    def gewicht(self, position):
        gewicht = 0
        for offset in self.offsets:
            neue_position = (position[0] + offset[0], position[1] + offset[1])
            if self.gueltig(neue_position):
                gewicht += 1
        return gewicht

    def springer(self, position):
        self.zuege.append(position)

        if len(self.zuege) == self.dimensionen[0] * self.dimensionen[1]:
            return True

        optionen = []

        for offset in self.offsets:
            neue_position = (position[0] + offset[0], position[1] + offset[1])
            if self.gueltig(neue_position):
                optionen.append((self.gewicht(neue_position), neue_position))

        optionen.sort(key=lambda x: x[0])

        for option in optionen:
            if self.springer(option[1]):
                return True

        self.zuege.remove(position)
        return False

class Gui:
    def __init__(self):
        self.modell = Springer()

        self.dimensionen = (500, 500)

        self.anzeigen = False

        self.tk = Tk()
        self.tk.title('Springer Problem')
        self.tk.geometry(f'{self.dimensionen[0]}x{self.dimensionen[1] + 50}')

        self.canvas = Canvas(self.tk, width=self.dimensionen[0], height=self.dimensionen[1])
        self.canvas.bind('<1>', self.klicken)
        self.canvas.pack()

        self.toggle_button = Button(self.tk, width=self.dimensionen[0], height=50, text='Start', command=self.toggle)
        self.toggle_button.pack()

        # self.reset_button = Button(self.tk, width=self.dimensionen[0], height=50, text='Reset', command=self.reset)
        # self.reset_button.pack()

        self.zeichne_feld()

        self.tk.mainloop()

    def zeichne_feld(self):
        self.canvas.delete('feld')
        a = min(self.dimensionen[0] // self.modell.dimensionen[0], self.dimensionen[1] // self.modell.dimensionen[1])
        b = (self.dimensionen[0] - self.modell.dimensionen[0] * a) // 2
        c = (self.dimensionen[1] - self.modell.dimensionen[1] * a) // 2
        for i in range(self.modell.dimensionen[0]):
            for j in range(self.modell.dimensionen[1]):
                if (i % 2 == 0) == (j % 2 == 0):
                    farbe = 'black'
                else:
                    farbe = 'white'
                self.canvas.create_rectangle(i * a + b, j * a + c, i * a + a + b, j * a + a + c, fill=farbe, tags='feld')

    def zeichne_zug(self, zug):
        self.canvas.delete('figur')
        a = min(self.dimensionen[0] // self.modell.dimensionen[0], self.dimensionen[1] // self.modell.dimensionen[1])
        b = (self.dimensionen[0] - self.modell.dimensionen[0] * a) // 2
        c = (self.dimensionen[1] - self.modell.dimensionen[1] * a) // 2
        self.canvas.create_rectangle(zug[0] * a + b, zug[1] * a + c, zug[0] * a + a + b, zug[1] * a + a + c, fill='green', tags='zug')
        self.canvas.create_text(zug[0] * a + a // 2 + b, zug[1] * a + a // 2 + c, text='♞', font=('MS Comic Sans', a // 2), tags='figur')

    def reset(self):
        self.modell.reset()
        self.canvas.delete('figur')
        self.canvas.delete('zug')

    def toggle(self):
        self.anzeigen = not self.anzeigen
        if self.anzeigen:
            if len(self.modell.zuege) == 0:
                self.toggle_button.config(text='Stop')
                self.modell.springer((0, 0))
                self.weiter()
            else:
                if self.modell.springer(self.modell.zuege[-1]):
                    self.toggle_button.config(text='Stop')
                    self.weiter()
                else:
                    print('keine lösung gefunden')
        else:
            self.toggle_button.config(text='Start')
            self.modell.zuege = self.modell.zuege[:self.modell.position]

    def klicken(self, event):
        a = min(self.dimensionen[0] // self.modell.dimensionen[0], self.dimensionen[1] // self.modell.dimensionen[1])
        b = (self.dimensionen[0] - self.modell.dimensionen[0] * a) // 2
        c = (self.dimensionen[1] - self.modell.dimensionen[1] * a) // 2
        zug = ((event.x - b) // a, (event.y - c) // a)
        if self.modell.gueltig(zug):
            if len(self.modell.zuege) == 0:
                self.modell.zuege.append(zug)
                self.setzen(zug)
            else:
                d = self.modell.zuege[-1]
                if (zug[0] - d[0], zug[1] - d[1]) in self.modell.offsets:
                    self.modell.zuege.append(zug)
                    self.setzen(zug)

    def setzen(self, zug):
        self.zeichne_zug(zug)
        self.modell.position += 1

    def weiter(self):
        if self.anzeigen and self.modell.position < len(self.modell.zuege):
            self.setzen(self.modell.zuege[self.modell.position])
            self.tk.after(500, self.weiter)

gui = Gui()
