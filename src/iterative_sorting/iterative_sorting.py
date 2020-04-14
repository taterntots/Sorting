def insertion_sort(arr): 
  
    # loop through elements
    for i in range(1, len(arr)):

       #element to be compared
       current = arr[i]

       #comparing the current element with the sorted portion and swapping
       while i > 0 and arr[i-1] > current:
            arr[i] = arr[i-1]
            i = i-1
            arr[i] = current

    return arr

# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):

    # Loop through n-1 elements
    for i in range(len(arr)):

        # Start by assuming the first element is the smallest
        current_index = i
        smallest_index = current_index

        # Using j, we can loop throgh the remaining elements
        for j in range(i+1, len(arr)):

            # Find next smallest element and update smallest_index if j is lower
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap the found minimum element with smallest_index found in the above loop
        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
             
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    # Loop through the array
    for i in range(len(arr)):

        # Compare each element to its neighbor
        for j in range(len(arr)-1):
            # current_value = arr[j]
            # neighbor_value = arr[j+1]
            # print(j)

            # If elements in wrong position (relative to each other), swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        # We go through the list as many times as there are elements

    return arr


arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]

print(f'Original =', arr)
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortInsert =', insertion_sort(arr))
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortSelect =', selection_sort(arr))
arr = [5, 1, 7, 8, 2, 95, 79, 4, 11, 74, 34, 41]
print(f'SortBubble =', bubble_sort(arr))

# for i in range(0, len(arr)):
#     print(arr[i])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr