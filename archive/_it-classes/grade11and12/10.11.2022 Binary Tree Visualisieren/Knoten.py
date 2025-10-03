class Knoten:
    def __init__(self, wert, links=None, rechts=None):
        self.wert = wert
        self.links = links
        self.rechts = rechts
        self.max_depth = self.maxDepth(self)
        global aeste
        aeste = []

    def __str__(self):
        rechts_string = "None"
        links_string = "None"
        if self.links != None:
            links_string = self.links.__str__()
        if self.rechts != None:
            rechts_string = self.rechts.__str__()
        return f"|[Wert: {self.wert}, Wert links: {links_string}, Wert rechts: {rechts_string}]|"

    def maxDepth(self, root):
        # Null node has 0 depth.
        if root == None:
            return 0

        # Get the depth of the left and right subtree
        # using recursion.
        leftDepth = self.maxDepth(root.links)
        rightDepth = self.maxDepth(root.rechts)

        # Choose the larger one and add the root to it.
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

    def maxDepth_aktualisieren(self):
        self.max_depth = self.maxDepth(self)

    def aeste_auslesen(self):
        self.aeste_erarbeiten()
        return aeste

    def aeste_erarbeiten(self, liste=[]):
        liste.append(self.wert)
        if not self.links and not self.rechts:
            aeste.append(liste)
        if self.links:
            self.links.aeste_erarbeiten(liste[:])
        if self.rechts:
            self.rechts.aeste_erarbeiten(liste[:])

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

    def insert(self, wert):
        if wert > self.wert and self.rechts:
            self.rechts.insert(wert)
        if wert > self.wert and not self.rechts:
            self.rechts = Knoten(wert)

        if wert < self.wert and self.links:
            self.links.insert(wert)
        if wert < self.wert and not self.links:
            self.links = Knoten(wert)

    def insertliste(self, liste):
        for knoten_wert in liste:
            self.insert(knoten_wert)


'''root = Knoten(50, Knoten(20, Knoten(13, Knoten(7)), Knoten(28)), Knoten(90, Knoten(60, rechts=Knoten(70)), Knoten(111, rechts=Knoten(130, Knoten(127)))))
print(root.aeste_auslesen())'''
'''print(root)
print(root.maxDepth(root))
print(root.max_depth)'''
# root.print_inorder()
# root.print_postorder()
