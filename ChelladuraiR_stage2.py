# Stage 2: Calculator with Result Check

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    else:
        result = num1 / num2

else:
    print("Invalid operator entered.")
    exit()

# Display result
print(f"You have chosen {operator} operator the result is {result}")

# Check if result is positive, negative, or zero
if result > 0:
    print("The result is a Positive value.")

elif result < 0:
    print("The result is a Negative value.")

else:
    print("The result is Zero")