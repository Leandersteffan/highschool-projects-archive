from tkinter import *
from eigenesFeldErstellen import *
from validSudoku import *


class Main:
    def __init__(self):
        self.hauptfenster = Tk()
        self.hauptfenster.title("Löse ein Feld")
        self.hauptfenster.geometry("1200x800")
        self.hauptfenster.configure(background="lightgreen")
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Canvas malen
        self.sudoku_Main_cnv = Canvas(self.hauptfenster, background="white", width="600", height="600")
        self.sudoku_Main_cnv.place(x=40, y=40)
        buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1, 9):
            self.sudoku_Main_cnv.create_line(67 * i, 0, 67 * i, 600, fill="lightgrey")
            self.sudoku_Main_cnv.create_line(0, 67 * i, 600, 67 * i, fill="lightgrey")
        for i in [1, 2]:
            self.sudoku_Main_cnv.create_line(200 * i, 0, 200 * i, 600, fill="black")
            self.sudoku_Main_cnv.create_line(0, 200 * i, 600, 200 * i, fill="black")
        for i in range(9):
            self.buchstaben_l = Label(self.hauptfenster, text=buchstaben[i], background="lightgreen")
            self.buchstaben_l.place(x=70 + 67 * i, y=10)
            self.zahlen_l = Label(self.hauptfenster, text=zahlen[i], background="lightgreen")
            self.zahlen_l.place(x=10, y=70 + 67 * i)

            # Button
            self.neuesFeld_btn = Button(self.hauptfenster, text="Neues Feld bauen/einspeichern", background="orange", command=self.neuesfeld)
            self.neuesFeld_btn.place(x="700", y="50")
            self.solve_btn = Button(self.hauptfenster, text="Sudoku lösen", background="green", command=self.solve)
            self.solve_btn.place(x="700", y="320")

            self.notvalid_l = Label(self.hauptfenster, text="", background="lightgreen")
            self.notvalid_l.place(x="700", y="360")

            # Feld laden
            self.zuladen_l = Label(self.hauptfenster, text="Dateiname (ohne Dateientyp)", background="lightgreen")
            self.zuladen_l.place(x="700", y="170")
            self.zuladen_e = Entry(self.hauptfenster, width=40)
            self.zuladen_e.place(x="700", y="200")
            self.zuladen_btn = Button(self.hauptfenster, text="Feld laden", background="red", command=self.laden)
            self.zuladen_btn.place(x="700", y="230")

            # zu speichern
            self.speichern_l = Label(self.hauptfenster, text="geben sie den Namen der Datei an (ohne Dateientyp)", background="lightgreen")
            self.speichern_l.place(x="700", y="500")
            self.speichern_e = Entry(self.hauptfenster, width=40)
            self.speichern_e.place(x="700", y="525")
            self.speichern_btn = Button(self.hauptfenster, text="Feld speichern", background="red", command=self.speichern)
            self.speichern_btn.place(x="700", y="550")

        self.hauptfenster.mainloop()
    def neuesfeld(self):
        neuesfeld = Felderstellen()

    def laden(self):
        dateiname = self.zuladen_e.get()
        self.datei = open(f".\Felder\{dateiname}.txt")
        self.feld = self.datei.readlines()
        for i in range(len(self.feld)):
            self.feld[i] = self.feld[i].strip()
            self.feld[i] = self.feld[i].split(' ')
            for j in range(len(self.feld[i])):
                self.feld[i][j] = int(self.feld[i][j])
        self.datei.close()
        self.feldAktualisieren()

    def feldAktualisieren(self):
        for i in range(9):
            for j in range(9):
                self.zahlen_l = Label(self.sudoku_Main_cnv, text=self.feld[i][j], background="white", font="15")
                self.zahlen_l.place(x=67 * j + 20, y=67 * i + 20)

    def findNextCellToFill(self, grid, i, j):
        for x in range(i, 9):
            for y in range(j, 9):
                if grid[x][y] == 0:
                    return x, y
        for x in range(0, 9):
            for y in range(0, 9):
                if grid[x][y] == 0:
                    return x, y
        return -1, -1

    def isValid(self, grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                # finding the top left x,y co-ordinates of the section containing the i,j cell
                secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
                for x in range(secTopX, secTopX + 3):
                    for y in range(secTopY, secTopY + 3):
                        if grid[x][y] == e:
                            return False
                return True
        return False

    def solveSudoku(self, grid, i=0, j=0):
        i, j = self.findNextCellToFill(grid, i, j)
        if i == -1:
            return True
        for e in range(1, 10):
            if self.isValid(grid, i, j, e):
                grid[i][j] = e
                if self.solveSudoku(grid, i, j):
                    return True
                # Undo the current cell for backtracking
                grid[i][j] = 0
        return False

    def solve(self):
        self.notvalid_l.configure(text="", background="lightgreen")
        x = ValidSudoku()
        if not x.isValidSudoku(self.feld):
            self.notvalid_l.configure(text="Dieses Sudoku ist nicht lösbar", background="red")
        else:
            self.solveSudoku(self.feld)
        self.feldAktualisieren()

    def speichern(self):
        dateiname = str(self.speichern_e.get())
        with open(f".//SolvedFelder//{dateiname}.txt", "w+") as f:
            for i in range(9):
                x = ""
                for j in range(9):
                    x = x + " " + str(self.feld[i][j])
                f.write(x)
                f.write("\n")

    """def d_to_dd(self):
        self.dd_feld = []
        for i in range(9):
            self.dd_feld.append([])
            for j in range(9):
                self.dd_feld[i].append([])
                self.dd_feld[i][j] = [self.feld[i][j]]
        for i in range(9):
            for j in range(9):
                if self.dd_feld[i][j][0] == 0:
                    self.dd_feld[i][j].append(0)
                else:
                    self.dd_feld[i][j].append(1)
        return self.dd_feld

    def dd_to_d(self, feld):
        pass

    def solve(self):
        self.feld_dd_original = self.d_to_dd()
        while True:
            for i in range(9):
                for j in range(9):
                    if self.feld_dd_original[i][j][1] == 0:
                        pass"""






start = Main()