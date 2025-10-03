
# -*- coding: cp1252 -*-
from tkinter import *
# import tkMessageBox


class Reversi:
    def __init__(self):

        self.spielfeld= [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
        '''self.feld_datei_name = '1.txt'           # When you want to read in Field
        self.datei = open(f".\Fields\{self.feld_datei_name}")
        self.spielfeld = self.datei.readlines()
        for i in range(len(self.spielfeld)):
            self.spielfeld[i] = self.spielfeld[i].strip()
            self.spielfeld[i] = self.spielfeld[i].split(' ')
            for j in range(len(self.spielfeld[i])):
                self.spielfeld[i][j] = int(self.spielfeld[i][j])
        self.datei.close()'''
        print(self.spielfeld)

        self.spielfeld[3][3]=1
        self.spielfeld[3][4]=2
        self.spielfeld[4][3]=2
        self.spielfeld[4][4]=1
        self.nachbarn=[(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
        self.aktSpieler=1           
        self.gegner=2
        self.felder=[]
        self.z=0
        self.s=0
        self.spielende=0
        self.eins_counter=2
        self.zwei_counter=2
        self.is_ki = False
        self.empty_koords = []
        


    def umdrehen(self, felder):
        felder.append((self.z,self.s))
        #print "in umdrehen: ", felder
        for feld in felder:
            z=feld[0]
            s=feld[1]
            if self.aktSpieler==1:
                self.spielfeld[z][s]=1
            elif self.aktSpieler==2:
                self.spielfeld[z][s]=2
            

    def indexfehler(self,s,z):
        if s>7 or s<0 or z>7 or z<0 :
            'print("indexfehler %i, %i" %(s,z))' # nervt
            return 1
        else:
            return 0
        
    def gueltigerZug(self, z, s):
        steine = []
        drehsteine = []
        if not self.indexfehler(z, s) and self.spielfeld[z][s] == 0:
            for n in self.nachbarn:
                steine = []
                nachbary = z + n[0]
                nachbarx = s + n[1]
                while not (self.indexfehler(nachbary, nachbarx)) and self.spielfeld[nachbary][nachbarx] == self.gegner:
                    steine.append((nachbary, nachbarx))
                    nachbary = nachbary + n[0]
                    nachbarx = nachbarx + n[1]
                if not (self.indexfehler(nachbary, nachbarx)) and self.spielfeld[nachbary][nachbarx] == self.aktSpieler and len(steine) > 0:
                    drehsteine = drehsteine + steine
        return drehsteine

    def ki_on_off(self):
        if self.is_ki:
            self.is_ki = False
        else:
            self.is_ki = True

    def ki_turn(self):
        print('ki turn')
        every_koord_with_drehstein = []
        self.empty_koords = []
        for i in range(len(self.spielfeld)):
            for j in range(len(self.spielfeld[i])):
                if self.spielfeld[i][j] == 0:
                    self.empty_koords.append([i, j])
        print(self.empty_koords)
        for i in range(len(self.empty_koords)):
            if self.gueltigerZug(self.empty_koords[i][0], self.empty_koords[i][1]):
                '''appendix1 = [self.empty_koords[i][0], self.empty_koords[i][1]]
                appendix2 = self.gueltigerZug(self.empty_koords[i][0], self.empty_koords[i][1])'''
                every_koord_with_drehstein.append([[self.empty_koords[i][0], self.empty_koords[i][1]], self.gueltigerZug(self.empty_koords[i][0], self.empty_koords[i][1])])
        '''if not every_koord_with_drehstein:
            print('player1 win')'''
        print(every_koord_with_drehstein)
        ki_zug = every_koord_with_drehstein[0]
        for i in range(len(every_koord_with_drehstein)):
            if len(every_koord_with_drehstein[i][1]) > len(ki_zug[1]):
                ki_zug = every_koord_with_drehstein[i]
        return (ki_zug[0][0], ki_zug[0][1])
 

    def spielerwechsel(self):
        if self.aktSpieler==1:
            self.aktSpieler=2
            self.gegner=1
        else:
            self.aktSpieler=1
            self.gegner=2
        

    def spielende_ueberpruefung(self):
        if self.eins_counter+self.zwei_counter==60:
            self.spielende=1
        
    def zaehle(self):
        for z in self.spielfeld:
            for s in self.spielfeld:
                if self.spielfeld[z][s] == 1:
                    self.eins_counter =+ 1
                    return self.eins_counter
                elif self.spielfeld[z][s] == 2:
                    self.zwei_counter =+1
                    return self.zwei_counter

    def setzen(self, zeile, spalte):
        print('setzen', zeile, spalte)
        self.spielende_ueberpruefung()
        positionen=self.gueltigerZug(zeile, spalte)
        if positionen:
            self.umdrehen(positionen)
        if self.spielende==0  and positionen:
            self.spielerwechsel()


#Hauptprogramm
class Gui:
    def __init__(self):
        
        self.modell=Reversi()
        self.hauptfenster=Tk()
        self.hauptfenster.geometry('850x700')
        self.hauptfenster.title('Reversi')
        self.hauptfenster.configure(bg="#2b2b2b")

        #Canvas
        '''self.canvas=Canvas(self.hauptfenster,height=600,width=600, bg='#1d3227')''' # original
        self.canvas = Canvas(self.hauptfenster, height=600, width=600, bg='lightgreen') # Canvas color change
        self.canvas.place(x=25,y=25)
        self.dran_cnv = Canvas(self.hauptfenster, height=75, width=75, bg='lightgreen')  # Canvas color change
        self.dran_cnv.place(x=750, y=15)
        self.canvas.bind("<Button-1>", func=self.setzen)
        #Lines
        for i in range(1,8):
            self.canvas.create_line(i*75,600,i*75,0)
        for i in range(1,8):
            self.canvas.create_line(0,i*75,600,i*75)

        #Buttons
        self.restart_BTN = Button(self.hauptfenster, text="Starten",command=self.restart, width=10, height=2, bg='#578251')
        self.restart_BTN.place(x=650,y=575)
        self.close_BTN = Button(self.hauptfenster, text="Close",command=self.close, width=10, height=2, bg='#f99266')
        self.close_BTN.place(x=750,y=575)
        self.regeln_BTN=Button(self.hauptfenster,text="Regeln",command=self.popupfenster,width=10,height=2)
        self.regeln_BTN.place(x=650,y=500)
        self.ki_BTN = Button(self.hauptfenster, text="KI", command=self.modell.ki_on_off, width=10, height=2, bg='orange')
        self.ki_BTN.place(x=750, y=500)

        #Labels
        self.spieler_LBL=Label(self.hauptfenster, text='Spieler 1 ist am Zug', bg= '#c16c02', font=("Timesnewroman", 15))
        self.spieler_LBL.place(x=650, y=100)
        self.when_ki_LBL = Label(self.hauptfenster, text='KI ist Spieler zwei und kann\n nur im Zug von Spieler 1\n betätigt werden.', bg='#c16c02', font=("Timesnewroman", 10))
        self.when_ki_LBL.place(x=650, y=140)
        self.how_ki_LBL = Label(self.hauptfenster, text='Damit die KI ihren Zug macht\n muss man wenn Spieler 2\n dran ist irgendwo hin tippen', bg='#c16c02', font=("Timesnewroman", 10))
        self.how_ki_LBL.place(x=650, y=200)
        self.wer_ist_LBL = Label(self.hauptfenster, text='Dran ist:', bg='#c16c02', font=("Timesnewroman", 15))
        self.wer_ist_LBL.place(x=655, y=45)
        
        
        self.hauptfenster.mainloop()
        
    def aktualisiere(self):
        print(self.modell.is_ki)
        for s in range(0, 8):
            for z in range(0, 8):
                if self.modell.spielfeld[s][z]==1:
                    self.canvas.create_oval((75)*s,(75)*z, (s*75)+75, (z*75)+75, fill="black")
                elif self.modell.spielfeld[s][z]==2:
                    self.canvas.create_oval((75)*s,(75)*z, (s*75)+75, (z*75)+75, fill='white')
                    
        if self.modell.aktSpieler == 1:
            self.spieler_LBL['text'] = 'Spieler 1 ist am Zug'
            self.dran_cnv.create_oval(5, 5, 74, 74, fill='black')
        if self.modell.aktSpieler == 2:
            self.spieler_LBL['text'] = 'Spieler 2 ist am Zug'
            self.dran_cnv.create_oval(5, 5, 74, 74, fill='white')

        self.gewinnfenster()
                    
    def setzen(self, event):
        if self.modell.aktSpieler == 2 and self.modell.is_ki:
            self.ki_setzen()
        else:
            self.modell.z = int(event.x/75)
            self.modell.s = int(event.y/75)
            self.modell.setzen(self.modell.z, self.modell.s)
            self.aktualisiere()

    def ki_setzen(self):
        position = self.modell.ki_turn()
        self.modell.z = position[0]
        self.modell.s = position[1]
        self.modell.setzen(self.modell.z, self.modell.s)
        self.aktualisiere()

    def restart(self):
        self.modell.__init__()
        #Canvas
        self.canvas.delete("all")
        '''self.canvas=Canvas(self.hauptfenster,height=600,width=600, bg='#1d3227')''' # original
        self.canvas = Canvas(self.hauptfenster, height=600, width=600, bg='lightgreen')  # Canvas color change
        self.canvas.place(x=25,y=25)
        self.canvas.bind("<Button-1>", func=self.setzen)
        #Lines
        for i in range(1,8):
            self.canvas.create_line(i*75,600,i*75,0)
        for i in range(1,8):
            self.canvas.create_line(0,i*75,600,i*75)
        self.aktualisiere()
            
    def starten(self):
        self.aktualisiere()
        self.hauptfenster.mainloop()
        self.modell.__init__()
        
    def close(self):
        self.hauptfenster.destroy()
        self.hauptfenster2.destroy()
        
    def close2(self):
        self.hauptfenster2.destroy()
        
    def popupfenster(self):
        self.hauptfenster2=Tk()
        self.hauptfenster2.geometry('800x500')
        self.hauptfenster2.title('Spielregeln Reversi:')
        with open('Reversi_Regeln.txt','r') as f:
            Label(self.hauptfenster2, text=f.read()).pack()
            
        self.close2_BTN = Button(self.hauptfenster2, text="Close",command=self.close2, width=10, height=2, bg='#f99266')
        self.close2_BTN.place(x=675,y=450)

    def gewinnfenster(self):
        if self.modell.spielende==1:
            if self.modell.eins_counter>self.modell.eins_counter:
                gewinnfenster1 = tkMessageBox.showinfo('Gewinnfenster','Spieler1 hat gewonnen')
            if self.modell.zwei_counter>self.modell.eins_counter:
                    gewinnfenster2 = tkMessageBox.showinfo('Gewinnfenster','Spieler2 hat gewonnen')
    
#Hauptprogramm                    
gui=Gui()
gui.starten()
gui.gewinnfenster()
