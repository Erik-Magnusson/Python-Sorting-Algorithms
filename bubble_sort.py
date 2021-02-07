
import random

def bubble_sort(array):

	p = 1

	for i in range(1,len(array)):
		for j in range(0,len(array)-p):
			if array[i] < array[j]:
				array[i],array[j] = array[j], array[i]
	p += 1
			
	return array

