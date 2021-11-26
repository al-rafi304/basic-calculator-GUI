import tkinter as tk
from tkinter.constants import END

class CalculatorGUI:
    def __init__(self, main):
        self.main = main
        self.main.title('Calculator')
        # Initializing widgets
        self.text = tk.Entry(self.main, width=80, borderwidth=2)
        self.button1 = tk.Button(self.main, text='1', padx=40, pady=20, command=lambda: self.button_click(1))
        self.button2 = tk.Button(self.main, text='2', padx=40, pady=20, command=lambda: self.button_click(2))
        self.button3 = tk.Button(self.main, text='3', padx=40, pady=20, command=lambda: self.button_click(3))
        self.button4 = tk.Button(self.main, text='4', padx=40, pady=20, command=lambda: self.button_click(4))
        self.button5 = tk.Button(self.main, text='5', padx=40, pady=20, command=lambda: self.button_click(5))
        self.button6 = tk.Button(self.main, text='6', padx=40, pady=20, command=lambda: self.button_click(6))
        self.button7 = tk.Button(self.main, text='7', padx=40, pady=20, command=lambda: self.button_click(7))
        self.button8 = tk.Button(self.main, text='8', padx=40, pady=20, command=lambda: self.button_click(8))
        self.button9 = tk.Button(self.main, text='9', padx=40, pady=20, command=lambda: self.button_click(9))
        self.button0 = tk.Button(self.main, text='0', padx=40, pady=20, command=lambda: self.button_click(0))

        self.button_add = tk.Button(self.main, text='+', padx=40, pady=20, command=lambda: self.button_click('+'))
        self.button_sub = tk.Button(self.main, text='-', padx=40, pady=20, command=lambda: self.button_click('-'))
        self.button_mul = tk.Button(self.main, text='*', padx=40, pady=20, command=lambda: self.button_click('*'))
        self.button_div = tk.Button(self.main, text='/', padx=40, pady=20, command=lambda: self.button_click('/'))

        self.button_solve = tk.Button(self.main, text='=', padx=88, pady=50, command=self.solve)
        self.button_clear = tk.Button(self.main, text='Clear', padx=78, pady=20, command=self.clear_button)

        # Rendering widgets
        self.text.grid(row=0, column=0, columnspan=5, ipady=5)

        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.button_div.grid(row=1, column=3)
        self.button_mul.grid(row=1, column=4)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button_add.grid(row=2, column=3)
        self.button_sub.grid(row=2, column=4)

        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        
        self.button_solve.grid(row=3, column=3, rowspan=2, columnspan=2)

        self.button0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)

    
    # Triggers after any number or operator button click
    def button_click(self, num):
        temp_text = self.text.get()
        temp_text += str(num)
        self.text.delete(0, END)
        self.text.insert(0, temp_text)
    
    # Triggers after 'clear' button click
    def clear_button(self):
        self.text.delete(0, END)

    # Triggers after '=' button click
    def solve(self):
        num = self.text.get()
        operators = ['/', '*', '-', '+']
        try:
            num_list = self.create_list(num)
        except SyntaxError:
            self.text.delete(0, END)
            self.text.insert(0, 'Syntax Error')
            return
        check = operators[0]
        i = 0

        # Loop keeps running until every calculation is solved
        while len(num_list) > 1:
            check = operators[i]

            # If i'th operator is found then calculates values around it and updates the list
            if self.getIndex(num_list, check) != False:      
                target = self.getIndex(num_list, check)
                prev = num_list[target-1]
                next =  num_list[target+1]
                cal = self.calculate(prev, next, check)
                num_list[target+1] = cal
                del num_list[target-1:target+1]
            else:
                i += 1
        self.text.delete(0, END)
        self.text.insert(0, str(num_list[0]))

    # Returns index of an item in the list
    def getIndex(self, data, val):
        for index in range(len(data)):
            if data[index] == val:
                return index
        return False

    # Returns calculation of two values based on the operator
    def calculate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        else:
            raise Exception('Syntax Error')

    # Converts a string into a list with appropriate data type
    def create_list(self, string):
        operators = ['/', '*', '-', '+']
        temp = ''
        output = []
        try:
            for char in string:
                if char in operators:
                    output.append(float(temp))
                    output.append(char)
                    temp = ''
                    continue
                temp += char
            output.append(float(temp))
            return list(output)
        except:
            raise SyntaxError



if __name__=='__main__':
    root = tk.Tk()
    app = CalculatorGUI(root)

    root.mainloop()

