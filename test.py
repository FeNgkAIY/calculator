from Login import Login
# # numeralCalculations
# sqrt(2)

# # calculate_statistics
# 1 2 3 4 5 mean

# # solve_linear_equations
# [[1, 2, 3, 6], [2, -1, 1, 5], [3, 3, 3, 15]]

# evaluate_matrix_expression
# 
# [[1, 2], [3, 4]] rank
# [[1, 2], [3, 4]] inv
# [[1, 2], [3, 4]] adj
# [[1, 2], [3, 4]] eigvals
# [[1, 2], [3, 4]] eigvecs
# [[1, 2], [3, 4]]+[[2, 3], [4, 5]]
# [[1, 2], [3, 4]]-[[2, 3], [4, 5]]
# [[1, 2], [3, 4]]*[[2, 3], [4, 5]]
# [[1, 2], [3, 4]] conj
# [[1, 2], [3, 4]] det

login = Login()

# 添加用户和密码
login.add_user('user1', 'password1')

# 验证用户
username_input = 'user1'
password_input = 'password1'
login.log_in(username_input, password_input)

