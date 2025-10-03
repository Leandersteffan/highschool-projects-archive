from tkinter import *
from time import sleep
from PIL import Image,ImageTk


class Gui:
    def __init__(self, x, y, animationsgeschwindigkeit=200):
        self.spielfeld_breite = x
        self.spielfeld_höhe = y
        self.animationsgeschwindikgeit = animationsgeschwindigkeit
        self.springerproblem = Springerproblem(x, y)
        self.springerposition_x = 1
        self.springerposition_y = 0
        self.i = 0
        self.weg = []
        self.colors = [["red", "blue"], ["green", "pink"], ["blue", "red"], ["pink", "green"]]
        self.colornum = -1
        self.feld = [[0 for j in range(self.spielfeld_breite)] for i in range(self.spielfeld_höhe)]

        self.hauptfenster = Tk()
        self.hauptfenster.geometry('1000x840')
        self.hauptfenster.title('Springerproblem')
        self.hauptfenster.configure(bg="#2b2b2b")
        self.img = ImageTk.PhotoImage(Image.open("Springer.jpg"))

        # Canvas
        '''self.canvas=Canvas(self.hauptfenster,height=600,width=600, bg='#1d3227')'''  # original
        self.canvas = Canvas(self.hauptfenster, height=100*self.spielfeld_höhe, width=100*self.spielfeld_breite, bg='lightgreen')  # Canvas color change
        self.canvas.place(x=10, y=10)

        # Lines
        for i in range(1, self.spielfeld_breite):
            self.canvas.create_line(i * 100, 800, i * 100, 0)
        for i in range(1, self.spielfeld_höhe):
            self.canvas.create_line(0, i * 100, 800, i * 100)

        self.explain_L = Label(self.hauptfenster, text="Folgen sie der Schrittfolge:\n1. Startfeld drücken", width=20, bg='#578251')
        self.explain_L.place(x=830, y=50)

        self.start_BTN = Button(self.hauptfenster, text="2. Berechnen", command=lambda: self.lösen_vorschritt([self.springerposition_y, self.springerposition_x]), width=20, height=2, bg='#578251')
        self.start_BTN.place(x=830, y=100)
        self.vis_BTN = Button(self.hauptfenster, text="3. Visualisieren", command=self.visualisieren, width=20, height=2, bg='#578251')
        self.vis_BTN.place(x=830, y=150)
        self.reset_BTN = Button(self.hauptfenster, text="4. daten reseten", command=self.reset, width=20, height=2, bg='#578251')
        self.reset_BTN.place(x=830, y=200)

        self.none_label = Label(self.hauptfenster, text="", fg="red", background="#2b2b2b")
        self.none_label.place(x=830, y=250)

        self.canvas.bind("<Button-1>", func=self.setzen)

        self.hauptfenster.mainloop()

    def setzen(self, event):
        self.none_label.configure(text="")
        if self.colornum < 3:
            self.colornum += 1
        else:
            self.colornum = 0
        self.springerposition_x = int(event.x/100)
        self.springerposition_y = int(event.y/100)
        self.feld_aktualisieren(self.springerproblem.feld, self.springerposition_y, self.springerposition_x)

    def reset(self):
        self.springerposition_x = 1
        self.springerposition_y = 0
        self.i = 0
        self.weg = []
        self.feld = [[0 for j in range(self.spielfeld_breite)] for i in range(self.spielfeld_höhe)]

        self.springerproblem.feld = [[0 for j in range(self.spielfeld_höhe)] for i in range(self.spielfeld_breite)]
        self.springerproblem.trys = 0
        self.springerproblem.weg = []
        self.springerproblem.weg_correct = []


    def lösen_vorschritt(self, coord):
        self.weg = self.springerproblem.lösen(coord)
        if not self.weg:
            self.none_label.configure(text="Keine Lösung")

    def feld_aktualisieren(self, feld, sp_x, sp_y): # jeden Zug und Feld malen
        for i in range(len(feld)):
            for j in range(len(feld[i])):
                if feld[i][j] == 1:
                    self.canvas.create_rectangle(j * 100, i * 100, j * 100 + 100, i * 100 + 100, fill=self.colors[self.colornum][0])
                    self.canvas.create_image(j * 100 + 20, i * 100 + 10, anchor=NW, image=self.img)
        self.canvas.create_rectangle(sp_y * 100, sp_x * 100, sp_y * 100 + 100, sp_x * 100 + 100, fill=self.colors[self.colornum][1])
        self.canvas.create_image(sp_y * 100 + 20, sp_x * 100 + 10, anchor=NW, image=self.img)

    def visualisieren(self):        # richtigen Weg visualisieren
        self.i += 1
        self.feld[self.weg[self.i][0]][self.weg[self.i][1]] = 1
        self.feld_aktualisieren(self.feld, self.weg[self.i][0], self.weg[self.i][1])
        if self.i < (self.spielfeld_breite * self.spielfeld_höhe) - 1:
            self.canvas.after(self.animationsgeschwindikgeit, self.visualisieren)

