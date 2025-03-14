import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCalc")
        self.root.geometry("400x600")
        
        self.equation = ""
        
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.SUNKEN, justify='right')
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('←', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), (')', 4, 3), ('=', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3), ('log', 5, 4),
            ('exp', 6, 0), ('^', 6, 1), ('pi', 6, 2), ('e', 6, 3), ('!', 6, 4)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 14), width=5, height=2,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == "=":
            try:
                expression = self.equation.replace("^", "**").replace("sqrt", "sqrt(") + ")"
                self.equation = str(eval(expression, {"__builtins__": None}, vars()))
            except Exception:
                self.equation = "Error"
        elif char == "C":
            self.equation = ""
        elif char == "←":
            self.equation = self.equation[:-1]
        elif char == "pi":
            self.equation += "pi"
        elif char == "e":
            self.equation += "e"
        elif char == "!":
            try:
                self.equation = str(factorial(int(self.equation)))
            except:
                self.equation = "Error"
        else:
            self.equation += char
        
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
