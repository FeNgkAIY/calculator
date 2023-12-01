from calculator import Calculator
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
            print(f"{record[0]} -> {record[1]}")
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