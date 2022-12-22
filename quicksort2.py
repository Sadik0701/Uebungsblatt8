from typing import List
def quicksort(input_array, left, right):
    if (left < right):
        pivot_location = partition(input_array,left, right)
        quicksort(input_array, left, pivot_location-1)
        quicksort(input_array, pivot_location + 1, right)



def partition (input_array, left: int, right: int):
    i = left
    j = right-1
    pivot =  input_array[right]

    while i<j:
        while i<j and input_array[i] <= pivot:
            i+=1
        while j>i and input_array[j]>pivot:
            j-=1
        if input_array[i]>input_array[j]:
            temp = input_array[i]
            input_array[i] = input_array[j]
            input_array[j] = temp
    if input_array[i]>pivot:
        temp = input_array[i]
        input_array[i] = input_array[right]
        input_array[right] = temp
    else:
        i = right
    return i