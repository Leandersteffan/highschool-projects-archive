from tkinter import *


class Tik_Tak_To:
    def __init__(self):
        self.hauptfenster = Tk()
        self.hauptfenster.title("Tik_Tak_To")
        self.hauptfenster.geometry("670x420")
        self.hauptfenster_color = 'lightgreen'
        self.hauptfenster.configure(background=self.hauptfenster_color)

        self.siege_1 = 0
        self.siege_2 = 0
        self.aktueller_spieler = 1
        self.spielfeld = [[0,0,0],[0,0,0],[0,0,0]]
        self.darf_klicken = True
        self.lines = []
        

        #Canvas
        self.spielfenster_CNV = Canvas(self.hauptfenster, width = 300, height = 300, bg='white')
        self.spielfenster_CNV.place(x = 350, y = 100)


        #Label
        self.weristAnzeige_La = Label(self.hauptfenster, bg=self.hauptfenster_color, text = 'Spieler 1 ist dran')
        self.weristAnzeige_La.place(x = 450, y = 70)

        self.title_La = Label(self.hauptfenster, bg=self.hauptfenster_color, font = 15, text = 'Tik Tak To')
        self.title_La.place(x = 300, y = 30)

        self.gewinner_masg_La = Label(self.hauptfenster, bg=self.hauptfenster_color, font = 20, fg = 'red', text = '')
        self.gewinner_masg_La.place(x = 425, y = 40)
        
        self.statistik_überschrift_La = Label(self.hauptfenster, bg=self.hauptfenster_color, text = 'Statistiken:')
        self.statistik_überschrift_La.place(x = 20, y = 250)
        self.spieler1siege_La = Label(self.hauptfenster, bg=self.hauptfenster_color, text = 'Spieler 1 Siege: ' + str(self.siege_1))
        self.spieler1siege_La.place(x = 20, y = 280)
        self.spieler2siege_La = Label(self.hauptfenster, bg=self.hauptfenster_color, text = 'Spieler 2 Siege: ' + str(self.siege_2))
        self.spieler2siege_La.place(x = 20, y = 300)

        #Button
        self.ende_BTN=Button(self.hauptfenster,text="Beenden",bg='red',width=10,height=2, command = self.ende)
        self.ende_BTN.place(x=20,y=150)
        self.neues_spiel_BTN=Button(self.hauptfenster,text="Neues Spiel",bg='yellow',width=10,height=2, command = self.neues_spiel)
        self.neues_spiel_BTN.place(x=20,y=100)
        self.save_BTN=Button(self.hauptfenster,text="Save",bg='orange',width=10,height=2, command = self.save)
        self.save_BTN.place(x=120,y=100)
        self.load_BTN=Button(self.hauptfenster,text="Load",bg='white',width=10,height=2, command = self.load)
        self.load_BTN.place(x=120,y=150)
        
        self.spielfenster_CNV.bind("<Button-1>", self.play)

        self.neues_spiel()
        self.hauptfenster.mainloop()
        
    def save(self):
        with open('gespeichert.txt','r+') as f:
            f.write(str(self.spielfeld))
            f.write("\n")
            f.write(str(self.aktueller_spieler))
            f.write("\n")
            f.write(str(self.siege_1))
            f.write("\n")
            f.write(str(self.siege_2))
            f.write("\n")
            f.write(str(self.darf_klicken))
            f.write("\n")
        print('save', self.spielfeld)

    def load(self):
        file1 = open('gespeichert.txt', 'r')
        self.lines = file1.readlines()
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i][:-1]
        print('load', self.lines)
        self.aktueller_spieler = int(self.lines[1])
        self.siege_1 = int(self.lines[2])
        self.spieler1siege_La.configure(text='Spieler 1 Siege: ' + str(self.siege_1))
        self.siege_2 = int(self.lines[3])
        self.spieler2siege_La.configure(text='Spieler 2 Siege: ' + str(self.siege_2))
        if self.lines[4] == 'False':
            self.darf_klicken = False
        self.load_draw()
        
    def neues_spiel(self):
        self.gewinner_masg_La.configure(text = '')
        self.spielfenster_CNV.create_rectangle(-10,-10,310,310,fill='white')
        #Felderstellung
        self.spielfenster_CNV.create_line(0,100,300,100,fill='black',width=2)
        self.spielfenster_CNV.create_line(0,200,300,200,fill='black',width=2)
        self.spielfenster_CNV.create_line(100,0,100,300,fill='black',width=2)
        self.spielfenster_CNV.create_line(200,0,200,300,fill='black',width=2)
        self.spielfeld = [[0,0,0],[0,0,0],[0,0,0]]
        self.aktueller_spieler = 1
        self.darf_klicken = True
        self.weristAnzeige_La.configure(text = 'Spieler 1 ist dran')

    def spielerwechsel(self):
        if self.aktueller_spieler == 1:
            self.aktueller_spieler = 2
            self.weristAnzeige_La.configure(text = 'Spieler 2 ist dran')
        elif self.aktueller_spieler == 2:
            self.aktueller_spieler = 1
            self.weristAnzeige_La.configure(text = 'Spieler 1 ist dran')

    def check_win(self):
        self.is_win = False
        self.zwischenspeicher_sieger = 0
        if self.spielfeld[0][0] == self.spielfeld[1][1] and self.spielfeld[0][0] == self.spielfeld[2][2] or self.spielfeld[2][0] == self.spielfeld[1][1] and self.spielfeld[2][0] == self.spielfeld[0][2]:
            if self.spielfeld[1][1] != 0:
                    self.is_win = True
                    self.zwischenspeicher_sieger = self.spielfeld[1][1]
        else:
            for i in range(3):
                if self.spielfeld[i][0] == self.spielfeld[i][1] and self.spielfeld[i][0] == self.spielfeld[i][2]:
                    if self.spielfeld[i][0] != 0:
                        self.is_win = True
                        self.zwischenspeicher_sieger = self.spielfeld[i][0]
                elif self.spielfeld[0][i] == self.spielfeld[1][i] and self.spielfeld[0][i] == self.spielfeld[2][i]:
                    if self.spielfeld[0][i] != 0:
                        self.is_win = True
                        self.zwischenspeicher_sieger = self.spielfeld[0][i]
        if self.is_win:
            if self.zwischenspeicher_sieger == 1:
                self.spieler1_win()
            elif self.zwischenspeicher_sieger == 2:
                self.spieler2_win()

    def play(self, event):
        #Spalte 1
        if self.darf_klicken:
            if event.x >= 0 and event.x < 100:
                if event.y >= 0 and event.y < 100:
                    if self.spielfeld[0][0] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(10,10,90,90,fill='black',width=5)
                            self.spielfenster_CNV.create_line(10,90,90,10,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(10,10,90,90,width=5)
                        self.spielfeld[0][0] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 100 and event.y < 200:
                    if self.spielfeld[1][0] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(10,110,90,190,fill='black',width=5)
                            self.spielfenster_CNV.create_line(10,190,90,110,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(10,110,90,190,width=5)
                        self.spielfeld[1][0] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 200 and event.y < 300:
                    if self.spielfeld[2][0] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(10,210,90,290,fill='black',width=5)
                            self.spielfenster_CNV.create_line(10,290,90,210,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(10,210,90,290,width=5)
                        self.spielfeld[2][0] = self.aktueller_spieler
                        self.spielerwechsel()
            #Spalte 2            
            if event.x >= 100 and event.x < 200:
                if event.y >= 0 and event.y < 100:
                    if self.spielfeld[0][1] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(110,10,190,90,fill='black',width=5)
                            self.spielfenster_CNV.create_line(110,90,190,10,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(110,10,190,90,width=5)
                        self.spielfeld[0][1] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 100 and event.y < 200:
                    if self.spielfeld[1][1] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(110,110,190,190,fill='black',width=5)
                            self.spielfenster_CNV.create_line(110,190,190,110,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(110,110,190,190,width=5)
                        self.spielfeld[1][1] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 200 and event.y < 300:
                    if self.spielfeld[2][1] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(110,210,190,290,fill='black',width=5)
                            self.spielfenster_CNV.create_line(110,290,190,210,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(110,210,190,290,width=5)
                        self.spielfeld[2][1] = self.aktueller_spieler
                        self.spielerwechsel()
            #Spalte 3
            if event.x >= 200 and event.x < 300:
                if event.y >= 0 and event.y < 100:
                    if self.spielfeld[0][2] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(210,10,290,90,fill='black',width=5)
                            self.spielfenster_CNV.create_line(210,90,290,10,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(210,10,290,90,width=5)
                        self.spielfeld[0][2] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 100 and event.y < 200:
                    if self.spielfeld[1][2] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(210,110,290,190,fill='black',width=5)
                            self.spielfenster_CNV.create_line(210,190,290,110,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(210,110,290,190,width=5)
                        self.spielfeld[1][2] = self.aktueller_spieler
                        self.spielerwechsel()
                if event.y >= 200 and event.y < 300:
                    if self.spielfeld[2][2] == 0:
                        if self.aktueller_spieler == 1:
                            self.spielfenster_CNV.create_line(210,210,290,290,fill='black',width=5)
                            self.spielfenster_CNV.create_line(210,290,290,210,fill='black',width=5)
                        else:
                            self.spielfenster_CNV.create_oval(210,210,290,290,width=5)
                        self.spielfeld[2][2] = self.aktueller_spieler
                        self.spielerwechsel()
            self.check_win()

    def spieler1_win(self):
        self.siege_1 += 1
        self.spieler1siege_La.configure(text = 'Spieler 1 Siege: ' + str(self.siege_1))
        self.gewinner_masg_La.configure(text = 'Spieler 1 hat gewonnen')
        self.darf_klicken = False

    def spieler2_win(self):
        self.siege_2 += 1
        self.spieler2siege_La.configure(text = 'Spieler 2 Siege: ' + str(self.siege_2))
        self.gewinner_masg_La.configure(text = 'Spieler 2 hat gewonnen')
        self.darf_klicken = False

    def ende(self):
        self.hauptfenster.destroy()

    def load_draw(self):
        self.lines = self.lines[0]
        a, b, c, d, e, f, g, h, i = int(self.lines[2]), int(self.lines[5]), int(self.lines[8]), int(self.lines[13]), int(self.lines[16]), int(self.lines[19]), int(self.lines[24]), int(self.lines[27]), int(self.lines[30])
        self.spielfeld = [[a, b, c], [d, e, f], [g, h, i]]
        print('load 1', self.spielfeld)
        if self.aktueller_spieler == 1:
            self.weristAnzeige_La.configure(text = 'Spieler 1 ist dran')
        elif self.aktueller_spieler == 2:
            self.weristAnzeige_La.configure(text = 'Spieler 2 ist dran')
        if self.spielfeld[0][0] != 0:
            if self.spielfeld[0][0] == 1:
                self.spielfenster_CNV.create_line(10, 10, 90, 90, fill='black', width=5)
                self.spielfenster_CNV.create_line(10, 90, 90, 10, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(10, 10, 90, 90, width=5)
        if self.spielfeld[1][0] != 0:
            if self.spielfeld[1][0] == 1:
                self.spielfenster_CNV.create_line(10, 110, 90, 190, fill='black', width=5)
                self.spielfenster_CNV.create_line(10, 190, 90, 110, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(10, 110, 90, 190, width=5)
        if self.spielfeld[2][0] != 0:
            if self.spielfeld[2][0] == 1:
                self.spielfenster_CNV.create_line(10, 210, 90, 290, fill='black', width=5)
                self.spielfenster_CNV.create_line(10, 290, 90, 210, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(10, 210, 90, 290, width=5)

        if self.spielfeld[0][1] != 0:
            if self.spielfeld[0][1] == 1:
                self.spielfenster_CNV.create_line(110, 10, 190, 90, fill='black', width=5)
                self.spielfenster_CNV.create_line(110, 90, 190, 10, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(110, 10, 190, 90, width=5)
        if self.spielfeld[1][1] != 0:
            if self.spielfeld[1][1] == 1:
                self.spielfenster_CNV.create_line(110, 110, 190, 190, fill='black', width=5)
                self.spielfenster_CNV.create_line(110, 190, 190, 110, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(110, 110, 190, 190, width=5)
        if self.spielfeld[2][1] != 0:
            if self.spielfeld[2][1] == 1:
                self.spielfenster_CNV.create_line(110, 210, 190, 290, fill='black', width=5)
                self.spielfenster_CNV.create_line(110, 290, 190, 210, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(110, 210, 190, 290, width=5)

        if self.spielfeld[0][2] != 0:
            if self.spielfeld[0][2] == 1:
                self.spielfenster_CNV.create_line(210, 10, 290, 90, fill='black', width=5)
                self.spielfenster_CNV.create_line(210, 90, 290, 10, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(210, 10, 290, 90, width=5)
        if self.spielfeld[1][2] != 0:
            if self.spielfeld[1][2] == 1:
                self.spielfenster_CNV.create_line(210, 110, 290, 190, fill='black', width=5)
                self.spielfenster_CNV.create_line(210, 190, 290, 110, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(210, 110, 290, 190, width=5)
        if self.spielfeld[2][2] != 0:
            if self.spielfeld[2][2] == 1:
                self.spielfenster_CNV.create_line(210, 210, 290, 290, fill='black', width=5)
                self.spielfenster_CNV.create_line(210, 290, 290, 210, fill='black', width=5)
            else:
                self.spielfenster_CNV.create_oval(210, 210, 290, 290, width=5)



spiel = Tik_Tak_To()
