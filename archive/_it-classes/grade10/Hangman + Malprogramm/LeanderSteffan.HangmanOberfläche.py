from tkinter import *


class Hangman(object):
    x = 0

    def __init__(self):
        self.anzahlfversuche=0
        self.hauptfenster = Tk()
        self.hauptfenster.title('Hangman')
        self.hauptfenster.geometry('1080x720')
        self.hauptfenster_hintergrund = "lightblue"
        self.hauptfenster.configure(background=self.hauptfenster_hintergrund)

        # Canvas
        self.malFenster_CNV = Canvas(self.hauptfenster, width=480, height=620, bg="white")
        self.malFenster_CNV.place(x=600, y=100)

        # Button
        self.start_BTN = Button(self.hauptfenster, text="Spiel starten", bg='green', width=10, height=2,
                                command=self.spielst)
        self.start_BTN.place(x=100, y=100)
        self.versuch_BTN = Button(self.hauptfenster, text="Falscher Versuch", bg='orange', width=15, height=2,
                                  command=self.fVersuch)
        self.versuch_BTN.place(x=200, y=100)
        self.ende_BTN = Button(self.hauptfenster, text="Beenden", bg='red', width=10, height=2, command=self.ende)
        self.ende_BTN.place(x=200, y=600)

        # oval
        self.malFenster_CNV.create_oval(150, 470, 450, 770, fill='green', outline='green')

        self.hauptfenster.mainloop()

    def ende(self):
        self.hauptfenster.destroy()

    def fVersuch(self):
        self.anzahlfversuche = self.anzahlfversuche + 1
        if self.anzahlfversuche == 1:
            self.malFenster_CNV.create_line(235, 540, 365, 540, fill='black', width=20)
        if self.anzahlfversuche == 2:
            self.malFenster_CNV.create_line(300, 540, 300, 20, fill='black', width=20)
        if self.anzahlfversuche == 3:
            self.malFenster_CNV.create_line(310, 20, 100, 20, fill='black', width=20)
        if self.anzahlfversuche == 4:
            self.malFenster_CNV.create_line(300,90,230,20, fill='black', width=20)
        if self.anzahlfversuche == 5:
            self.malFenster_CNV.create_line(110,20,110,170, fill='black', width=5)
        if self.anzahlfversuche == 6:
            self.malFenster_CNV.create_line(110,170,110,320, fill='black', width=35)
        if self.anzahlfversuche == 7:
            self.malFenster_CNV.create_line(110,300,180,390, fill='black', width=15)
        if self.anzahlfversuche == 8:
            self.malFenster_CNV.create_line(110,300,40,390, fill='black', width=15)
        if self.anzahlfversuche == 9:
            self.malFenster_CNV.create_line(110,190,180,190, fill='black', width=15)
        if self.anzahlfversuche == 10:
            self.malFenster_CNV.create_line(110,190,40,190, fill='black', width=15)
        if self.anzahlfversuche == 11:
            self.malFenster_CNV.create_oval(85,120,135,170, fill='black', width=20)
            self.hauptfenster_L = Label(self.hauptfenster, width=15, text="Du hast verloren")
            self.hauptfenster_L.place(x=100,y=450)


    def spielst(self):
        falscheVersuche = 0


a = Hangman()
