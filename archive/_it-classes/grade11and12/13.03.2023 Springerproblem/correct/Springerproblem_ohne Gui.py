class Springerproblem:
    def __init__(self):
        self.feld = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        """self.feld = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]"""
        """self.feld = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]"""
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
        self.weg = []
        self.weg_correct = []

    def lösen(self, coord): #coord == [x, y]
        self.trys += 1
        self.weg.append(coord)
        self.feld[coord[1]][coord[0]] += 1
        if self.check():  # Abbruchkriterium
            self.weg_correct.append(self.weg)
            return self.weg
        else:
            möglichkeiten = self.heuristic_sort_moves(coord)
            for möglichkeit in möglichkeiten:
                if self.legal_move(möglichkeit):
                    "self.imprint(weg)"
                    self.lösen(möglichkeit)
            if not self.check():    #Abbruchkriterium
                self.feld[self.weg[-1][1]][self.weg[-1][0]] -= 1
                self.weg.pop(-1)     #letzten rückgängig
                return None
        return self.weg

    def check(self):
        for i in range(len(self.feld)):
            for j in range(len(self.feld[i])):
                if self.feld[i][j] < 1:
                    return False
        return True

    def mögliche_züge(self, coord):
        möglichkeiten = [[coord[0] + 2, coord[1] - 1], [coord[0] + 2, coord[1] + 1], [coord[0] + 1, coord[1] - 2], [coord[0] - 1, coord[1] - 2],
                         [coord[0] - 2, coord[1] + 1], [coord[0] - 2, coord[1] - 1], [coord[0] - 1, coord[1] + 2], [coord[0] + 1, coord[1] + 2]]
        x = -1
        while x <= len(möglichkeiten) - 2:
            x += 1
            if not self.legal_move(möglichkeiten[x]):
                möglichkeiten.pop(x)
                x -= 1
        return möglichkeiten

    def heuristic_sort_moves(self, coord):
        possible_moves = self.mögliche_züge(coord)
        sorted_moves = sorted(possible_moves, key=lambda move: len(self.mögliche_züge(move)))
        return sorted_moves

    def möglichkeiten_ranken(self, möglichkeiten):
        optionen = []
        for möglichkeit in möglichkeiten:
            if self.legal_move(möglichkeit):
                count = 0
                moves = [[möglichkeit[0] + 2, möglichkeit[1] - 1], [möglichkeit[0] + 2, möglichkeit[1] + 1], [möglichkeit[0] + 1, möglichkeit[1] - 2],
                         [möglichkeit[0] - 1, möglichkeit[1] - 2], [möglichkeit[0] - 2, möglichkeit[1] + 1], [möglichkeit[0] - 2, möglichkeit[1] - 1],
                         [möglichkeit[0] - 1, möglichkeit[1] + 2], [möglichkeit[0] + 1, möglichkeit[1] + 2]]
                for move in moves:
                    if self.legal_move(move):
                        count += 1
                optionen.append([count, möglichkeit])
        optionen.sort()
        out = []
        for op in optionen:
            if op[0] > 0:
                out.append(op[1])
        return out


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
test.lösen([0, 0])
n = test.weg
print(len(n), test.trys, n, test.weg_correct)
#print(test.möglichkeiten_ranken([[3, 1], [3, 3], [2, 0], [0, 0], [-1, 3], [-1, 1], [0, 4], [2, 4]]))

