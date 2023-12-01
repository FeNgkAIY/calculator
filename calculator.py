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


class Interaction:
    def __init__(self,username,database):
        self.calculator = Calculator()
        self.database = database
        self.username = username
    def dispatch(self, input_string):
        try:
            operators1 = ['rank', 'inv', 'adj', 'eigvals', 'eigvecs',']+[', ']-[', ']*[', 'conj', 'det']
            operators2 = ['mean', 'std']
            operator = None
            result = None
            if '[' in input_string:
                input_string = input_string.replace(" ", "")
                for op in operators1:
                    if op in input_string:
                        operator = op
                        break
                if operator:
                    result = self.calculator.evaluate_matrix_expression(input_string)
                    
                else:
                    result = self.calculator.solve_linear_equations(input_string)
                    
            else:
                for op in operators2:
                    if op in input_string:
                        operator = op
                        break
                if operator:
                    result = self.calculator.calculate_statistics(input_string)
                    
                else:
                    result = self.calculator.numeralCalculations(input_string)
            self.database.add_to_history(self.username, input_string, str(result))
            return result
        except Exception as e:
            return f"Error: {e}"
    def show_history(self):
        history = self.database.get_user_history(self.username)
        print("历史记录：")
        for record in history:
            print(f"{record[0]} = {record[1]}")
    def main(self):
        while True:
            input_string = input("请输入您要计算的表达式：")
            if input_string == 'exit':
                break
            elif input_string == 'history':
                self.show_history()
            else:
                result = self.dispatch(input_string)
                print(result)

class MyDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('calculator.db')
        self.cursor = self.conn.cursor()

        self.create_users_table()
        self.create_history_table()

    def create_users_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                               Username TEXT PRIMARY KEY,
                               Password TEXT)''')
        self.conn.commit()

    def create_history_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS HistoryRecord (
                               RecordId INTEGER PRIMARY KEY AUTOINCREMENT,
                               Username TEXT,
                               Calculation TEXT,
                               Result TEXT,
                               FOREIGN KEY (Username) REFERENCES User(Username))''')
        self.conn.commit()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO User (Username, Password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def verify_user(self, username, password):
        self.cursor.execute("SELECT Password FROM User WHERE Username=?", (username,))
        fetched_password = self.cursor.fetchone()
        if fetched_password and fetched_password[0] == password:
            return True
        else:
            return False

    def add_to_history(self, username, calculation, result):
        self.cursor.execute("INSERT INTO HistoryRecord (Username, Calculation, Result) VALUES (?, ?, ?)", (username, calculation, result))
        self.conn.commit()

    def get_user_history(self, username):
        self.cursor.execute("SELECT Calculation, Result FROM HistoryRecord WHERE Username=?", (username,))
        return self.cursor.fetchall()

class Login:
    def __init__(self, database):
        self.db = database
        self.interaction=None

    def add_user(self, username, password):
        self.db.add_user(username, password)

    def log_in(self, username, password):
        if self.db.verify_user(username, password):
            print(f"Welcome, {username}!")
            self.interaction = Interaction(username,self.db)
            self.interaction.main()
        else:
            print("Invalid credentials")
# # 示例用法
# calc = Interaction()

# # numeralCalculations
# result = calc.dispatch("sqrt(2)")
# print(result)

# # calculate_statistics
# numbers = "1 2 3 4 5 mean"
# result = calc.dispatch(numbers)
# print(result)

# # solve_linear_equations
# augmented_matrix = "[[1, 2, 3, 6], [2, -1, 1, 5], [3, 3, 3, 15]]"
# result = calc.dispatch(augmented_matrix)
# print(result)

# evaluate_matrix_expression
# expressions = [
#     "[[1, 2], [3, 4]] rank",
#     "[[1, 2], [3, 4]] inv",
#     "[[1, 2], [3, 4]] adj",
#     "[[1, 2], [3, 4]] eigvals",
#     "[[1, 2], [3, 4]] eigvecs",
#     "[[1, 2], [3, 4]]+[[2, 3], [4, 5]]",
#     "[[1, 2], [3, 4]]-[[2, 3], [4, 5]]",
#     "[[1, 2], [3, 4]]*[[2, 3], [4, 5]]",
#     "[[1, 2], [3, 4]] conj",
#     "[[1, 2], [3, 4]] det"
# ]

# for expr in expressions:
#     result = calc.dispatch(expr)
#     print(f"{expr} = {result}")
# 示例用法
# 示例用法
# 示例用法
# db = MyDatabase()
# login = Login(db)

# # 添加用户和密码
# login.add_user('user1', 'password1')

# # 验证用户
# username_input = 'user1'
# password_input = 'password1'
# login.log_in(username_input, password_input)