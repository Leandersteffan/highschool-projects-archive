from tkinter import *


class Viergewinnt:
    def __init__(self):
        self.feld = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.aktuellerSpieler = 1

    def setzen(self, x):
        spalte = int(x / 75)
        if self.feld[spalte][0] != 0:
            return None, None
        else:
            for i in range(len(self.feld[spalte])):
                if i == 5 or self.feld[spalte][i + 1] != 0:
                    self.feld[spalte][i] = self.aktuellerSpieler
                    return spalte, i

    def checkWin(self, s, z):
        spieler = self.feld[s][z]
        testroutinenliste = [[[s, z + 1], [s, z + 2], [s, z + 3]], [[s - 1, z], [s - 2, z], [s - 3, z]], [[s + 1, z], [s + 2, z], [s + 3, z]], [[s + 1, z + 1], [s + 2, z + 2], [s + 3, z + 3]], [[s - 1, z - 1], [s - 2, z - 2], [s - 3, z - 3]], [[s - 1, z + 1], [s - 2, z + 2], [s - 3, z + 3]], [[s + 1, z - 1], [s + 2, z - 2], [s + 3, z - 3]], [[s + 2, z - 2], [s + 1, z - 1], [s - 1, z + 1]], [[s, z - 2], [s, z - 1], [s, z + 1]], [[s - 2, z - 2], [s - 1, z - 1], [s + 1, z + 1]], [[s - 1, z - 1], [s + 1, z + 1], [s + 2, z + 2]], [[s + 1, z - 1], [s - 1, z + 1], [s - 2, z + 2]], [[s, z - 1], [s, z + 1], [s, z + 2]], [[s + 1, z], [s - 1, z], [s - 2, z]], [[s - 1, z], [s + 1, z], [s + 2, z]]]
        for testroutine in testroutinenliste:
            count = 1
            for test in testroutine:
                try:
                    if self.feld[test[0]][test[1]] == spieler:
                        count += 1
                except IndexError:
                    pass
            if count == 4:
                return True
        return False


class Gui:
    def __init__(self):
        self.model = Viergewinnt()
        self.hauptfenster = Tk()
        self.hauptfenster.geometry('1000x500')
        self.hauptfenster.title('Reversi')
        self.hauptfenster.configure(bg="#2b2b2b")
        self.isWin = False

        # Canvas
        self.canvas = Canvas(self.hauptfenster, height=450, width=525, bg='lightgreen')  # Canvas color change
        self.canvas.place(x=25, y=25)
        self.canvas.bind("<Button-1>", func=self.setzen)
        self.drawCanvas()

        # Labels
        self.spieler_LBL = Label(self.hauptfenster, text='Spieler 1 (schwarz) ist am Zug', bg='#c16c02', font=("Timesnewroman", 15))
        self.spieler_LBL.place(x=650, y=100)
        self.win_LBL = Label(self.hauptfenster, text='', bg='#2b2b2b', fg="red", font=("Timesnewroman", 20))
        self.win_LBL.place(x=630, y=200)

        # Button
        self.restart_BTN = Button(self.hauptfenster, text="neustart", command=self.restart, width=10, height=2, bg='#578251')
        self.restart_BTN.place(x=650, y=300)
        '''self.restart_BTN = Button(self.hauptfenster, text="print", command=self.giveData, width=10, height=2, bg='#578251')
        self.restart_BTN.place(x=650, y=350)'''

        self.hauptfenster.mainloop()

    '''def giveData(self):
        print(f"feld: {self.model.feld}, isWin: {self.isWin}, actSp: {self.model.aktuellerSpieler}")'''

    def setzen(self, event):
        if not self.isWin:
            x = event.x
            s, z = self.model.setzen(x)
            if s != None:
                self.aktualisiere()
                if self.model.checkWin(s, z):
                    self.win_LBL.configure(text=f"Spieler {self.model.aktuellerSpieler} hat gewonnen!")
                    self.isWin = True
                self.spielerwechsel()

    def spielerwechsel(self):
        if self.model.aktuellerSpieler == 1:
            self.model.aktuellerSpieler = 2
            self.spieler_LBL.configure(text='Spieler 2 (weiß) ist am Zug')
        elif self.model.aktuellerSpieler == 2:
            self.model.aktuellerSpieler = 1
            self.spieler_LBL.configure(text='Spieler 1 (schwarz) ist am Zug')

    def aktualisiere(self):
        for s in range(0, 7):
            for z in range(0, 6):
                if self.model.feld[s][z] == 1:
                    self.canvas.create_oval((75)*s,(75)*z, (s*75)+75, (z*75)+75, fill="black")
                elif self.model.feld[s][z] == 2:
                    self.canvas.create_oval((75)*s,(75)*z, (s*75)+75, (z*75)+75, fill='white')

    def restart(self):
        self.model.feld = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.model.aktuellerSpieler = 1
        self.spieler_LBL.configure(text='Spieler 1 (schwarz) ist am Zug')
        self.win_LBL.configure(text="")
        self.drawCanvas()
        self.isWin = False

    def drawCanvas(self):
        self.canvas.create_rectangle(0, 0, 525, 450, fill='lightgreen', outline='lightgreen')
        # Lines
        for i in range(1, 7):
            self.canvas.create_line(i * 75, 450, i * 75, 0)
        for i in range(1, 6):
            self.canvas.create_line(0, i * 75, 525, i * 75)


# Hauptprogramm
viergewinnt = Gui()
