import random


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_inplace(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


def insertion_sort_inplace(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


def mergesort(list1):
    if len(list1) == 1:     # Base case: list is already sorted
        return list1
    else:
        mid = len(list1) // 2
        left = list1[:mid]
        right = list1[mid:]

        left = mergesort(left)   # Recursive call to sort left half
        right = mergesort(right)  # Recursive call to sort right half

        # Merge the two sorted halves
        i = 0   # Index for left list
        j = 0   # Index for right list
        merged_list = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1

        # Append any remaining elements from left or right lists
        while i < len(left):
            merged_list.append(left[i])
            i += 1
        while j < len(right):
            merged_list.append(right[j])
            j += 1

        return merged_list


def merge_sort_in_place(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the left and right halves in place
        merge_sort_in_place(left_half)
        merge_sort_in_place(right_half)

        # Merge the two sorted halves in place
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[-1]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


def quicksort_in_place(lst, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low < high:
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        pivot = i + 1
        quicksort_in_place(lst, low, pivot - 1)
        quicksort_in_place(lst, pivot + 1, high)
    return lst


def test_sort_algorithm(sort_func):
    random_list = [random.randint(0, 100) for _ in range(10)]
    sorted_list = list(range(10))
    reverse_sorted_list = list(range(10, 0, -1))
    duplicate_list = [random.randint(0, 5) for _ in range(10)]
    single_element_list = [5]
    large_list = [random.randint(0, 1000000) for _ in range(10)]
    small_list = [random.randint(-1000, 0) for _ in range(10)]
    repeated_list = [random.choice(['a', 'b', 'c']) for _ in range(10)]
    negative_list = [random.randint(-100, 100) for _ in range(10)]

    test_cases = [random_list, sorted_list, reverse_sorted_list, duplicate_list,
                  single_element_list, large_list, small_list, repeated_list, negative_list]

    print(f"Testing {sort_func}")
    for lst in test_cases:
        # print(f"Testing with list: {lst}")
        # print(f"Before sorting: {lst}")
        sorted_lst = sort_func(lst)
        # print(f"After sorting: {sorted_lst}")

        if sorted_lst == sorted(lst):
            print("Test passed! List is correctly sorted.")
        else:
            print("Test failed! List is not correctly sorted.")

    print("-----------------------------")


def hand_simulation(sort_func, lst):
    sorted_lst = lst.copy()
    for i in range(len(sorted_lst)):
        for j in range(i, len(sorted_lst)):
            if sorted_lst[i] > sorted_lst[j]:
                sorted_lst[i], sorted_lst[j] = sorted_lst[j], sorted_lst[i]
                print(f"Step {i + 1}: {sorted_lst}")
    return sorted_lst


def hand_simulation2(sort_func, lst):
    print("Starting list: ", lst)
    print("Sorting method: ", sort_func.__name__)

    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            print("Comparing", lst[j], "and", lst[j + 1])
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print("Swapping", lst[j + 1], "and", lst[j])
        print("List after pass", i + 1, ":", lst)

    print("Sorted list: ", lst)


test_sort_algorithm(bubble_sort)
test_sort_algorithm(bubble_sort_inplace)
test_sort_algorithm(insertion_sort)
test_sort_algorithm(insertion_sort_inplace)
test_sort_algorithm(mergesort)
test_sort_algorithm(merge_sort_in_place)
test_sort_algorithm(quicksort)
test_sort_algorithm(quicksort_in_place)

lst1 = [4, 3, 7, 6, 5, 8, 9, 1]
hand_simulation(bubble_sort, lst1)
# hand_simulation2(bubble_sort, lst1)