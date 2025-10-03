from tkinter import *
class Malprogramm(object):
    def __init__(self):

        self.hauptfenster = Tk()
        self.hauptfenster.title("Paint")
        self.hauptfenster.geometry("1080x720")
        self.hauptfenster_hintergrund="lightgreen"
        self.durchmesser=1

        self.hauptfenster.configure(background=self.hauptfenster_hintergrund)

        self.farbe="#FFFFFF"

        #Label
        #self.hauptfenster_L = Label(self.hauptfenster,width=15,text="Werkzeuge")
        #self.hauptfenster_L.place(x=850,y=2750)
        
        #Canvas
        self.malFenster_CNV = Canvas(self.hauptfenster, width=800, height=680, bg="white")
        self.malFenster_CNV.place(x=20, y=20)
        
        self.vorschauFenster_CNV=Canvas(self.hauptfenster,width=50,height=50,bg=self.farbe)
        self.vorschauFenster_CNV.place(x=840, y=35)
        
        #Scale
        self.skalarot_SCL = Scale(self.hauptfenster, width=15, bg="red", activebackground="red",
                                  showvalue=10, from_=0, to=255, command=self.setFarbe)
        self.skalarot_SCL.place(x=900, y=35)
        
        self.skalagruen_SCL = Scale(self.hauptfenster, width=15, bg="green", activebackground="green",
                                  showvalue=10, from_=0, to=255, command=self.setFarbe)
        self.skalagruen_SCL.place(x=945, y=35)
        
        self.skalablau_SCL = Scale(self.hauptfenster, width=15, bg="blue", activebackground="blue",
                                  showvalue=10, from_=0, to=255, command=self.setFarbe)
        self.skalablau_SCL.place(x=990, y=35)

        self.skalaDurchmesser_SCL=Scale(self.hauptfenster, label="Durchmesser",orient=HORIZONTAL,showvalue=10,bg=self.hauptfenster_hintergrund,
                                     activebackground=self.hauptfenster_hintergrund,width=15,length=190,from_=1,to=200,command=self.setDurchmesser)
        self.skalaDurchmesser_SCL.place(x=840, y=150)

        #Button
        self.ende_BTN=Button(self.hauptfenster,text="Beenden",bg='red',width=10,height=2,command=self.ende)
        self.ende_BTN.place(x=900,y=600)

        self.loescheAlles_BTN=Button(self.hauptfenster,text="Löschen",bg='orange',width=10,height=2,command=self.loescheAlles)
        self.loescheAlles_BTN.place(x=900,y=500)

        self.sonne_BTN=Button(self.hauptfenster,text="Sonne",bg='lightgreen',width=10,height=2,command=self.sonne)
        self.sonne_BTN.place(x=950,y=400)

        self.haus_BTN=Button(self.hauptfenster,text="Haus",bg='lightgreen',width=10,height=2,command=self.haus)
        self.haus_BTN.place(x=950,y=350)

        self.bg_BTN=Button(self.hauptfenster,text="Hintergrund",bg='lightgreen',width=10,height=2,command=self.bgaendern)
        self.bg_BTN.place(x=950,y=250)

        self.speichern_BTN=Button(self.hauptfenster,text="Speichern",bg='yellow',width=10,height=2,command=self.speichern)
        self.speichern_BTN.place(x=900,y=650)

        #Radio Button

        self.pinsel=IntVar() #Interer-Variable für Oberflächenelement
        self.radierer_RDO=Radiobutton(self.hauptfenster,text="Radierer",value=1,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.radierer_RDO.place(x=850,y=300)
        self.kreis_RDO=Radiobutton(self.hauptfenster,text="Kreis",value=2,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.kreis_RDO.place(x=850,y=350)
        self.rechteck_RDO=Radiobutton(self.hauptfenster,text="Rechteck",value=3,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.rechteck_RDO.place(x=850,y=325)
        self.dreieck_RDO=Radiobutton(self.hauptfenster,text="Dreieck",value=4,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.dreieck_RDO.place(x=850,y=375)
        self.sonne_RDO=Radiobutton(self.hauptfenster,text="Sonne",value=5,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.sonne_RDO.place(x=850,y=400)
        self.haus_RDO=Radiobutton(self.hauptfenster,text="Haus",value=6,variable=self.pinsel,bg='lightgreen',command=self.spitzenart)
        self.haus_RDO.place(x=850,y=425)
        

        #Event
        #self.malFenster_CNV.bind("<Button-1>", self.malen)
        self.malFenster_CNV.bind("<B1-Motion>", self.malen)



        self.hauptfenster.mainloop()
        
    def setFarbe(self, event):
        self.farbe="#%2x%2x%2x" %(self.skalarot_SCL.get(),self.skalagruen_SCL.get(),self.skalablau_SCL.get())
        self.farbe = self.farbe.replace(" ","0")
        self.vorschauFenster_CNV.configure(bg=self.farbe)

    def setDurchmesser(self, event):
        self.durchmesser=self.skalaDurchmesser_SCL.get()

        

    def ende(self):
        self.hauptfenster.destroy()

    def loescheAlles(self):
        self.malFenster_CNV.create_rectangle(0,0,820,700, fill='white',outline='white')

    def haus(self):
        self.malFenster_CNV.create_line(20,170,20,470,fill='red',width=10)
        self.malFenster_CNV.create_line(20,470,320,470,fill='red',width=10)
        self.malFenster_CNV.create_line(320,470,320,170,fill='red',width=10)
        self.malFenster_CNV.create_line(320,170,20,170,fill='red',width=10)
        self.malFenster_CNV.create_line(20,170,320,470,fill='red',width=10)
        self.malFenster_CNV.create_line(20,470,320,170,fill='red',width=10)
        self.malFenster_CNV.create_line(20,170,170,20,fill='red',width=10)
        self.malFenster_CNV.create_line(170,20,320,170,fill='red',width=10)

    def sonne(self):
        self.malFenster_CNV.create_oval(550,200,650,300,fill='yellow',outline='yellow')
        self.malFenster_CNV.create_line(540,250,440,250,fill='yellow',width=8)
        self.malFenster_CNV.create_line(600,190,600,90,fill='yellow',width=8)
        self.malFenster_CNV.create_line(600,310,600,410,fill='yellow',width=8)
        self.malFenster_CNV.create_line(660,250,760,250,fill='yellow',width=8)

    def malen(self,event):
        if self.pinsel_art==1:
            self.malFenster_CNV.create_oval(event.x-self.durchmesser,event.y-self.durchmesser,event.x+self.durchmesser,event.y+self.durchmesser,fill="white",outline="white")
        if self.pinsel_art==2:
            self.malFenster_CNV.create_oval(event.x-self.durchmesser,event.y-self.durchmesser,event.x+self.durchmesser,event.y+self.durchmesser,fill=self.farbe,outline=self.farbe)
        if self.pinsel_art==3:
            self.malFenster_CNV.create_rectangle(event.x-self.durchmesser,event.y-self.durchmesser,event.x+self.durchmesser,event.y+self.durchmesser,fill=self.farbe,outline=self.farbe)
        if self.pinsel_art==4:
            self.malFenster_CNV.create_polygon(event.x-self.durchmesser,event.y-self.durchmesser,event.x+self.durchmesser,event.y+self.durchmesser,fill=self.farbe,outline=self.farbe)
        #if self.pinsel_art==5:
            #self.malFenster_CNV.create_oval(event.x-50,event.y-50,event.x+50,event.y+50,fill=self.farbe,outline=self.farbe)
            #self.malFenster_CNV.create_line(event.x-60,event.y,event.x-160,event.y,fill=self.farbe,width=8)
            #self.malFenster_CNV.create_line(event.x+60,event.y,event.x+160,event.y,fill=self.farbe,width=8)
            #self.malFenster_CNV.create_line(event.x,event.y-60,event.x,event.y-160,fill=self.farbe,width=8)
            #self.malFenster_CNV.create_line(event.x,event.y+60,event.x,event.y+160,fill=self.farbe,width=8)
        if self.pinsel_art==5:
            self.malFenster_CNV.create_oval(event.x-self.durchmesser,event.y-self.durchmesser,event.x+self.durchmesser,event.y+self.durchmesser,fill=self.farbe,outline=self.farbe)
            self.malFenster_CNV.create_line(event.x-self.durchmesser*1.1,event.y,event.x-self.durchmesser*2.6,event.y,fill=self.farbe,width=8)
            self.malFenster_CNV.create_line(event.x+self.durchmesser*1.1,event.y,event.x+self.durchmesser*2.6,event.y,fill=self.farbe,width=8)
            self.malFenster_CNV.create_line(event.x,event.y-self.durchmesser*1.1,event.x,event.y-self.durchmesser*2.6,fill=self.farbe,width=8)
            self.malFenster_CNV.create_line(event.x,event.y+self.durchmesser*1.1,event.x,event.y+self.durchmesser*2.6,fill=self.farbe,width=8)
        if self.pinsel_art==6:
            self.malFenster_CNV.create_rectangle(event.x-150,event.y-150,event.x+150,event.y+150,outline=self.farbe,width=10)
            self.malFenster_CNV.create_line(event.x-150,event.y-150,event.x+150,event.y+150,fill=self.farbe,width=10)
            self.malFenster_CNV.create_line(event.x-150,event.y+150,event.x+150,event.y-150,fill=self.farbe,width=10)
            self.malFenster_CNV.create_line(event.x-150,event.y-150,event.x,event.y-300,fill=self.farbe,width=10)
            self.malFenster_CNV.create_line(event.x+150,event.y-150,event.x,event.y-300,fill=self.farbe,width=10)
        
    def spitzenart(self):
        self.pinsel_art=self.pinsel.get()
        

    def bgaendern(self):
        self.malFenster_CNV.create_rectangle(0,0,820,700, fill=self.farbe,outline=self.farbe)

    def speichern(self):
        filename = "temporaereDatei.ps"
        self.malFenster_CNV.postscript(file=filename)
        print('gespeichert')
        
male=Malprogramm()
