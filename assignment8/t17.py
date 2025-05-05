def sort_matrix_by_row_sum(matrix):
     return sorted(matrix, key=lambda row: sum(row))
 
 # Example 1
 matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
 sorted_matrix1 = sort_matrix_by_row_sum(matrix1)
 print("Sorted Matrix 1:", sorted_matrix1)
 
 # Example 2
 matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
 sorted_matrix2 = sort_matrix_by_row_sum(matrix2)
 print("Sorted Matrix 2:", sorted_matrix2)