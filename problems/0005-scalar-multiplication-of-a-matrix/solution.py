def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	result = []

	for row in matrix:
		temp_row = []
		for i in range(len(row)):
			temp_row.append(row[i] * scalar)
		result.append(temp_row)

	return result

	pass