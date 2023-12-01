import numpy as np
import math
import numpy as np
import sqlite3
class Calculator:
    def numeralCalculations(self, expression):
        try:
            result = eval(f"math.{expression}")
            return result
        except Exception as e:
            return f"Error: {e}"
    def calculate_statistics(self, input_string):
        try:
            input_list = input_string.split()
            numbers = np.array([float(x) for x in input_list[:-1]])
            operator = input_list[-1]

            if operator == 'mean':
                result = np.mean(numbers)
                return f"平均值为：{result}"
            elif operator == 'std':
                result = np.std(numbers)
                return f"标准差为：{result}"
            else:
                return "Error: Invalid operator. Please use 'mean' or 'std'."
        except Exception as e:
            return f"Error: {e}"
    def evaluate_matrix_expression(self, expression):
        try:
            expression = expression.replace(" ", "")
            operators1 = ['rank', 'inv', 'adj', 'eigvals', 'eigvecs', 'conj', 'det']
            operators2 = ['+', '-', '*']
            operator = None

            for op in operators1:
                if op in expression:
                    operator = op
                    break

            if operator:
                matrix_str = expression.split(operator)[0]
                matrix = np.array(eval(matrix_str))

                if operator == 'rank':
                    rank = np.linalg.matrix_rank(matrix)
                    return rank
                elif operator == 'inv':
                    inverse = np.linalg.inv(matrix)
                    return inverse
                elif operator == 'adj':
                    adjoint = np.round(np.linalg.det(matrix) * np.linalg.inv(matrix), decimals=2)
                    return adjoint
                elif operator == 'eigvals':
                    eigenvalues = np.linalg.eigvals(matrix)
                    return eigenvalues
                elif operator == 'eigvecs':
                    eigenvalues, eigenvectors = np.linalg.eig(matrix)
                    return eigenvectors
                elif operator == 'conj':
                    result = np.conj(matrix)
                    return result
                elif operator == 'det':
                    result = np.linalg.det(matrix)
                    return result
            else:
                for op in operators2:
                    if op in expression:
                        operator = op
                        break

                if operator:
                    matrix1_str, matrix2_str = expression.split(operator)
                    matrix1 = np.array(eval(matrix1_str))
                    matrix2 = np.array(eval(matrix2_str))

                    if operator == '+':
                        result = matrix1 + matrix2
                    elif operator == '-':
                        result = matrix1 - matrix2
                    elif operator == '*':
                        result = np.dot(matrix1, matrix2)

                    return result
                else:
                    return "Error: Invalid operation."
        except Exception as e:
            return f"Error: {e}"
    def solve_linear_equations(self, augmented_matrix):
        try:
            augmented_matrix = np.array(eval(augmented_matrix))
            coefficients = augmented_matrix[:, :-1]
            constants = augmented_matrix[:, -1]

            solution = np.linalg.solve(coefficients, constants)

            return f"方程组的解为：{solution}"
        except Exception as e:
            return "无解"