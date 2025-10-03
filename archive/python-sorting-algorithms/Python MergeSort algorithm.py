'''die Liste wird in immer kleinere Teile geteilt und fügt sich dann von ganz
unten zusammen und Sortiert sich langsam in immer größere listen bis sie in
es wieder zu nur einer Liste geschaft hat.
yt: https://www.youtube.com/watch?v=Nso25TkBsYI&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=4'''
'fast 0(n log n)'
def merge_sort(A):
    return merge_sort2(A, 0, len(A) - 1)

def merge_sort2(A, first,last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle + 1, last)
        return merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

print(merge_sort([1,4,6,2,6,9,2]))
