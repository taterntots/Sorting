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
    merged_arr2 = []
    print(elements)
    for a in arrA:
        for b in arrB:
            if arrA[a] <= arrB[b]:
                print('yes!')
                merged_arr2.append(arr[a])
                print(merged_arr2)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # (base case) If the array is empty or length 1, return
    if len(arr) <= 1:
        return arr

    # Split the arrays into half
    arr1 = []
    arr2 = []

    # Sort each half
    arr1 = [0,1,2,3,6]
    arr2 = [4,5,7,8,9]
    # Merge them back together
    # Compare the first values of each array, add smaller of the 2 to result
    merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
def timsort( arr ):

    return arr

# ----------------------------------------------------------
# ------------------- Data to play with --------------------
# ----------------------------------------------------------
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
arrA = [1, 2, 4, 5, 8]
arrB = [3, 6, 7, 9, 10]

print(f'Original =', arr)
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortQuick =', quick_sort(arr))
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortMerge =', merge_sort(arr))
print(f'MergeTwo =', merge(arrA, arrB))