import matplotlib.pyplot as plt

def plot_grade_barchart(grades_dict):

    
    student_names = list(grades_dict.keys())
    grades = list(grades_dict.values())
    plt.bar(student_names,grades)
    plt.xlabel("Student Name")
    plt.ylabel("Grade")
    plt.title("Class Performance")
    plt.show()

grades = {
    "Alice": 88,
    "Bob": 92,
    "Charlie": 77,
    "Diana": 85,
    "Ethan": 90
}
plot_grade_barchart(grades)
