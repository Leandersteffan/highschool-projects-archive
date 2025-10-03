from tkinter import *

'''    def __init__(self, master=None):
        Frame.__init__(self,master)
        '''   # Einfacher, ohne Anpassung

class ButtonNeu(Frame):
    def __init__(self, master=None, fwidth=100, fheight=100):
        Frame.__init__(self, master, width=fwidth, height=fheight, borderwidth=5, relief='raised')  # Masterobjekt ist das dem es zugeordnet ist
        self.pack_propagate(False)
        self.b = Button(self, text="Klicke", command=self.klick)
        self.b.pack()
        self.l=Label(self,text="0")
        self.l.pack()
        self.zaehler = 0
        self.master=master
        

    def klick(self):
        self.zaehler += 1
        print("Button wurde {} mal geklickt.".format(self.zaehler))
        self.l.configure(text=str(self.zaehler))
        self.master.geometry(str(200*self.zaehler)+"x"+str(200*self.zaehler))

class Gui:
    def __init__(self):
        self.root = Tk()
        self.button_neu1 = ButtonNeu(self.root)
        self.button_neu1.pack()
        self.button_neu2 = ButtonNeu(self.root)
        self.button_neu2.pack()
        self.button_neu3 = ButtonNeu(self.root)
        self.button_neu3.pack()
    
        self.root.mainloop()

g=Gui()
