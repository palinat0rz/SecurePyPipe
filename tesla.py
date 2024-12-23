# Vulnerable code: allows arbitrary code execution
user_input = input("Enter a Python expression to evaluate: ")
result = eval(user_input)  # Unsafe use of eval
print(f"The result is: {result}")
