from tkinter import *
import math
'''import sys
sys.setrecursionlimit(10 ** 6)  # maximale Rekursionstiefe erhöhen da sonst bei 1000 stopt'''


class Backend:
    def __init__(self): # alle größen sind sehr ähnlich zu meiner Excel Datei benannt.
        self.mErde = 5.97*1000000000000000000000000
        self.mSat = 1000
        self.gc = 0.00000000006673
        self.rErde = 6371000
        self.deltat = 0.1
        self.t = 0
        self.v0 = 0
        self.r = self.rErde
        self.coord_list = [[0, self.r]] # erster Punkt schon in der Liste
        self.count = 0      # Wird die Rekursion mitzählen und nicht jeden Punkt in die Coord Liste packen
        self.count_limit = 1500000
        self.rundenindikator = 0
        self.r_max = 0
        self.umlaufdauer = 0

        # alles x       # erstmal alle Größen festlegen (viele werden vor der ersten verwendung nochmal verändert)
        self.x = 0
        self.vx = self.v0
        self.ax = 0
        self.fx = 0

        # alles y
        self.y = self.r
        self.vy = 0
        self.ay = 0
        self.fy = 0

    def rechne_coord(self): # erster durchlauf bei dem noch nicht alles berechnet werden muss, da vieles egal welche v0, immer gleich ist
        self.vx = self.v0
        self.f = self.gc * ((self.mSat * self.mErde) / (self.r**2))
        self.anteilfx = -(self.x / self.r)
        self.anteilfy = -(self.y / self.r)
        self.fy = self.f * self.anteilfy
        self.ay = self.fy / self.mSat
        self.count += 1
        self.rechne_coord_rekursion()

    def rechne_coord_rekursion(self):
        while self.count < self.count_limit:
            self.t += self.deltat
            self.x = self.x + (self.vx * self.deltat)
            self.y = self.y + (self.vy * self.deltat)
            self.r = math.sqrt(self.x**2 + self.y**2)
            self.f = self.gc * ((self.mSat * self.mErde) / (self.r ** 2))
            self.anteilfx = -(self.x / self.r)
            self.anteilfy = -(self.y / self.r)
            self.fy = self.f * self.anteilfy
            self.vy = self.vy + (self.ay * self.deltat) # muss vor ay da sonst nicht mehr der alte ay Wert
            self.ay = self.fy / self.mSat
            self.fx = self.f * self.anteilfx
            self.vx = self.vx + (self.ax * self.deltat)  # muss vor ay da sonst nicht mehr der alte ax Wert
            self.ax = self.fx / self.mSat
            self.umlaufdauer = self.t
            if self.r > self.r_max:
                self.r_max = self.r
            if self.r < self.rErde*0.95 and self.x < 0 and self.y < 0:   # Grafisch schön damit man die "Bahn durch die Erde" bis unten links sieht
                break
            if self.rundenindikator == 0 and self.x < 0 and self.y < 0:
                self.rundenindikator = 1
            if self.rundenindikator == 1 and self.x > 0 and self.y > 0:
                break

            self.count += 1
            if self.count % 100 == 0:
                self.coord_list.append([int(self.x), int(self.y)])
                """print(self.count, self.f, self.anteilfx, self.anteilfy, self.r)"""

    def reset(self, deltat):
        self.deltat = deltat
        self.rundenindikator = 0
        self.r_max = 0
        self.umlaufdauer = 0
        self.t = 0
        self.r = self.rErde
        self.coord_list = [[0, self.r]]  # erster Punkt schon in der Liste
        self.count = 0  # Wird die Rekursion mitzählen und nicht jeden Punkt in die Coord Liste packen
        self.count_limit = 15000000
        if self.v0 > 11184:
            self.count_limit = 1500000

        # alles x       # erstmal alle Größen festlegen (viele werden vor der ersten verwendung nochmal verändert)
        self.x = 0
        self.vx = self.v0
        self.ax = 0
        self.fx = 0

        # alles y
        self.y = self.r
        self.vy = 0
        self.ay = 0
        self.fy = 0


