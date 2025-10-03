from tkinter import *
from time import sleep


class Gui:
    def __init__(self):
        self.springerproblem = Springerproblem(self)
        self.springerposition_x = 1
        self.springerposition_y = 0
        self.i = 0

        self.hauptfenster = Tk()
        self.hauptfenster.geometry('1000x840')
        self.hauptfenster.title('Springerproblem')
        self.hauptfenster.configure(bg="#2b2b2b")

        # Canvas
        '''self.canvas=Canvas(self.hauptfenster,height=600,width=600, bg='#1d3227')'''  # original
        self.canvas = Canvas(self.hauptfenster, height=800, width=800, bg='lightgreen')  # Canvas color change
        self.canvas.place(x=10, y=10)

        # Lines
        for i in range(1, 8):
            self.canvas.create_line(i * 100, 800, i * 100, 0)
        for i in range(1, 8):
            self.canvas.create_line(0, i * 100, 800, i * 100)

        self.restart_BTN = Button(self.hauptfenster, text="Starten", command=lambda: self.springerproblem.lösenT(self.springerposition_x, self.springerposition_y), width=10, height=2, bg='#578251')
        self.restart_BTN.place(x=830, y=100)
        self.vis_BTN = Button(self.hauptfenster, text="nächsten Visualisieren", command=self.visualisieren, width=10, height=2, bg='#578251')
        self.vis_BTN.place(x=830, y=150)

        self.canvas.bind("<Button-1>", func=self.setzen)

        self.hauptfenster.mainloop()

    def setzen(self, event):
        self.springerposition_x = int(event.x/100)
        self.springerposition_y = int(event.y/100)
        self.feld_aktualisieren(self.springerproblem.feld, self.springerposition_y, self.springerposition_x)

    def feld_aktualisieren(self, feld, sp_x, sp_y):
        for i in range(len(feld)):
            for j in range(len(feld[i])):
                if feld[i][j] == 1:
                    self.canvas.create_rectangle(j * 100, i * 100, j * 100 + 100, i * 100 + 100, fill="blue")
        self.canvas.create_rectangle(sp_y * 100, sp_x * 100, sp_y * 100 + 100, sp_x * 100 + 100, fill="red")

    def visualisieren(self):
        self.i += 1
        feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        feld[self.springerproblem.lösungs_züge[self.i][0]][self.springerproblem.lösungs_züge[self.i][1]] = 1
        self.feld_aktualisieren(feld, self.springerproblem.lösungs_züge[self.i][0], self.springerproblem.lösungs_züge[self.i][1])


class Springerproblem:
    def __init__(self, gui):
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.count = 0
        self.gui = gui
        self.lösungs_züge = []
        self.lösung = []

    def __str__(self):
        for i in range(len(self.feld)):
            print(self.feld[i])
        return ""

    def lösenT(self, springerposition_x, springerposition_y):
        self.lösung = self.lösen(springerposition_x, springerposition_y)
        print(self.lösung)

    def lösen(self, springerposition_x, springerposition_y):
        self.feld[springerposition_y][springerposition_x] += 1
        self.lösungs_züge.append([springerposition_x, springerposition_y])
        self.count += 1
        if not self.check():
            coordinates = self.wohin_springen(springerposition_x, springerposition_y)
            "print(self)"
            for i in range(len(coordinates)):
                if self.möglicher_zug(coordinates[i][1]):
                    self.lösen(coordinates[i][1][0], coordinates[i][1][1])
                    self.feld[coordinates[i][1][1]][coordinates[i][1][0]] -= 1
                    self.lösungs_züge.pop(-1)
                    return None
        else:
            print(self)
            print("won", self.count, springerposition_x, springerposition_y)
            return self.lösungs_züge

    def check(self):
        for i in range(len(self.feld)):
            for j in range(len(self.feld[i])):
                if self.feld[i][j] > 1:
                    print("mehr als einmal")
                    return False
                if self.feld[i][j] < 1:
                    return False
        return True

    def wohin_springen(self, sp_x, sp_y):
        möglichkeiten = [[sp_x + 2, sp_y - 1], [sp_x + 2, sp_y + 1], [sp_x + 1, sp_y - 2], [sp_x - 1, sp_y - 2], [sp_x - 2, sp_y + 1], [sp_x - 2, sp_y - 1], [sp_x - 1, sp_y + 2], [sp_x + 1, sp_y + 2]]
        best_option = []
        for i in range(len(möglichkeiten)):
            erstestelle = self.möglichkeit_zählen(möglichkeiten[i])
            zweitestelle = möglichkeiten[i]
            best_option.append([erstestelle, zweitestelle])
        best_option.sort()
        return best_option

    def möglichkeit_zählen(self, möglichkeit):
        möglichkeits_feld_x = möglichkeit[0]
        möglichkeits_feld_y = möglichkeit[1]
        möglichkeiten = [[möglichkeits_feld_x + 2, möglichkeits_feld_y - 1], [möglichkeits_feld_x + 2, möglichkeits_feld_y + 1], [möglichkeits_feld_x + 1, möglichkeits_feld_y - 2], [möglichkeits_feld_x - 1, möglichkeits_feld_y - 2], [möglichkeits_feld_x - 2, möglichkeits_feld_y + 1], [möglichkeits_feld_x - 2, möglichkeits_feld_y - 1], [möglichkeits_feld_x - 1, möglichkeits_feld_y + 2], [möglichkeits_feld_x + 1, möglichkeits_feld_y + 2]]
        count = 0
        for i in range(len(möglichkeiten)):
            if self.möglicher_zug(möglichkeiten[i]):
                count += 1
        return count

    def möglicher_zug(self, cords):
        if 0 <= cords[0] < len(self.feld[0]):
            if 0 <= cords[1] < len(self.feld):
                if self.feld[cords[1]][cords[0]] == 0:
                    return True
        return False


test = Gui()
"test.lösen(7, 0)"
