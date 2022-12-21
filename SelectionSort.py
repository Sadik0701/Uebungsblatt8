from typing import List

def selectionsort(input_array: List[int]):
    """

    :param input_array: array of integers can also be empty
    :return: None
    """
    n = len(input_array)
    for i in range(n):
        i_min = i
        for j in range(i+1, n):
            if input_array[j] < input_array[i_min]:
                i_min = j
        if i_min != i:
            temp = input_array[i_min]
            input_array[i_min] = input_array[i]
            input_array[i] = temp