class Gui:
    def __init__(self):
        self.backend = Backend()
        self.hauptfenster = Tk()
        self.hauptfenster.geometry('1300x800')
        self.hauptfenster.title('Reversi')
        self.hauptfenster.configure(bg="darkblue")
        self.farben = ['red', 'blue', 'green', 'orange', 'pink', 'yellow', 'lightblue', 'lightgreen', 'lightpink', 'lightyellow'] # farben für die Grafen
        self.farbencount = 0
        self.isSkala = False

        # Canvas    Maßstab von 200.000 zu 1 --> 6.000.000m = 30Pixel
        self.canvas = Canvas(self.hauptfenster, width=1000, height=800, bg='black')  # Canvas color change
        self.canvas.place(x=0, y=0)
        self.erde = PhotoImage(file="earth64x64.png")
        self.canvas.create_image(468, 68, anchor=NW, image=self.erde)
        self.canvas.create_oval(495, 63, 505, 73, fill="red", outline="red")

        # Entry
        self.v0_entry = Entry(self.hauptfenster)
        self.v0_entry.place(x=1050, y=150)
        self.deltat_entry = Entry(self.hauptfenster)
        self.deltat_entry.place(x=1085, y=550)

        # Label
        self.v0_entry_label = Label(self.hauptfenster, text="Startgeschwindigkeit in m/s als Zahl eingeben", bg="darkblue", fg="white")
        self.v0_entry_label.place(x=1020, y=120)
        self.warnung_entry = Label(self.hauptfenster, text="Erst nach Eingabe drücken", bg="darkblue", fg="white")
        self.warnung_entry.place(x=1020, y=220)
        self.falsche_eingame = Label(self.hauptfenster, text="", bg="darkblue")
        self.falsche_eingame.place(x=1020, y=180)
        self.hinweis_L = Label(self.hauptfenster, text='wenn nichts eingetragen, dann gilt "normal"', bg='orange')
        self.hinweis_L.place(x=1020, y=470)
        self.deltat_L = Label(self.hauptfenster, text="delta t\nwie lang ist konstant (in s) Emphelung = 0.1 - 0.5 \n normal = 0.5", bg="darkblue", fg="white")
        self.deltat_L.place(x=1020, y=500)
        self.berechnungen_L = Label(self.hauptfenster, text="es wird solang gerechnet, bis ganze Ellipse vorhanden\nsollte nach 15 000 000 Berechnungen\nkeine entstehen, wird bis dorthin gezeichnet\nund v0 > vP oder deltat zu klein", bg="darkblue", fg="white")
        self.berechnungen_L.place(x=1010, y=600)
        self.skala_L = Label(self.canvas, text="", bg="black", fg="white")
        self.skala_L.place(x=520, y=315)
        self.rmax_L = Label(self.hauptfenster, text=f"", bg="darkblue", fg="white")
        self.rmax_L.place(x=1020, y=350)
        self.credit_L = Label(self.hauptfenster, text="Leander Steffan", bg="darkblue", fg="red")
        self.credit_L.place(x=1200, y=5)

        # Button
        self.start_BTN = Button(self.hauptfenster, text="Start", command=self.start, width=10, height=2, bg='#578251')
        self.start_BTN.place(x=1050, y=250)
        self.skala_BTN = Button(self.hauptfenster, text="Koordinatensystem\naus/an", command=self.skala, width=15, height=2, bg='#578251')
        self.skala_BTN.place(x=1050, y=300)

        self.hauptfenster.mainloop()

    def start(self):
        try:
            self.backend.v0 = int(self.v0_entry.get())
            self.falsche_eingame.configure(text="", bg="darkblue")
            try:
                deltat = float(self.deltat_entry.get())
            except ValueError:
                deltat = 0.5
            self.backend.reset(deltat=deltat)
            self.backend.rechne_coord()
            self.grafischeUmsetzung(self.backend.coord_list)
            self.rmax_L.configure(text=f"Die maximale Entfernung des letzten Satelliten:\n{int(self.backend.r_max / 1000)}km\nDie Umlaufzeit des letzten Satelliten:\n{int(self.backend.umlaufdauer)}s\n{int(self.backend.umlaufdauer/60)}min\n{self.backend.umlaufdauer/3600}h\n{self.backend.umlaufdauer/(3600 * 24)}d")
        except ValueError:
            self.falsche_eingame.configure(text="Falsche Eingabe", bg="red")

    def grafischeUmsetzung(self, coord_liste):
        # Umrechnung der Liste in richtigen Maßstab.        Maßstab von 200.000 zu 1 --> 6.000.000m = 30Pixel
        for i in range(len(coord_liste)):
            for j in [0, 1]:
                if j == 0:
                    coord_liste[i][j] = int(coord_liste[i][j] / 200000) + 500
                if j == 1:
                    coord_liste[i][j] = -(int(coord_liste[i][j] / 200000) - 100)

        # darstellung des Kreises
        for i in range(len(coord_liste) - 1):
            self.canvas.create_line(coord_liste[i][0], coord_liste[i][1], coord_liste[i + 1][0], coord_liste[i + 1][1], fill=self.farben[self.farbencount])
        if self.farbencount == 9:  # nächste Frabe für den nächsten grafen
            self.farbencount = 0
        else:
            self.farbencount += 1

    def skala(self):
        if self.isSkala == False:
            self.isSkala = True
            self.canvas.create_line(500, 132, 500, 800, fill="white")
            for i in range(14):
                self.canvas.create_line(490, 150+50*i, 510, 150+50*i, fill="white")
            self.canvas.create_line(0, 400, 1000, 400, fill="white")
            for i in range(20):
                self.canvas.create_line(50*i, 390, 50*i, 410, fill="white")
            self.canvas.create_line(515, 300, 515, 350, fill="white")
            self.skala_L.configure(text="10'000km")
        else:
            self.isSkala = False
            self.canvas.create_line(500, 132, 500, 800, fill="black")
            for i in range(14):
                self.canvas.create_line(490, 150 + 50 * i, 510, 150 + 50 * i, fill="black")
            self.canvas.create_line(0, 400, 1000, 400, fill="black")
            for i in range(20):
                self.canvas.create_line(50 * i, 390, 50 * i, 410, fill="black")
            self.canvas.create_line(515, 300, 515, 350, fill="black")
            self.skala_L.configure(text="")



model_Erde_Satellit = Gui()

