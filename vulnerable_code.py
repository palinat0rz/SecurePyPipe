import os

# Vulnerable code: using eval (high risk for code injection)
def execute_code(code):
    eval(code)

# Example call
user_input = input("Enter command: ")
execute_code(user_input)

so = 1
