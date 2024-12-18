
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

if __name__ == "__main__":
    increment_counter()  # Counter inside function: 1
    increment_counter()  # Counter inside function: 2
