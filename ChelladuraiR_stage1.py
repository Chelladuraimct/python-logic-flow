# Stage 1: Basic Calculator

# Taking input from User
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")

#Using if-elif-else
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "x":
    result = num1 * num2

elif operator == "/":
    if num2 ==0:
        print("Error: Division by zero is not allowed.")
        exit()

    else:
        result = num1 / num2

else:
    print("Invalid operator entered.")
    exit()

print(f"You have chosen {operator} operator the result is {result}")



