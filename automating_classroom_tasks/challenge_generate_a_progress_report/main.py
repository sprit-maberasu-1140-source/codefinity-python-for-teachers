def generate_progress_report(students, filename):
    report_lines = []
    for student in students:
        name = student["name"]
        grades = student["grades"]
        if grades:
            average = sum(grades) / len(grades)
        else:
            average = 0
        line = f"Student: {name}, Average Grade: {average:.2f}"
        report_lines.append(line)
    with open(filename,"w") as file:
        for line in report_lines:
            file.write(line + "\n")
            
    

students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [70, 75, 80]},
    {"name": "Diana", "grades": []}
]

generate_progress_report(students, "progress_report.txt")
