import random

def merge(sub1,sub2):

	array = []
	i,j = 0,0

	while i < len(sub1) and j < len(sub2):
		if sub1[i] >= sub2[j]:
			array.append(sub2[j])
			j = j + 1
		elif sub1[i] < sub2[j]:
			array.append(sub1[i])
			i = i + 1	
	if j > i:
		array = array + sub1[i:]
	elif i > j:
		array = array + sub2[j:]

	return array


def merge_sort(array):

	if len(array) < 2:
		return array
	else:
		sub1 = merge_sort(array[:int(len(array)/2)])
		sub2 = merge_sort(array[int(len(array)/2):])

		array = merge(sub1,sub2)
	return array



