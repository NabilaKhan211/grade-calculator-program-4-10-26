# Student Grade Calculator (Python)

Veda Technology Python Internship — Level 1, Task 4

A Python program that accepts marks for multiple subjects, calculates the total marks and percentage, and assigns a grade based on predefined conditions.

## Objective
Practice conditions, arithmetic operations, and validation.

## Tools
- Python 3 (no external libraries)

## Features
- Takes the student name and marks for 5 subjects: Python, Mathematics, English, Science and Computer (each out of 100)
- Validates marks: only numbers from 0 to 100 are accepted, otherwise the program asks again
- Letters or other invalid input do not crash the program
- Total and percentage are calculated once and reused
- Shows each subject's marks, total, percentage, grade and PASS/FAIL

## How to Run
```bash
python grade_calculator.py
```

## Grade Criteria

| Percentage | Grade | Result |
|------------|-------|--------|
| 90 and above | A+ | PASS |
| 80 – 89.99 | A | PASS |
| 70 – 79.99 | B | PASS |
| 60 – 69.99 | C | PASS |
| 50 – 59.99 | D | PASS |
| 40 – 49.99 | E | PASS |
| Below 40 | F | FAIL |

## Approach
- `get_marks(subject)` asks for the marks of one subject inside a `while True` loop. `try/except ValueError` catches non-numeric input, and an `if 0 <= marks <= 100` check rejects values outside the range. It repeats until the input is valid.
- `calculate_grade(percentage)` uses an `if / elif / else` chain, checked from the highest boundary to the lowest, to return the grade.
- Marks are stored in a dictionary (subject: marks). The total is calculated with `sum(marks.values())` and the percentage as `total / maximum_marks * 100`, both only once.
- The result is printed in a formatted layout using f-strings.

## Sample Student Results

**Student 1**
```
========================================
       STUDENT GRADE CALCULATOR
========================================
Enter student name: Nabila Khan
Enter marks for Python (0-100): 85
Enter marks for Mathematics (0-100): 78
Enter marks for English (0-100): 92
Enter marks for Science (0-100): 66
Enter marks for Computer (0-100): 74

========================================
           STUDENT RESULT
========================================
Student Name : Nabila Khan
Python         : 85.00
Mathematics    : 78.00
English        : 92.00
Science        : 66.00
Computer       : 74.00
----------------------------------------
Total Marks   : 395.00/500
Percentage    : 79.00%
Grade         : B
========================================
Result        : PASS
========================================
```

**Student 2**
```
========================================
       STUDENT GRADE CALCULATOR
========================================
Enter student name: Rahul Verma
Enter marks for Python (0-100): 95
Enter marks for Mathematics (0-100): 88
Enter marks for English (0-100): 91
Enter marks for Science (0-100): 97
Enter marks for Computer (0-100): 90

========================================
           STUDENT RESULT
========================================
Student Name : Rahul Verma
Python         : 95.00
Mathematics    : 88.00
English        : 91.00
Science        : 97.00
Computer       : 90.00
----------------------------------------
Total Marks   : 461.00/500
Percentage    : 92.20%
Grade         : A+
========================================
Result        : PASS
========================================
```

**Student 3: invalid inputs (letters and 105) are rejected, then a failing result**
```
========================================
       STUDENT GRADE CALCULATOR
========================================
Enter student name: Priya Singh
Enter marks for Python (0-100): 35
Enter marks for Mathematics (0-100): abc
Invalid input! Please enter a number.
Enter marks for Mathematics (0-100): 105
Invalid marks! Please enter a value between 0 and 100.
Enter marks for Mathematics (0-100): 40
Enter marks for English (0-100): 30
Enter marks for Science (0-100): 38
Enter marks for Computer (0-100): 32

========================================
           STUDENT RESULT
========================================
Student Name : Priya Singh
Python         : 35.00
Mathematics    : 40.00
English        : 30.00
Science        : 38.00
Computer       : 32.00
----------------------------------------
Total Marks   : 175.00/500
Percentage    : 35.00%
Grade         : F
========================================
Result        : FAIL
========================================
```

## Interview Questions

**1. How would you validate user input?**
Wrap `float(input())` in `try/except ValueError` to catch non-numeric input, then check the range (`0 <= marks <= 100`). Use a `while True` loop so the user is asked again until the input is valid.

**2. How does Python evaluate multiple conditions?**
In an `if / elif / else` chain, Python checks conditions from top to bottom and runs only the first one that is `True`; the rest are skipped. That is why the grade boundaries are checked from highest to lowest. With `and` / `or`, Python stops as soon as the result is known (short-circuit evaluation).

**3. What happens if a user enters a value outside the expected range?**
Without validation, wrong marks (like 105 or -5) would give a wrong percentage and grade. This program prints "Invalid marks!" and asks again until the marks are between 0 and 100.

## Outcome
The program calculates total marks, percentage and grade correctly, and rejects invalid or out-of-range marks instead of giving wrong results.