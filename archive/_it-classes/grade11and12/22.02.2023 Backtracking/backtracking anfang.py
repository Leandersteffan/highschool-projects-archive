class Backtracking:
    def __init__(self):
        self.g = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0],
        ]
        self.wege = []

    def findeweg(self, s, e, weg=[]):
        weg.append(s)
        if s == e:
            return weg
        else:
            for i in range(len(self.g[s])):
                if self.g[s][i] == 1 and i not in weg:
                    self.findeweg(i, e, weg)
            if weg[-1] != e:
                weg.pop(-1)
                return None
        return weg

    def findeallewege(self, s, e, weg):
        if s == e:
            self.wege.append(weg[:])
        else:
            for i in range(len(self.g[s])):
                if self.g[s][i] == 1 and i not in weg:
                    weg.append(i)
                    ergebnis = self.findeallewege(i, e, weg)
                    weg.remove(i)



test = Backtracking()
print(test.findeweg(0, 4, [0]))
print(test.wege)
