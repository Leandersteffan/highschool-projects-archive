from Knoten import Knoten
from tkinter import *


class Gui:
    def __init__(self, root):
        self.hauptfenster = Tk()
        self.hauptfenster.title("Binary Tree")
        self.hauptfenster.geometry("1000x800")
        self.hauptfenster.configure(background="lightgreen")

        self.etagen_l, x = [], 400      # Liste für die x-Achsen-Verschiebungs Distanzen
        while x > 2:
            self.etagen_l.append(x)
            x /= 2
        self.line_y_length = 700 / root.max_depth

        self.canvas = Canvas(self.hauptfenster, height="800", width="1000", background="lightgreen")
        self.canvas.place(x="0", y="0")

        self.draw_tree(root)        # Aufruf der Eigentlichen Zeichnung des Baums

        self.hauptfenster.mainloop()

    def draw_tree(self, root):      # Erster Funktionsaufruf, später kein Teil der Rekursion
        x, y, etage = 500, 5, 0     # Variablen
        self.canvas_L = Label(self.canvas, text=root.wert)
        self.canvas_L.place(x=f"{x - 10}", y=f"{y}")
        if root.links:
            self.draw_links(root.links, x, y, etage)
        if root.rechts:
            self.draw_rechts(root.rechts, x, y, etage)

    def draw_links(self, root, x, y, etage):        # Rekursionsfunktion für die linken Unterbäume
        x, y, etage = x - 10, y + 20, etage + 1     # Coordinaten und Etage Aktualisieren und in ausgangslage bringen
        self.canvas.create_line(x, y, x - self.etagen_l[etage], y + self.line_y_length)
        x, y = x - self.etagen_l[etage], y + self.line_y_length + 2
        self.canvas_L = Label(self.canvas, text=root.wert)
        self.canvas_L.place(x=f"{x - 10}", y=f"{y}")
        if root.links:
            self.draw_links(root.links, x, y, etage)
        if root.rechts:
            self.draw_rechts(root.rechts, x, y, etage)

    def draw_rechts(self, root, x, y, etage):       # Rekursionsfunktion für die rechten Unterbäume
        x, y, etage = x + 10, y + 20, etage + 1
        self.canvas.create_line(x, y, x + self.etagen_l[etage], y + self.line_y_length)
        x, y = x + self.etagen_l[etage], y + self.line_y_length + 2
        self.canvas_L = Label(self.canvas, text=root.wert)
        self.canvas_L.place(x=f"{x - 10}", y=f"{y}")
        if root.links:
            self.draw_links(root.links, x, y, etage)
        if root.rechts:
            self.draw_rechts(root.rechts, x, y, etage)


try:
    werte = eval(input("geben sie die Werte ihres Baumes ein als würden sie eine Liste erstellen \n(Maximale Tiefe = 8, erster Wert=Wurzel, der rest wird preorder aufgebaut): "))
    root = Knoten(werte[0])
    root.insertliste(werte)
    root.maxDepth_aktualisieren()
    if root:
        start = Gui(root)
    else:
        print("No root given!")
except NameError:
    print("No root given!")

'''try:         # Alter Input wo man Knoten einzeln eigeben muss
    root = eval(input("geben sie ihren Baum ein (Maximale Tiefe = 8): root = "))
    'root = Knoten(50, Knoten(20, Knoten(13, Knoten(7)), Knoten(28)), Knoten(90, Knoten(60, rechts=Knoten(70)), Knoten(111, rechts=Knoten(130, Knoten(127)))))'
    if root:
        start = Gui(root)
    else:
        print("No root given!")
except NameError:
    print("No root given!")'''
