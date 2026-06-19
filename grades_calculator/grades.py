"""
Grade Calculator
-----------------
Asks the user for a number of grades (between 0 and 10 each),
calculates the average, indicates whether the result is a pass
or fail, and shows the highest and lowest grade.
"""

grades_summary = []

# Ask how many grades will be entered, validating it's a positive number
while True:
    num_grades = int(input("How many grades do you want to enter? "))
    if num_grades > 0:
        break
    print("The number of grades must be greater than 0. Try again.")

# Ask for each grade, validating it's within the allowed range (0-10)
for i in range(num_grades):
    while True:
        grade = float(input(f"Enter grade {i+1}: "))
        if 0 <= grade <= 10:
            break
        print("The grade must be between 0 and 10. Try again.")
    grades_summary.append(grade)

# Basic statistics
average = sum(grades_summary) / len(grades_summary)
maximum = max(grades_summary)
minimum = min(grades_summary)

# Results
print(f"The average grade is: {average:.2f}")
if average >= 5:
    print("Passed!")
else:
    print("Failed.")
print(f"The highest grade is: {maximum:.2f}")
print(f"The lowest grade is: {minimum:.2f}")