from tkinter import *

class ButtonNeu(Frame):
    def __init__(self, master=None, fwidth=100, fheight=100):
        Frame.__init__(self,master, width=fwidth,height=fheight, borderwidth=5, relief='raised')
        self.pack_propagate(False)
        self.b=Button(self, text="Klicke", command=self.klick)
        self.b.pack()
        self.l=Label(self,text="0")
        self.l.pack()
        self.zaehler = 0
        self.master=master
        

    def klick(self):
        self.zaehler += 1
        print("Button wurde {} mal geklickt.".format(self.zaehler))
        self.l.configure(text=str(self.zaehler))

class EntryNeu(Entry):
    def __init__(self, master):
        print(Entry.__init__(self, master))
        self.bind('<Button-1>', self.enter)
        self.werte=""
        

    def enter(self, event):
        self.werte+=""+self.get()
        print(self.werte)
    
class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400")
    
        self.button_neu1 = ButtonNeu(self.root,fwidth=300, fheight=200)
        self.button_neu1.pack()
        self.button_neu2 = ButtonNeu(self.root)
        self.en=EntryNeu(self.root)
        self.en.pack()
    
        self.root.mainloop()

g=Gui()
