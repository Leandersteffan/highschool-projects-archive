'''bei der Insertion methode geht man durch eine Liste und beim aktuellen
schaut man ob das linke glied größer ist. Wenn ja tauschen diese Plätze
und das geht so lange weiter bis das linke Glied nicht mehr größer ist
oder man ganz links ist.
Die zweite Methode ist etwas schneller da sie sich den aktuellen Wert merkt
und nur mit den Wert durch das Array geht ohne zu tauschen sonder immer nur
den linken Wert unter sich einsetzt. wenn es am finalen Punkt ist dann setzt
sich der Wert einfach ein.
1. [1,2,5,8,9,3] --> [1,2,5,6,3,9] --> [1,2,5,3,6,9] --> [1,2,3,5,6,9]
2. [1,2,5,8,9,3] --> [1,2,5,6,9,9] --> [1,2,5,6,6,9] --> [1,2,3,5,6,9]
yt: https://www.youtube.com/watch?v=Nkw6Jg_Gi4w&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq'''


def sorting(A):
    for i in range(len(A)):
        for j in range(i-1, 0, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return A

def sorting_faster(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
    return A

print(sorting([1,4,6,2,6,9,2]))
print(sorting_faster([1,4,6,2,6,9,2]))
