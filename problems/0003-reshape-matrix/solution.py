import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	flat_buffer = []

	for row in a:
		for i in range(len(row)):
			flat_buffer.append(row[i])

	if (new_shape[0] * new_shape[1]) != len(flat_buffer):
		return []

	reshaped_matrix = []

	count = 0
	for i in range(new_shape[0]):
		row_buf = []
		for j in range(new_shape[1]):
			row_buf.append(flat_buffer[count])
			count += 1


		reshaped_matrix.append(row_buf)

	# print(reshaped_matrix)

	return reshaped_matrix