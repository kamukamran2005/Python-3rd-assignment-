
# Basic Arithmetic Function
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# Default and Keyword Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    result = calculate(10, 5, '+')
    print(result)  # Output: 15
    greet("Alice")  # Output: Hello, Alice!
    greet("Bob", "Hi")  # Output: Hi, Bob!
