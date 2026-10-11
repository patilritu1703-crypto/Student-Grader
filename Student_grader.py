
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

try:
    marks = float(input("Enter marks (0-100): "))

    grade = calculate_grade(marks)

    print("\n===== Result =====")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

    if grade == "F":
        print("Result: Fail")
    elif grade == "Invalid marks":
        print("Please enter marks between 0 and 100.")
    else:
        print("Result: Pass")

except ValueError:
    print("Invalid input! Please enter numeric marks.")
