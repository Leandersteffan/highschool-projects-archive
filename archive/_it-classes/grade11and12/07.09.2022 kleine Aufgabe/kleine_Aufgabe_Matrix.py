class Beispiel_1:
    def __init__(self):
        self.matrix = [[0, 1, 2, 1],
                       [1, 2, 0, 1],
                       [0, 2, 1, 0],
                       [0, 2, 0, 1]]

    def eins_to_zwei(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    self.matrix[i][j] = 2
        self.ausgabe(self.matrix)

    def zwei_to_eins(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 2:
                    self.matrix[i][j] = 1
        self.ausgabe(self.matrix)

    def x_to_y(self, ersetzen, gewollt):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == ersetzen:   # Vergleichsoperator
                    self.matrix[i][j] = gewollt     # Wertzuweisungsoperator
        self.ausgabe(self.matrix)

    def ausgabe(self, matrix):
        for i in range(len(matrix)):
            s = ''
            for j in range(len(matrix[i])):
                s = s + str(matrix[i][j]) + ' '
            print(s)

modell = Beispiel_1()
modell.x_to_y(0, 4)
