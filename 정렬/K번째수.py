def solution(array, commands):
	list = []
	for i, j, k in commands:
		new_array=array[i-1:j]
		new_array.sort()
		list.append(new_array[k-1])
	return list