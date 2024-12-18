
# Using len()
def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)

# Using type()
def type_checker(value):
    return type(value)

# Using range()
def sum_of_evens(n):
    return sum(x for x in range(n + 1) if x % 2 == 0)

if __name__ == "__main__":
    print(longest_word(["apple", "banana", "cherry"]))  # Output: ('banana', 6)
    print(type_checker(42))  # Output: <class 'int'>
    print(type_checker("Hello"))  # Output: <class 'str'>
    print(sum_of_evens(10))  # Output: 30
