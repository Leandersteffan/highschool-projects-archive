from tkinter import *
from time import sleep


class Gui:
    def __init__(self):
        self.hauptfenster = Tk()
        self.hauptfenster.geometry('840x840')
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

        self.hauptfenster.mainloop()

    def feld_aktualisieren(self, feld, sp_x, sp_y):
        for i in range(len(feld)):
            for j in range(len(feld[i])):
                if feld[i][j] == 1:
                    self.canvas.create_rectangle(i * 100, j * 100, i * 100 + 100, j * 100 + 100, fill="blue")
        self.canvas.create_rectangle(sp_y * 100, sp_x * 100, sp_y * 100 + 100, sp_x * 100 + 100, fill="blue")




class Springerproblem:
    def __init__(self):
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.count = 0
        self.gui = Gui()

    def __str__(self):
        for i in range(len(self.feld)):
            print(self.feld[i])
        return ""

    def lösen(self, springerposition_x, springerposition_y):
        self.feld[springerposition_y][springerposition_x] += 1
        self.count += 1
        self.gui.feld_aktualisieren(self.feld, springerposition_x, springerposition_y)
        sleep(0.2)
        if not self.check():
            coordinates = self.wohin_springen(springerposition_x, springerposition_y)
            print(self)
            for i in range(len(coordinates)):
                if self.möglicher_zug(coordinates[i][1]):
                    self.lösen(coordinates[i][1][0], coordinates[i][1][1])
        else:
            print(self)
            print("won", self.count, springerposition_x, springerposition_y)

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
        möglichkeits_feld_x = möglichkeit[1]
        möglichkeits_feld_y = möglichkeit[0]
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


test = Springerproblem()
"test.lösen(7, 0)"
