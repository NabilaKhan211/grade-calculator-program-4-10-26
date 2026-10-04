# Student Grade Calculator
# Veda Technology - Task 4

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} : "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# Get student details
print("=" * 40)
print("       STUDENT GRADE CALCULATOR")
print("=" * 40)

name = input("Enter student name: ")

# Subjects
subjects = ["Python", "Mathematics", "English", "Science", "Computer"]

marks = {}

# Input marks
for subject in subjects:
    marks[subject] = get_marks(subject)

# Calculate total and percentage
total = sum(marks.values())
maximum_marks = len(subjects) * 100
percentage = (total / maximum_marks) * 100

# Calculate grade
grade = calculate_grade(percentage)

# Display result
print("\n" + "=" * 40)
print("           STUDENT RESULT")
print("=" * 40)

print(f"Student Name : {name}")

for subject, mark in marks.items():
    print(f"{subject:<15}: {mark:.2f}")

print("-" * 40)
print(f"Total Marks   : {total:.2f}/{maximum_marks}")
print(f"Percentage    : {percentage:.2f}%")
print(f"Grade         : {grade}")
print("=" * 40)

# Pass/Fail result
if percentage >= 40:
    print("Result        : PASS")
else:
    print("Result        : FAIL")

print("=" * 40)
