import numpy as np

class HungarianAlgorithm:
    
	def min_zero_row(self, zero_mat, mark_zero):
		
		'''
		The function can be splitted into two steps:
		#1 The function is used to find the row which containing the fewest 0.
		#2 Select the zero number on the row, and then marked the element corresponding row and column as False
		'''

		#1 Find the row
		min_row = [99999, -1] #[number of zeros, index]
  
 		# Iterate over each row to find the one with the fewest zeros
		for row_num in range(zero_mat.shape[0]): 
			if np.sum(zero_mat[row_num] == True) > 0 and min_row[0] > np.sum(zero_mat[row_num] == True):
				min_row = [np.sum(zero_mat[row_num] == True), row_num]

		#2 Marked the specific row and column as False
		zero_index = np.where(zero_mat[min_row[1]] == True)[0][0] # Find the index of the first True value
		mark_zero.append((min_row[1], zero_index)) # Add the coordinates of the zero to the marked zeros list
		zero_mat[min_row[1], :] = False # Set the entire row to False
		zero_mat[:, zero_index] = False # Set the entire column to False

	def mark_matrix(self, mat):
		'''
		Finding the returning possible solutions for the Assignment problem.
		'''

		#Transform the matrix to boolean matrix(0 = True, others = False)
		cur_mat = mat
		zero_bool_mat = (cur_mat == 0)
		zero_bool_mat_copy = zero_bool_mat.copy()

		#Recording possible answer positions by marked_zero
		marked_zero = []
		while (True in zero_bool_mat_copy):
			self.min_zero_row(zero_bool_mat_copy, marked_zero)
		
		#Recording the row and column positions separately.
		marked_zero_row = []
		marked_zero_col = []
		for i in range(len(marked_zero)):
			marked_zero_row.append(marked_zero[i][0])
			marked_zero_col.append(marked_zero[i][1])

		# Determine the non-marked rows and columns
		non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))
		marked_cols = []
		check_switch = True
		while check_switch:
			check_switch = False
			for i in range(len(non_marked_row)):
				row_array = zero_bool_mat[non_marked_row[i], :]
				for j in range(row_array.shape[0]):
					if row_array[j] == True and j not in marked_cols:
						marked_cols.append(j)
						check_switch = True

			for row_num, col_num in marked_zero:
				if row_num not in non_marked_row and col_num in marked_cols:
					non_marked_row.append(row_num)
					check_switch = True

		marked_rows = list(set(range(mat.shape[0])) - set(non_marked_row))
		return(marked_zero, marked_rows, marked_cols)

	def adjust_matrix(self,mat, cover_rows, cover_cols):
		'''
		Adjust the input matrix based on the covered rows and columns.
		'''
      
		cur_mat = mat
		non_zero_element = []

        # Find the minimum non-covered element
		for row in range(len(cur_mat)):
			if row not in cover_rows:
				for i in range(len(cur_mat[row])):
					if i not in cover_cols:
						non_zero_element.append(cur_mat[row][i])
		min_num = min(non_zero_element)

 		# Adjust the matrix by subtracting the minimum non-covered element
		for row in range(len(cur_mat)):
			if row not in cover_rows:
				for i in range(len(cur_mat[row])):
					if i not in cover_cols:
						cur_mat[row, i] = cur_mat[row, i] - min_num
 		# Add the minimum non-covered element to the elements covered twice
		for row in range(len(cover_rows)):  
			for col in range(len(cover_cols)):
				cur_mat[cover_rows[row], cover_cols[col]] = cur_mat[cover_rows[row], cover_cols[col]] + min_num
		return cur_mat

	def hungarian_algorithm(self,mat): 
		'''
		Implementation of the Hungarian Algorithm to solve the Assignment Problem.
		'''
  
		dim = mat.shape[0]
		cur_mat = mat

		#Subtract the minimum value of each row from all elements in that row
		for row_num in range(mat.shape[0]): 
			cur_mat[row_num] = cur_mat[row_num] - np.min(cur_mat[row_num])
		#Subtract the minimum value of each column from all elements in that column
		for col_num in range(mat.shape[1]): 
			cur_mat[:,col_num] = cur_mat[:,col_num] - np.min(cur_mat[:,col_num])
   
		zero_count = 0
  
 	    # Repeat until all zeros are covered
		while zero_count < dim:
			ans_pos, marked_rows, marked_cols = self.mark_matrix(cur_mat)
			zero_count = len(marked_rows) + len(marked_cols)
   
			#Adjust matrix if necessary
			if zero_count < dim:
				cur_mat = self.adjust_matrix(cur_mat, marked_rows, marked_cols)

		return ans_pos

	def cost_calculation(self,mat, pos):
		'''
        Calculate the total cost of the matrix,
        '''
		total = 0
		for i in range(len(pos)):
        	# Add the cost of the chosen element to the total
			total += mat[pos[i][0], pos[i][1]]
    		# Mark the chosen element in the matrix
		return total

	   
	def binary_matrix(self,mat, pos):
		'''
        Generate the binary form of the matrix,
        ''' 
		ans_mat = np.zeros_like(mat)
		for i in range(len(pos)):
			ans_mat[pos[i][0], pos[i][1]] = 1
		return ans_mat