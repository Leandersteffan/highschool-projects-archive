
class Knoten:
    def __init__(self, wert, links, rechts):
        global aeste
        self.wert = wert
        self.links = links
        self.rechts = rechts
        

##    def __str__(self):
##        unterbaeume=""
##        if self.links==None:
##            unterbaeume+="Links: None"+"\n"
##        else:
##            unterbaeume+="Links: "+str(self.links.wert)+"\n"
##        
##        if self.rechts==None:
##            unterbaeume+="Rechts: None"
##        else:
##            unterbaeume+="Rechts: "+str(self.rechts.wert)+"\n"
##        return ("Wert: %i\n%s " %(self.wert, unterbaeume))       

##    def preorder(self, liste):
##        print(self.wert)
##        if self.links:
##            self.links.preorder()
##        if self.rechts:
##            self.rechts.preorder()

    def aeste_auslesen(self, liste):
        liste.append(self.wert)
        if not self.links and not self.rechts:
            aeste.append(liste)
            #print("Knoten: ", self.wert, " ", liste, " ", aeste)
        print(self.wert)
        
        if self.links:
            self.links.aeste_auslesen(liste)
        if self.rechts:
            self.rechts.aeste_auslesen(liste)

    def aeste_auslesen_mit_Listenkopie(self, liste):
        liste.append(self.wert)
        if not self.links and not self.rechts:
            aeste.append(liste)
            #print("Knoten: ", self.wert, " ", liste, " ", aeste)
        print(self.wert)
        
        if self.links:
            self.links.aeste_auslesen_mit_Listenkopie(liste[:])
        if self.rechts:
            self.rechts.aeste_auslesen_mit_Listenkopie(liste[:])
        
    def inorder(self):
        if self.links:
            self.links.inorder()
        print(self.wert)
        if self.rechts:
            self.rechts.inorder()

    def postorder(self):
        if self.links:
            self.links.postorder()
        if self.rechts:
            self.rechts.postorder()
        print(self.wert)
        
    def insert(self, wert):
        if self.wert == wert:
            pass
        if wert > self.wert and self.rechts:
            self.rechts.insert(wert)
        if wert > self.wert and not self.rechts:
            self.rechts = Knoten(wert, None, None)
        if wert < self.wert and self.links:
            self.links.insert(wert)
        if wert < self.wert and not self.links:
            self.links = Knoten(wert, None, None)
            
    def insertliste(self, liste):
        for i in liste:
            self.insert(i)

    def suche (self, wert):
        if self.wert == wert:
            print("gefunden: ", self.wert)
            return self
        if wert > self.wert and self.rechts:
            return self.rechts.suche(wert)    
        if wert > self.wert and not self.rechts:
            return None
        if wert < self.wert and self.links:
            return self.links.suche(wert)
        if wert < self.wert and not self.links:
            return None
        


#Hauptprogramm



#wurzel=Knoten(50,Knoten(30,None,Knoten(35,None,None)),Knoten(70,Knoten(65,Knoten(60, None,None),None),None))

wertliste = []
wurzel = Knoten(50, None, None)
wert = int(input("wert: "))
while wert:
    wertliste.append(wert)
    wert = int(input("wert: "))

wurzel.insertliste(wertliste)


wert = int(input("wertgesucht: "))
knotengesucht = wurzel.suche(wert)
print("suche: ", knotengesucht, knotengesucht.wert)



