def print_missing_students(all_students, submitted_students):
    # Write your code here
    missing_students = []
    for student in all_students:
        if student not in submitted_students:
            missing_students.append(student)
            
    print(missing_students)
    pass

# Sample data
all_students = ["Alice", "Bob", "Charlie", "Diana"]
submitted_students = ["Alice", "Diana"]

print_missing_students(all_students, submitted_students)
