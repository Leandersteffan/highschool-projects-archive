class Solution:
    def romanToInt(self, s: str) -> int:
        originalListe = []
        result = 0
        for i in range(len(s)):
            if s[i] == 'I':
                originalListe.append(1)
            elif s[i] == 'V':
                originalListe.append(5)
            elif s[i] == 'X':
                originalListe.append(10)
            elif s[i] == 'L':
                originalListe.append(50)
            elif s[i] == 'C':
                originalListe.append(100)
            elif s[i] == 'D':
                originalListe.append(500)
            elif s[i] == 'M':
                originalListe.append(1000)
        for i in range(len(originalListe)):
                result = result + originalListe[i]
                if i > 0:
                    if originalListe[i - 1] < originalListe[i]:
                        result = result - 2 * originalListe[i - 1]               
        return result
