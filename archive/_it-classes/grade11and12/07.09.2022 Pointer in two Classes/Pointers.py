class Eins:
    def __init__(self, gui_object):
        self.gui = gui_object

        self.gui.eins_geben(11)


class Gui:
    def __init__(self):
        self.modell = Eins(self)

    def eins_geben(self, x):
        print(x)



start0 = Gui()
start0.eins_geben(153)
