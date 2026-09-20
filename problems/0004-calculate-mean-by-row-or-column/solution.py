def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []

	if mode == 'row':
		for row in matrix:
			row_sum = 0
			row_len = len(row)
			for i in range(row_len):
				row_sum += row[i]
			row_mean = row_sum/row_len
			means.append(row_mean)

	rows_amt = len(matrix)
	cols_amt = len(matrix[0])

	if mode == 'column':
		for i in range(cols_amt): # loop over each column
			col_sum = 0
			for j in range(rows_amt): # loop over each row
				col_sum += matrix[j][i]
			col_mean = col_sum/rows_amt
			means.append(col_mean)

	return means