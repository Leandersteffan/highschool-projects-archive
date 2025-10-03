from tkinter import *


class Halbwertszeit(object):
    def __init__(self):

        self.hauptfenster = Tk()
        self.hauptfenster.title("Halbwertszeitveranschaulichung")
        self.hauptfenster.geometry("1080x720")
        self.hauptfenster_hintergrund="white"  #"lightblue"
        self.hauptfenster.configure(background=self.hauptfenster_hintergrund)

        #Canvas für Balken und Diagramme
        self.diagramm_CNV = Canvas(self.hauptfenster, width=800, height=680, bg="white")
        self.diagramm_CNV.place(x=0, y=0)

        #Buttons and entrys
        self.ende_BTN = Button(self.hauptfenster, text="Beenden", bg='red', width=10, height=2, command=self.ende)
        self.ende_BTN.place(x=900, y=50)

        self.set_start_BTN = Button(self.hauptfenster, text="Set Start", bg='orange', width=10, height=2, command=self.set_start)
        self.set_start_BTN.place(x=900, y=150)

        self.halbwertszeit1_entry = Entry(self.hauptfenster, width=10)
        self.halbwertszeit1_entry.place(x=900, y=245)

        self.halbwertszeit2_entry = Entry(self.hauptfenster, width=10)
        self.halbwertszeit2_entry.place(x=900, y=290)

        self.interval_entry = Entry(self.hauptfenster, width=10)
        self.interval_entry.place(x=900, y=380)

        self.abbruch_entry = Entry(self.hauptfenster, width=10)
        self.abbruch_entry.place(x=900, y=450)

        self.start_BTN = Button(self.hauptfenster, text="Start", bg='green', width=10, height=2, command=lambda: self.start(float(self.interval_entry.get()), float(self.abbruch_entry.get()), float(self.halbwertszeit1_entry.get()), float(self.halbwertszeit2_entry.get())))
        self.start_BTN.place(x=900, y=500)

        self.dia_BTN = Button(self.hauptfenster, text="Diagramme", bg='lightblue', width=10, height=2, command=lambda: self.draw_diagramm())
        self.dia_BTN.place(x=900, y=580)

        #Label
        self.hwz1_Label = Label(self.hauptfenster, text="Halbwertszeit erster Stoff", bg='white')
        self.hwz1_Label.place(x=870, y=220)
        self.hwz2_Label = Label(self.hauptfenster, text="Halbwertszeit zweiter Stoff", bg='white')
        self.hwz2_Label.place(x=870, y=265)
        self.interval_Label = Label(self.hauptfenster, text="Interval zwischen Rechnungen\numso kleiner umso genauer aber dauert länger\nhängt von betrachteter Zeit ab\nstandard ist 0.5", bg='white')
        self.interval_Label.place(x=815, y=310)
        self.abbruch_Label = Label(self.hauptfenster, text="unter welche Prozent müssen\nAnteil 1 und 2 fallen damit Abgebrochen wird?\nstandard ist 0.03%", bg='white')
        self.abbruch_Label.place(x=815, y=400)
        self.diagramm_Label = Label(self.hauptfenster, text="nicht bereit für Diagramm!", bg='red')
        self.diagramm_Label.place(x=870, y=550)
        self.leander_Label = Label(self.hauptfenster, text="Leander Steffan", bg='lightgreen')
        self.leander_Label.place(x=980, y=10)


        #Variabeln
        self.interval_entry.insert(0, 0.5)
        self.abbruch_entry.insert(0, 0.03)
        self.halbwertszeit1 = 30
        self.halbwertszeit2 = 30
        self.time = 0
        self.turm1_anteil_zwischenscheicher = 1
        self.turm2_anteil_zwischenscheicher = 0
        self.intervallength = 0.5
        self.turm2_übergangs_liste = []
        self.diagramm_liste_1 = []
        self.diagramm_liste_2 = []
        self.diagramm_liste_3 = []
        self.end_when_tower_under = 0.03

        self.hauptfenster.mainloop()

    def set_start(self):
        self.diagramm_CNV.create_rectangle(0, 0, 800, 680, fill="white")
        self.diagramm_CNV.create_rectangle(100, 50, 200, 600, fill="red")
        self.diagramm_CNV.create_text(150, 640, text="1", fill="red", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(350, 640, text="2", fill="green", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(550, 640, text="3", fill="black", font=('Helvetica 25 bold'))
        self.halbwertszeit1 = 30
        self.halbwertszeit2 = 30
        self.time = 0
        self.turm1_anteil_zwischenscheicher = 1
        self.turm2_anteil_zwischenscheicher = 0
        self.intervallength = 0.5
        self.turm2_übergangs_liste = []
        self.diagramm_liste_1 = []
        self.diagramm_liste_2 = []
        self.diagramm_liste_3 = []
        self.end_when_tower_under = 0.03

    def update_by_Anteil(self, turm1, turm2, turm3):    #gives height of towers depending on how much they have and displays them
        self.diagramm_CNV.create_rectangle(0, 0, 800, 680, fill="white")
        self.diagramm_CNV.create_rectangle(100, 50 + (1- turm1) * 550, 200, 600, fill="red")
        self.diagramm_CNV.create_rectangle(300, 50 + (1- turm2) * 550, 400, 600, fill="green")
        self.diagramm_CNV.create_rectangle(500, 50 + (1 - turm3) * 550, 600, 600, fill="black")
        self.diagramm_CNV.create_text(150, 640, text="1", fill="red", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(350, 640, text="2", fill="green", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(550, 640, text="3", fill="black", font=('Helvetica 25 bold'))

    def start(self, interval, abbruch, halbwertszeit1, halbwertszeit2):
        self.intervallength = interval
        self.end_when_tower_under = abbruch
        self.halbwertszeit1 = halbwertszeit1
        self.halbwertszeit2 = halbwertszeit2
        self.big_time_loop(self.intervallength)

    def big_time_loop(self, intervals):
        #print("ss", self.time)
        self.time += intervals
        turm1_anteil, turm2_anteil, turm3_anteil = self.berechnen_Anteil_halbwertszeitanteril(self.time, self.halbwertszeit1, self.halbwertszeit2)
        self.diagramm_liste_1.append(turm1_anteil)
        self.diagramm_liste_2.append(turm2_anteil)
        self.diagramm_liste_3.append(turm3_anteil)
        #print(turm1_anteil, turm2_anteil, turm3_anteil)
        if turm1_anteil < self.end_when_tower_under and turm2_anteil < self.end_when_tower_under:
            self.diagramm_Label.configure(text="bereit für Diagramm", bg="green")
            self.diagramm_Label.place(x=884, y=550)
            return None
        self.update_by_Anteil(turm1_anteil, turm2_anteil, turm3_anteil)
        self.hauptfenster.after(1, lambda: self.big_time_loop(intervals))

    def turm2(self, neuerÜbergang, past_time, halbwertszeit2): #return des Aktuellen turm 2 anteils über individuelle betrachtung der Übergänge
        self.turm2_übergangs_liste.append(neuerÜbergang)
        if self.turm2_übergangs_liste:
            for i in range(len(self.turm2_übergangs_liste)):
                past_time = past_time - self.intervallength
                if past_time > 0:
                    self.turm2_übergangs_liste[i] = self.turm2_übergangs_liste[i] * ((1/2)**(past_time/halbwertszeit2))
        #print("llll", self.turm2_übergangs_liste)
        return sum(self.turm2_übergangs_liste)

    def berechnen_Anteil_halbwertszeitanteril(self, past_time, halbwertszeit1, halbwertszeit2): #rechnet aus wie viel noch im ersten sind und returnt prozent für Trum eins und zwei
        turm1_anteil = 1 * ((1/2)**(past_time/halbwertszeit1))
        #print(self.turm1_anteil_zwischenscheicher, turm1_anteil)
        turm1_übergang = self.turm1_anteil_zwischenscheicher - turm1_anteil
        self.turm1_anteil_zwischenscheicher = turm1_anteil
        turm2_anteil = self.turm2(turm1_übergang, past_time, halbwertszeit2)
        #turm2_anteil = 1 - turm1_anteil
        #turm2_anteil = (self.turm2_anteil_zwischenscheicher + turm1_übergang) * ((1/2)**(past_time/halbwertszeit2))
        #print("!!!!!!!!!", turm1_anteil, turm1_übergang, turm2_anteil, self.time, "Bruch::", (turm1_übergang/turm2_anteil))
        #self.turm2_anteil_zwischenscheicher = turm2_anteil
        turm3_anteil = 1 - turm1_anteil - turm2_anteil
        return turm1_anteil, turm2_anteil, turm3_anteil

    def draw_diagramm(self):
        self.diagramm_CNV.create_rectangle(0, 0, 800, 680, fill="white")
        #achsen
        self.diagramm_CNV.create_line(50,50,50,620, fill="black", width=2)
        self.diagramm_CNV.create_line(50, 620, 750, 620, fill="black", width=2)

        if len(self.diagramm_liste_1) >= 700:
            if len(self.diagramm_liste_1) >= 1400:
                listenverkleinerung = len(self.diagramm_liste_1) // 700  # wird errechnet jedes wie vielte Element man nimmt für das diagramm
                listenverkleinerung += 1
            elif len(self.diagramm_liste_1) >= 700:
                listenverkleinerung = 2
            listenverkleinerung = len(self.diagramm_liste_1) // 700  # wird errechnet jedes wie vielte Element man nimmt für das diagramm
            listenverkleinerung += 1
            gut_liste_1, gut_liste_2, gut_liste_3 = self.diagramm_liste_1, self.diagramm_liste_2, self.diagramm_liste_3
            self.diagramm_liste_1, self.diagramm_liste_2, self.diagramm_liste_3 = [], [], []
            listenverkleinerung = len(self.diagramm_liste_1)//700    #wird errechnet jedes wie vielte Element man nimmt für das diagramm
            print(listenverkleinerung, len(self.diagramm_liste_1))
            for i in range(len(self.diagramm_liste_1)):
                if i % listenverkleinerung == 0:
                    self.diagramm_liste_1.append(gut_liste_1[i])
                    self.diagramm_liste_2.append(gut_liste_2[i])
                    self.diagramm_liste_3.append(gut_liste_3[i])

        for i in range(1, len(self.diagramm_liste_1)):
            self.diagramm_CNV.create_line(i + 50, 50 + (1- self.diagramm_liste_1[i-1]) * 570, i + 50, 50 + (1- self.diagramm_liste_1[i]) * 570, fill="red", width=2)
            self.diagramm_CNV.create_line(i + 50, 50 + (1- self.diagramm_liste_2[i-1]) * 570, i + 50, 50 + (1- self.diagramm_liste_2[i]) * 570, fill="green", width=2)
            self.diagramm_CNV.create_line(i + 50, 50 + (1- self.diagramm_liste_3[i-1]) * 570, i + 50, 50 + (1- self.diagramm_liste_3[i]) * 570, fill="black", width=2)
        self.diagramm_CNV.create_text(25, 50, text="1", fill="red", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(15, 620, text="2", fill="green", font=('Helvetica 25 bold'))
        self.diagramm_CNV.create_text(35, 620, text="3", fill="black", font=('Helvetica 25 bold'))

    def ende(self):
        self.hauptfenster.destroy()



start = Halbwertszeit()
