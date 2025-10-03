from tkinter import *
from time import sleep


class Gui:
    def __init__(self):
        self.springerproblem = Springerproblem()
        self.springerposition_x = 1
        self.springerposition_y = 0
        self.i = 0
        self.weg = []
        self.colors = [["red", "blue"], ["blue", "green"], ["green", "pink"], ["pink", "red"]]
        self.colornum = -1
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

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

        self.restart_BTN = Button(self.hauptfenster, text="Starten", command=lambda: self.lösen_vorschritt([self.springerposition_y, self.springerposition_x]), width=10, height=2, bg='#578251')
        self.restart_BTN.place(x=830, y=100)
        self.vis_BTN = Button(self.hauptfenster, text="nächsten Visualisieren", command=self.visualisieren, width=10, height=2, bg='#578251')
        self.vis_BTN.place(x=830, y=150)

        self.canvas.bind("<Button-1>", func=self.setzen)

        self.hauptfenster.mainloop()

    def setzen(self, event):
        self.springerposition_x = int(event.x/100)
        self.springerposition_y = int(event.y/100)
        self.feld_aktualisieren(self.springerproblem.feld, self.springerposition_y, self.springerposition_x)

    def lösen_vorschritt(self, coord):
        self.weg = self.springerproblem.lösen(coord)
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]]
        self.i = 0
        if self.colornum < 3:
            self.colornum += 1
        else:
            self.colornum = 0
        print("self.weg", self.weg, "\nself.i", self.i, "\nself.feld", self.feld, "\nself.springerproblem.feld",
              self.springerproblem.feld, "\nself.springerproblem.weg", self.springerproblem.weg)

    def feld_aktualisieren(self, feld, sp_x, sp_y):
        for i in range(len(feld)):
            for j in range(len(feld[i])):
                if feld[i][j] == 1:
                    self.canvas.create_rectangle(j * 100, i * 100, j * 100 + 100, i * 100 + 100, fill=self.colors[self.colornum][0])
        self.canvas.create_rectangle(sp_y * 100, sp_x * 100, sp_y * 100 + 100, sp_x * 100 + 100, fill=self.colors[self.colornum][1])

    def visualisieren(self):
        self.i += 1
        self.feld[self.weg[self.i][0]][self.weg[self.i][1]] = 1
        self.feld_aktualisieren(self.feld, self.weg[self.i][0], self.weg[self.i][1])
        if self.i < 63:
            self.canvas.after(100, self.visualisieren)

class Springerproblem:
    def __init__(self):
        self.feld = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
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
        self.trys += 1
        self.weg.append(coord)
        self.feld[coord[1]][coord[0]] += 1
        if self.check():  # Abbruchkriterium
            self.weg_correct.append(self.weg)
            return self.weg
        else:
            möglichkeiten = self.heuristic_sort_moves(coord)
            for möglichkeit in möglichkeiten:
                if self.legal_move(möglichkeit):
                    "self.imprint(weg)"
                    self.lösen(möglichkeit)
            if not self.check():    #Abbruchkriterium
                self.feld[self.weg[-1][1]][self.weg[-1][0]] -= 1
                self.weg.pop(-1)     #letzten rückgängig
                return None
        return self.weg

    def check(self):
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


    def legal_move(self, coord):
        if 0 <= coord[0] < len(self.feld[0]):
            if 0 <= coord[1] < len(self.feld):
                if self.feld[coord[1]][coord[0]] == 0:
                    return True
        return False

    def imprint(self, weg):
        for row in self.feld:
            out = ""
            for ele in row:
                if ele == 1:
                    out += "# "
                else:
                    out += "- "
            print(out)
        print(weg[-5:], len(weg))
        x = input(":")


gui = Gui()
test = Springerproblem()
test.lösen([0, 0])
n = test.weg
print(len(n), test.trys, n, test.weg_correct)
#print(test.möglichkeiten_ranken([[3, 1], [3, 3], [2, 0], [0, 0], [-1, 3], [-1, 1], [0, 4], [2, 4]]))

