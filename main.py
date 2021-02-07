
import random
from bubble_sort import *
from heap_sort import *
from merge_sort import *
from quick_sort import *
from selection_sort import *

def generateArray(elements):
    array = []
    for i in range(elements):
        array.append(random.randint(0,100))
    return array


if __name__ == '__main__':

    ## Quicksort
    print('Quicksort:')
    array = generateArray(20)
    print(array)
    quick_sort(array,0,len(array)-1)
    print(array)

    ## Mergesort
    print('Mergesort:')
    array = generateArray(20)
    print(array)
    array = merge_sort(array)
    print(array)

    ## Selectionsort
    print('Selectionsort:')
    array = generateArray(20)
    print(array)
    selection_sort(array)
    print(array)

    ## Heapsort
    print('Selectionsort:')
    array = generateArray(20)
    print(array)
    heap_sort(array)
    print(array)

    ## Bubblesort
    print('Selectionsort:')
    array = generateArray(20)
    print(array)
    bubble_sort(array)
    print(array)








