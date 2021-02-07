

def heapify(array, index, amount):

	largest = index
	left = index*2 + 1
	right = index*2 + 2

	if left < amount and array[left] > array[largest]:
		largest = left
	if right < amount and array[right] > array[largest]:
		largest = right
	if largest != index:
		array[index], array[largest] = array[largest], array[index]
		heapify(array, largest, amount)
	return array

	
def build_heap(array):

	i = int((len(array) / 2) - 1)

	while i >= 0:
		heapify(array, i, len(array))
		i = i - 1
	return array

def heap_sort(array):
	array = build_heap(array)

	i = len(array) - 1

	while i > 0:
		array[0], array[i] = array[i], array[0]
		heapify(array, 0, i)
		i = i - 1
	return array



