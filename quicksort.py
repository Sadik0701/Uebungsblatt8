from typing import List


def partition (input_array: List[int], low: int, high: int):
    pivot = input_array[low] #-1
    leftwall = low #0

    for i in range(low + 1, high ): #1-3
        if (input_array[i] < pivot):
            temp = input_array[i]
            input_array[i] = input_array[leftwall]
            input_array[leftwall] = temp
            leftwall = leftwall + 1

    temp2 = pivot
    pivot = input_array[leftwall]
    input_array[leftwall] = temp2

    return leftwall
def quicksort(input_array: List[int], low: int, high: int):
    #[-1, 3, 2, 1]
    if (low < high):
        pivot_location = partition(input_array, low, high)
        quicksort(input_array, low, pivot_location)
        quicksort(input_array, pivot_location + 1, high)



