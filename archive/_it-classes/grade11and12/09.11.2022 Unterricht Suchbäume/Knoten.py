class Knoten:
    def __init__(self, wert, links=None, rechts=None):
        self.wert = wert
        self.links = links
        self.rechts = rechts

    def __str__(self):
        rechts_string = "None"
        links_string = "None"
        if self.links != None:
            links_string = self.links.__str__()
        if self.rechts != None:
            rechts_string = self.rechts.__str__()
        return f"|[Wert: {self.wert}, Wert links: {links_string}, Wert rechts: {rechts_string}]|"

    def print_preorder(self):
        print(self.wert)
        if self.links:
            self.links.print_preorder()
        if self.rechts:
            self.rechts.print_preorder()

    def return_preorder(self, liste=[]):
        liste.append(self.wert)
        if self.links:
            liste.append(self.links.return_preorder(liste))
        if self.rechts:
            liste.append(self.rechts.return_preorder(liste))
        return liste

    def print_inorder(self):
        if self.links:
            self.links.print_inorder()
        print(self.wert)
        if self.rechts:
            self.rechts.print_inorder()

    def return_inorder(self, liste=[]):
        if self.links:
            liste.append(self.links.return_inorder(liste))
        liste.append(self.wert)
        if self.rechts:
            liste.append(self.rechts.return_inorder(liste))
        return liste

    def print_postorder(self):
        if self.links:
            self.links.print_postorder()
        if self.rechts:
            self.rechts.print_postorder()
        print(self.wert)

    def return_postorder(self, liste=[]):
        if self.links:
            liste.append(self.links.return_postorder(liste))
        if self.rechts:
            liste.append(self.rechts.return_postorder(liste))
        liste.append(self.wert)
        return liste


root = Knoten(50, Knoten(20, Knoten(13, Knoten(7)), Knoten(28)), Knoten(90, Knoten(60, rechts=Knoten(70)), Knoten(111, rechts=Knoten(130, Knoten(127)))))
print(root)
root.print_preorder()
print(root.return_preorder())
#root.print_inorder()
#root.print_postorder()