class Springerproblem:
    def __init__(self, x, y):
        self.spielfeld_breite = x
        self.spielfeld_höhe = y
        self.feld = [[0 for j in range(self.spielfeld_höhe)] for i in range(self.spielfeld_breite)]
        #self.feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        """self.feld = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]"""
        """self.feld = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]"""
        """self.feld = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]"""
        """self.feld = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]"""
        self.trys = 0
        self.weg = []
        self.weg_correct = []

    def lösen(self, coord): #coord == [x, y]
        self.trys += 1      # mitlaufende Variablen
        self.weg.append(coord)
        self.feld[coord[1]][coord[0]] += 1
        if self.check():  # Abbruchkriterium
            self.weg_correct.append(self.weg)
            return self.weg
        else:
            möglichkeiten = self.heuristic_sort_moves(coord)    # Alternativen erstellen
            for möglichkeit in möglichkeiten:                   # Alternativen durchgehen
                if self.legal_move(möglichkeit):                # schauen ob funktioniert
                    self.lösen(möglichkeit)                     # Lösungsmenge verkleinern
            if not self.check():    # Abbruchkriterium, letzten rückgängig
                self.feld[self.weg[-1][1]][self.weg[-1][0]] -= 1
                self.weg.pop(-1)
                return None
        return self.weg     # Weg den Rekursivenaufstieg hochgeben

    def check(self):        # wird geschaut ob Feld beendet (Springer war überall)
        for i in range(len(self.feld)):
            for j in range(len(self.feld[i])):
                if self.feld[i][j] < 1:
                    return False
        return True

    def mögliche_züge(self, coord):
        möglichkeiten = [[coord[0] + 2, coord[1] - 1], [coord[0] + 2, coord[1] + 1], [coord[0] + 1, coord[1] - 2], [coord[0] - 1, coord[1] - 2],
                         [coord[0] - 2, coord[1] + 1], [coord[0] - 2, coord[1] - 1], [coord[0] - 1, coord[1] + 2], [coord[0] + 1, coord[1] + 2]]
        x = -1
        while x <= len(möglichkeiten) - 2:
            x += 1
            if not self.legal_move(möglichkeiten[x]):
                möglichkeiten.pop(x)
                x -= 1
        return möglichkeiten

    def heuristic_sort_moves(self, coord):
        possible_moves = self.mögliche_züge(coord)
        sorted_moves = sorted(possible_moves, key=lambda move: len(self.mögliche_züge(move)))
        return sorted_moves

    """def möglichkeiten_ranken(self, möglichkeiten):
        optionen = []
        for möglichkeit in möglichkeiten:
            if self.legal_move(möglichkeit):
                count = 0
                moves = [[möglichkeit[0] + 2, möglichkeit[1] - 1], [möglichkeit[0] + 2, möglichkeit[1] + 1], [möglichkeit[0] + 1, möglichkeit[1] - 2],
                         [möglichkeit[0] - 1, möglichkeit[1] - 2], [möglichkeit[0] - 2, möglichkeit[1] + 1], [möglichkeit[0] - 2, möglichkeit[1] - 1],
                         [möglichkeit[0] - 1, möglichkeit[1] + 2], [möglichkeit[0] + 1, möglichkeit[1] + 2]]
                for move in moves:
                    if self.legal_move(move):
                        count += 1
                optionen.append([count, möglichkeit])
        optionen.sort()
        out = []
        for op in optionen:
            if op[0] > 0:
                out.append(op[1])
        return out"""


    def legal_move(self, coord):    # schauen ob gegebener Zug möglich ist
        if 0 <= coord[0] < len(self.feld[0]):
            if 0 <= coord[1] < len(self.feld):
                if self.feld[coord[1]][coord[0]] == 0:  # schauen ob Feld leer
                    return True
        return False


class Vorfenster:       # Fenster zum einstellen von allem bevor man das Feld bekommt
    def __init__(self):
        self.hauptfenster = Tk()
        self.hauptfenster.geometry('250x180')
        self.hauptfenster.title('Springerproblem Größe festlegen')
        self.hauptfenster.configure(bg="#2b2b2b")

        # scal
        self.x_len_SCL = Scale(self.hauptfenster, from_=3, to=8, orient=HORIZONTAL, label="Feld Breite", background="lightgreen")
        self.x_len_SCL.place(x="10", y="10")
        self.y_len_SCL = Scale(self.hauptfenster, from_=4, to=8, orient=HORIZONTAL, label="Feld Höhe", background="lightgreen")
        self.y_len_SCL.place(x="130", y="10")
        self.x_len_SCL.set(8)
        self.y_len_SCL.set(8)

        self.animation_ent = Entry(self.hauptfenster, background="lightgreen", width=17)
        self.animation_ent.place(x="130", y="95")
        self.animation_ent.setvar()

        self.animation_label = Label(self.hauptfenster, background="lightgreen", text="Animationsge-\nschwindigkeit in ms:\n200ms standard")
        self.animation_label.place(x="10", y="80")

        # Button
        self.start_BTN = Button(self.hauptfenster, text="start", background="lightgreen", command=self.fertig, width=20)
        self.start_BTN.place(x="50", y="140")

        self.hauptfenster.mainloop()

    def fertig(self):
        animationspeed = 200
        x = self.x_len_SCL.get()
        y = self.y_len_SCL.get()
        if self.animation_ent.get():
            animationspeed = int(self.animation_ent.get())
        self.hauptfenster.destroy()
        gui = Gui(x, y, animationspeed)
        test = Vorfenster()

test = Vorfenster()
