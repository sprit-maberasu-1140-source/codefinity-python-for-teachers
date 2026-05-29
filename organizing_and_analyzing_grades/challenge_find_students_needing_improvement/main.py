def print_students_needing_improvement(grades):
    # Write your code here
    if False:
        student_name = None
        print(student_name)

    for name, grade in grades.items():
        if grade < 70:
            print(name)

grades = {
    "Alice": 85,
    "Bob": 67,
    "Charlie": 92,
    "Diana": 58,
    "Ethan": 74,
    "Fiona": 69
}

print_students_needing_improvement(grades)
