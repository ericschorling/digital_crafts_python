the_matrix_1 = [[1,2],[2,3],[5,6]]
the_matrix_2 = [[2,4],[3,5],[7,8]] 

return_matrix = [[0,0],[0,0],[0,0]]

c_to_r_mat_2 = [[0,0],[0,0]]

for i in range(len(the_matrix_1)):
    for j in range(len(the_matrix_2[0])):
        for k in range(len(the_matrix_2)):
            return_matrix[i][j] += the_matrix_1[i][k] * the_matrix_2[k][j]



print(return_matrix)