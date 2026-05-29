def send_notifications(student_grades):
    # Write your code here
    for student, grade in student_grades.items():
        # Set the message variable based on grade
        if grade >= 90:
            message = f"Congratulations {student}, you scored {grade}! Excellent work!"
        elif grade >= 70:
            message = f"Good job {student}, you scored {grade}. Keep it up!"
        else:
            message = f"{student}, you scored {grade}. Let's work together to improve your performance."
        print(message)

grades = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 68,
    "Diana": 74,
    "Evan": 59
}

send_notifications(grades)