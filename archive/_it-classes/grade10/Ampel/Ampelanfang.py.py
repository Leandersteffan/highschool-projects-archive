class Ampel(object):
    def __init__(self):
        self.lampeRot = False
        self.lampeGelb = False
        self.lampeGruen = False

    def setLampen(self, startwertLampeRot, startwertLampeGelb, startwertLampeGruen):
        self.lampeRot = startwertLampeRot
        self.lampeGelb = startwertLampeGelb
        self.lampeGruen = startwertLampeGruen

    def schalten(self):
        if (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, False, False):
            self.lampeGelb = True
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, False, True):
            self.lampeGruen = False
            self.lampeGelb = True
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, True, False):
            self.lampeRot = False
            self.lampeGelb = False
            self.lampeGruen = True
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, True, False):
            self.lampeRot = True
            self.lampeGelb= False

        #if (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, False, False):
            #self.lampeRot = False
            #self.lampeGruen = True
        #else:
            #self.lampeRot = True
            #self.lampeGruen = False