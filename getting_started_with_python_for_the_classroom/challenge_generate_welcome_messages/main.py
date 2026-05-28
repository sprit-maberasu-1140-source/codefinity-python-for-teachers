def print_welcome_messages(student_names):
    # Write your code here
    for name in student_names:
        message = "Welcome to class," + name + "!"
        print(message)

students = ["Alice", "Ben", "Carlos"]
print_welcome_messages(students)
