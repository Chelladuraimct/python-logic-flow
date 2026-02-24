# Stage 3: Student Grade Calculator

# Taking input from User:
name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

# Calculate total
totalMarks = mark1 + mark2 + mark3
# Calculate percentage
percentage = (totalMarks/300) * 100

# Grade logic
if percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "F"

# Display output
print("The Student name is: ", name)
print("Total: ", totalMarks,"/ 300")
print("Percentage: ", percentage, "%")
print("Grade: ", grade)