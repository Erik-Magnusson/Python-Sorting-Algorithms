import random

def selection_sort(array):
	for i in range(len(array) - 1):

		least = i
		
		for j in range(i+1, len(array)):

			if array[j] < array[least]:
				least = j
				
		if i != least:
			tmp = array[least]
			array[least] = array[i]
			array[i] = tmp
			
	return array









