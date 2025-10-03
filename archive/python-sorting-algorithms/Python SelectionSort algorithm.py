'''beim SelectionSort wird immer das niedrigste Element der Liste gesucht und
ganz vorne an die Liste gepackt. Darauf folgende Elemente natürlich rechts neben
das zuvor niedrigste Element.
yt: https://www.youtube.com/watch?v=mI3KgJy_d7Y&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=2'''
'Langsam'
def selection_sorting(A):
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
            if minIndex != i:
                A[i], A[minIndex] = A[minIndex], A[i]
    return A

print(selection_sorting([1,4,6,2,6,9,2]))
