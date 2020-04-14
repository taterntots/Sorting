# Quick Sort
def quick_sort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    # Separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # Sort smaller and larger
    # Concatenate smaller + pivot + larger
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # print('-----------------------')
    # print(f'arrA: ', arrA)
    # print(f'arrB: ', arrB)

    i = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del (arrA[0])
            i = i + 1
        else:
            merged_arr[i] = arrB[0]
            del (arrB[0])
            i = i + 1
    if len(arrA) > 0:
        for x in arrA:
            merged_arr[i] = x
            i = i + 1
    elif len(arrB) > 0:
        for x in arrB:
            merged_arr[i] = x
            i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # (base case) If the array is empty or length 1, return
    if len(arr) <= 1:
        return arr

    # Split the array in half
    half = len(arr) // 2
    first_half = merge_sort(arr[:half])
    second_half = merge_sort(arr[half:])
    # print(f'First Half: {first_half}')
    # print(f'Second Half: {second_half}')

    # Merge them back together in order with sorted merge function
    arr = merge(first_half, second_half)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# ----------------------------------------------------------
# ------------------- Data to play with --------------------
# ----------------------------------------------------------
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
arrA = [24, 22, 76, 56, 8]
arrB = [27, 6, 7, 9, 10]

print(f'Original =', arr)
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortQuick =', quick_sort(arr))
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print('----------------------------------------------')
print(f'SortMerge =', merge_sort(arr))
print(f'MergeTwo =', merge(arrA, arrB))
print('----------------------------------------------')