# import timeit

liste = [34, 3, 2, 6, 45, 8]


def insertion_sort(liste):
    for i in range(1, len(liste)):
        temp = liste[i]
        # j = i - 1
        while i - 1 >= 0 and liste[i-1] > temp:
            liste[i] = liste[i-1]
            i -= 1
        liste[i] = temp
    return liste


# print(insertion_sort(liste))


def bubble_sort(list_given):
    n = len(list_given)

    for i in range(n):
        # Flagge beendet die Funktion frühzeitig, wenn alles sortiert wurde
        already_sorted = True

        # Vergleiche aktuelles Item mit aktuellem Nachbarn rechts
        for j in range(n-i-1):
            if list_given[j] > list_given[j+1]:
                # Wenn das aktuelle Element größer ist
                # als das rechte, werden sie getauscht
                list_given[j], list_given[j+1] = list_given[j+1], list_given[j]
                # Es wurden Werte getauscht also muss die
                # Flagge wieder auf False gesetzt werden
                already_sorted = False
        # Wenn nichts sortiert werden musste, wurde Flagge nicht auf False
        # gesetzt also wird Programm hier beendet
        if already_sorted:
            return list_given
    return list_given

def bubble_sort_redo(list_given):
    n = len(list_given)
    for i in range(n - 1):
        for j in range(n-1-i):
            if list_given[j] > list_given[j + 1]:
                list_given[j], list_given[j + 1] = list_given[j + 1], list_given[j]
    return list_given


def rhode_insertion_sort(liste):
    # print(liste)
    # Verschiebe
    sortiert = len(liste)-1
    tmp = liste[0]
    for _ in range(0, sortiert):
        tmp = liste[0]

        # Verschiebe nach links
        for i in range(1, sortiert):
            liste[i-1] = liste[i]

        # Einsortieren
        for j in range(sortiert, len(liste)):
            if tmp <= liste[j]:
                liste[j-1] = tmp
                break
            else:
                liste[j-1] = liste[j]
                liste[j] = tmp
        sortiert -= 1
    return liste


print(rhode_insertion_sort(liste))
print(insertion_sort(liste))
print(bubble_sort(liste))
print(bubble_sort_redo(liste))
# timeit.timeit(lambda: rhode_insertion_sort(liste), number=1)

