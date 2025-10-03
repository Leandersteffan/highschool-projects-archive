# Datenmodell
from random import *
class Ratezahl(object):
    def __init__(self):
        self.zahl = 1

    def erzeugen(self, uGrenze, oGrenze):
        self.zahl = randint(uGrenze, oGrenze)

    def getZahl(self):
        return self.zahl

class Zaehler(object):
    def __init__(self):
        self.stand = 0

    def setzen(self, zahl):
        self.stand = zahl

    def weiter(self):
        self.stand = self.stand + 1

    def getStand(self):
        return self.stand

ratezahl = Ratezahl()
zaehler = Zaehler()
zaehler.setzen(1)

# GUI
from tkinter import *
from time import sleep
# Ereignisbehandlung

def buttonNeueZahlClick():
    ratezahl.erzeugen(1, obergrenze.get())
    zaehler.setzen(1)
    labelVersuche.config(text=str(zaehler.getStand()) + '. Rateversuch')
    entryZahl.delete(0, 'end')
    labelRueckmeldung.config(text='')
    

def buttonRatenClick(event):
    try:
        zahlGeraten = int(entryZahl.get())
        if zahlGeraten < 1 or zahlGeraten >  obergrenze.get():
            messagebox.showerror('Fehler', 'Zahl nicht im im gewÃ¤hlten Zahlbereich!')
            tkFenster.after(1, neuerRateversuch)
        else:
            if zahlGeraten == ratezahl.getZahl():
                labelRueckmeldung.config(text='Treffer')
            else:
                if zahlGeraten < ratezahl.getZahl():
                    labelRueckmeldung.config(text='zu klein')
                elif zahlGeraten > ratezahl.getZahl():
                    labelRueckmeldung.config(text='zu groÃŸ')
                tkFenster.after(1, neuerRateversuch)
    except:
        messagebox.showerror('Fehler', 'Keine sinnvolle Eingabe!')
        tkFenster.after(1, neuerRateversuch)
        

def neuerRateversuch():
    sleep(1)
    zaehler.weiter()
    labelVersuche.config(text=str(zaehler.getStand()) + '. Rateversuch')
    entryZahl.delete(0, 'end')
    labelRueckmeldung.config(text='')

def buttonBeendenClick():
    if messagebox.askyesno('Beenden', 'Soll das Spiel wirklich beendet werden?'):
        tkFenster.quit()
        tkFenster.destroy()

# Fenster
tkFenster = Tk()
tkFenster.title('Zahlenraten')
tkFenster.geometry('350x235')
# Rahmen
frameUeberschrift = Frame(master=tkFenster, bg='#889E9D')
frameUeberschrift.place(x=5, y=5, width=340, height=30)
frameSpiel = Frame(master=tkFenster, bg="#FFCFC9")
frameSpiel.place(x=5, y=40, width=340, height=80)
frameRaten = Frame(master=tkFenster, bg="#D5E88F")
frameRaten.place(x=5, y=125, width=340, height=105)
# Ãœberschrift
labelUeberschrift = Label(master=frameUeberschrift, text="Zahlenraten", 
                          fg="white", bg="#889E9D", font=("Arial", 16))
labelUeberschrift.place(x=5, y=5, width=330, height=20)
# Festlegung des Zahlenbereichs
obergrenze = IntVar()
radiobutton1 = Radiobutton(master=frameSpiel, anchor='w',
                           text='1..100', value=100, variable=obergrenze)
radiobutton1.place(x=5, y=5, width=80, height=20)
radiobutton2 = Radiobutton(master=frameSpiel, anchor='w',
                           text='1..500', value=500, variable=obergrenze)
radiobutton2.place(x=5, y=30, width=80, height=20)
radiobutton3 = Radiobutton(master=frameSpiel, anchor='w',
                           text='1..1000', value=1000, variable=obergrenze)
radiobutton3.place(x=5, y=55, width=80, height=20)
radiobutton1.select()
# Spielbutton
buttonNeueZahl = Button(master=frameSpiel, text='neue Ratezahl', command=buttonNeueZahlClick)
buttonNeueZahl.place(x=235, y=30, width=100, height=20)
labelSpielInfo1 = Label(master=frameSpiel, bg="#FFCFC9", anchor='w', text='WÃ¤hle einen Bereich,')
labelSpielInfo1.place(x=105, y=5, width=120, height=20)
labelSpielInfo2 = Label(master=frameSpiel, bg="#FFCFC9", anchor='w', text='drÃ¼cke dann auf')
labelSpielInfo2.place(x=105, y=30, width=120, height=20)
labelSpielInfo3 = Label(master=frameSpiel, bg="#FFCFC9", anchor='w', text='[neue Ratezahl].')
labelSpielInfo3.place(x=105, y=55, width=120, height=20)
# Rateversuche
labelVersuche = Label(master=frameRaten, anchor='w', text=str(zaehler.getStand()) + '. Rateversuch',
                      bg="#D5E88F")
labelVersuche.place(x=5, y=5, width=80, height=20)
entryZahl = Entry(master=frameRaten, bg='white', text='', font=("Arial", 16))
entryZahl.bind('<Return>', buttonRatenClick)
entryZahl.place(x=5, y=35, width=80, height=30)
labelRueckmeldung = Label(master=frameRaten, text='', bg="#D5E88F", font=("Arial", 16), anchor='w')
labelRueckmeldung.place(x=105, y=40, width=150, height=30)
labelInfo = Label(master=frameRaten, bg="#D5E88F", anchor='w', text='Gib eine Zahl ein und drÃ¼cke dann die Return-Taste.')
labelInfo.place(x=5, y=80, width=330, height=20)
buttonEndeSpiel = Button(master=frameRaten, text='beenden', command=buttonBeendenClick)
buttonEndeSpiel.place(x=235, y=45, width=100, height=20)
# Aktivierung des Fensters
tkFenster.mainloop()
