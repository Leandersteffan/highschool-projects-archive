class Springerproblem:
    def __init__(self):
        """self.feld = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]"""
        """self.feld = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]"""
        self.feld = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        """self.feld = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]"""
        self.trys = 0

    def lösen(self, coord, weg=[]): #coord == [x, y]
        self.trys += 1
        weg.append(coord)
        self.feld[coord[1]][coord[0]] += 1
        if self.check():  # Abbruchkriterium
            return weg
        else:
            möglichkeiten = self.mögliche_züge(coord)
            for möglichkeit in möglichkeiten:
                if self.legal_move(möglichkeit):
                    "self.imprint(weg)"
                    self.lösen(möglichkeit, weg)
            if not self.check():    #Abbruchkriterium
                self.feld[weg[-1][1]][weg[-1][0]] -= 1
                weg.pop(-1)     #letzten rückgängig
                return None
        return weg

    def check(self):
        for i in range(len(self.feld)):
            for j in range(len(self.feld[i])):
                if self.feld[i][j] < 1:
                    return False
        return True

    def mögliche_züge(self, coord):
        möglichkeiten = [[coord[0] + 2, coord[1] - 1], [coord[0] + 2, coord[1] + 1], [coord[0] + 1, coord[1] - 2], [coord[0] - 1, coord[1] - 2],
                         [coord[0] - 2, coord[1] + 1], [coord[0] - 2, coord[1] - 1], [coord[0] - 1, coord[1] + 2], [coord[0] + 1, coord[1] + 2]]
        return möglichkeiten

    def legal_move(self, coord):
        if 0 <= coord[0] < len(self.feld[0]):
            if 0 <= coord[1] < len(self.feld):
                if self.feld[coord[1]][coord[0]] == 0:
                    return True
        return False

    def imprint(self, weg):
        for row in self.feld:
            out = ""
            for ele in row:
                if ele == 1:
                    out += "# "
                else:
                    out += "- "
            print(out)
        print(weg[-5:], len(weg))
        x = input(":")

test = Springerproblem()
n = test.lösen([0, 0])
print(len(n), test.trys, n, "!")

