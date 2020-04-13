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

       #print(arr)

    return arr

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # Start with current index = 0
        cur_index = arr[i]
        smallest_index = cur_index
        # print(smallest_index)

        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code) 
        if cur_index < smallest_index:
            # print(arr[smallest_index])
            # Swap the element at current index with the smallest element found in the above loop
            cur_index == smallest_index



        # Start with current index = 0
        # For all indices EXCEPT the last index:
            # Loop through elements on right-hand-side of current index and find the smallest element
            # Swap the element at current index with the smallest element found in above loop
             
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    # Loop through your array
    for i in range(len(arr)-1):

        # Compare each element to its neighbor
        # current_value = arr[j]
        # neighbor_value = arr[j+1]

        # If elements in wrong position (relative to each other), swap them
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    # We go through the list as many times as there are elements

    return arr


arr = [5, 1, 7, 8, 2, 4, 11, 74, 34, 41]

print(f'Original =', arr)
arr = [5, 1, 7, 8, 2, 4, 11, 74, 34, 41]
print(f'SortInsert =', insertion_sort(arr))
arr = [5, 1, 7, 8, 2, 4, 11, 74, 34, 41]
print(f'SortSelect =', selection_sort(arr))
arr = [5, 1, 7, 8, 2, 4, 11, 74, 34, 41]
print(f'SortBubble =', bubble_sort(arr))

# for i in range(0, len(arr)):
#     print(arr[i])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr