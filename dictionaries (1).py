
def char_count(string):
    count = {}
    for char in string:
        count[char] = count.get(char, 0) + 1
    return count

students = {
    "Alice": (85, 90, 78),
    "Bob": (88, 94, 86),
    "Charlie": (70, 80, 85),
}

def calculate_averages(students):
    for name, scores in students.items():
        average = sum(scores) / len(scores)
        print(f"{name}: {average:.2f}")

def find_top_student(students):
    top_student = max(students, key=lambda name: sum(students[name]) / len(students[name]))
    return top_student

if __name__ == "__main__":
    print(char_count("hello"))
    calculate_averages(students)
    print("Top student:", find_top_student(students))  # Output: Top student: Bob
