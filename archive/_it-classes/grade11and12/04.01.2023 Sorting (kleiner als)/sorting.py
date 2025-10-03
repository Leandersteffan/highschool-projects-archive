def list_insert(liste):     # wenn man eine Hilfsliste nutzt
    neueListe = [liste[0]]
    for i in range(1, len(liste)):
        for j in range(len(neueListe)):
            if liste[i] < neueListe[j]:
                if j == 0:
                    neueListe = [liste[i]] + neueListe
                else:
                    neueListe = neueListe[:j] + [liste[i]] + neueListe[j:]
                break
            elif j == len(neueListe) - 1:
                neueListe = neueListe + [liste[i]]
                break
    return neueListe

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1):
        for j in range(len(unsorted_list)-1-i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list


liste = [96, 83, 97, 87, 10, 12, 44, 4, 39, 63, 8, 1, 65, 73, 21, 77, 82, 11, 9, 36, 26, 79, 72, 5, 91, 6, 14, 62, 81, 25, 27, 17, 80, 58, 24, 50, 66, 85, 93, 34, 15, 41, 94, 56, 89, 22, 16, 19, 32, 23, 71, 59, 60, 67, 3, 78, 20, 75, 55, 46, 84, 18, 31, 43, 49, 38, 45, 57, 74, 99, 68, 0, 64, 92, 53, 70, 35, 76, 29, 48, 40, 51, 33, 37, 28, 47, 52, 42, 90, 7, 13, 54, 69, 98, 86, 2, 61, 88, 30, 100, 95, 32]
print(list_insert(liste))
