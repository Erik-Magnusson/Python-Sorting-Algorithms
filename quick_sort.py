
def quick_sort(array,low,high):

	
	i, j = low, high	
	pivot = array[int(low + (high-low)/ 2)]

	while i <= j: 			
		while array[i] < pivot:
			i = i + 1			
		while array[j] > pivot:
			j = j - 1	
		if i <= j: 
			array[i], array[j] = array[j], array[i]
			i = i + 1
			j = j - 1
			
	if low < j:
		quick_sort(array, low, j);
			
	if i < high:
		quick_sort(array, i, high);

	return array






