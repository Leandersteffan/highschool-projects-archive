from tkinter import *
from validSudoku import ValidSudoku

class Gui:
    def __init__(self, object):
        self.felderstellen = object
        self.hauptfenster = Tk()
        self.hauptfenster.title("erstelle dein Feld")
        self.hauptfenster.geometry("1000x700")
        self.hauptfenster.configure(background="lightgreen")
        self.aktuellesFeld = 0
        self.feld = []

        # Canvas malen
        self.sudoku_cnv = Canvas(self.hauptfenster, background="white", width="600", height="600")
        self.sudoku_cnv.place(x=40, y=40)
        buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1, 9):
            self.sudoku_cnv.create_line(67 * i, 0, 67 * i, 600, fill="lightgrey")
            self.sudoku_cnv.create_line(0, 67 * i, 600, 67 * i, fill="lightgrey")
        for i in [1, 2]:
            self.sudoku_cnv.create_line(200 * i, 0, 200 * i, 600, fill="black")
            self.sudoku_cnv.create_line(0, 200 * i, 600, 200 * i, fill="black")
        for i in range(9):
            self.buchstaben_l = Label(self.hauptfenster, text=buchstaben[i], background="lightgreen")
            self.buchstaben_l.place(x=70 + 67 * i, y=10)
            self.zahlen_l = Label(self.hauptfenster, text=zahlen[i], background="lightgreen")
            self.zahlen_l.place(x=10, y=70 + 67 * i)

        # Button
        self.beginne_Erstellung_btn = Button(self.hauptfenster, text="Erstellung beginnen", command=self.reset_start)
        self.beginne_Erstellung_btn.place(x=800, y=100)

        # zu speichern
        self.speichern_l = Label(self.hauptfenster, text="geben sie den Namen der Datei an (ohne Dateientyp)", background="lightgreen")
        self.speichern_l.place(x="700", y="500")
        self.speichern_e = Entry(self.hauptfenster, width=40)
        self.speichern_e.place(x="700", y="525")
        self.speichern_btn = Button(self.hauptfenster, text="Feld speichern", background="red", command=self.speichern)
        self.speichern_btn.place(x="700", y="550")


        self.hauptfenster.mainloop()
    def reset_start(self):
        self.aktuellesFeld = 0
        self.feld = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.eingabefelder()

    def eingabefelder(self):
        self.aktuellesFeld += 1
        anzuzeigen, listcoord = self.felderstellen.aktuellesFeld(self.aktuellesFeld)
        self.eingabe_l = Label(self.hauptfenster, text=f"bestimmen sie Wert für Feld ({anzuzeigen[0]} {anzuzeigen[1]})", background="lightgreen")
        self.eingabe_l.place(x=750, y=200)
        self.eingabe_s = Scale(self.hauptfenster, from_=0, to=9, orient=HORIZONTAL, background="lightgreen")
        self.eingabe_s.place(x=750, y=250)
        def abspeichern():
            self.feld[listcoord[0]][listcoord[1]] = self.eingabe_s.get()
            self.feldAktualisieren()
            self.eingabefelder()
        self.beginne_Erstellung_btn = Button(self.hauptfenster, text="nächstes Feld", command=abspeichern)
        self.beginne_Erstellung_btn.place(x=870, y=250)

    def feldAktualisieren(self):
        for i in range(9):
            for j in range(9):
                self.zahlen_l = Label(self.sudoku_cnv, text=self.feld[i][j], background="white", font="15")
                self.zahlen_l.place(x=67 * j + 20, y=67 * i + 20)

    def speichern(self):
        dateiname = str(self.speichern_e.get())
        with open(f".//Felder//{dateiname}.txt", "w+") as f:
            for i in range(9):
                x = ""
                for j in range(9):
                    x = x + " " + str(self.feld[i][j])
                f.write(x)
                f.write("\n")
        self.hauptfenster.destroy()





class Felderstellen:
    def __init__(self):
        self.gui = Gui(self)

    def aktuellesFeld(self, feldzahl):
        y = int(feldzahl / 9.000001)
        x = (feldzahl % 9) - 1
        buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        return (buchstaben[x], y + 1), (y, x)

    def eingabefelderAuswertung(self):
        pass
