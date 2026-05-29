def print_grade_statistics(grades):
    # Write your code here
    values = list(grades.values())
    average_grade = sum(values) / len(values)
    highest_grade = max(values)
    lowest_grade = min(values)
    
    print("Average grade:", average_grade)
    print("Highest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)

grades = {"Alice": 88, "Bob": 92, "Charlie": 76, "Diana": 85}
print_grade_statistics(grades)
