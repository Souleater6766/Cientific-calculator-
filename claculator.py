# Scientific calculator in Python

import math

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square root")
print("6. Exponential")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)

elif choice == '5':
    num = float(input("Enter a number: "))
    print("Square root of", num, "is", math.sqrt(num))

elif choice == '6':
    num1 = float(input("Enter a base number: "))
    num2 = float(input("Enter an exponent number: "))
    print(num1, "to the power of", num2, "is", math.pow(num1, num2))

elif choice == '7':
    num = float(input("Enter a number: "))
    print("Logarithm of", num, "is", math.log10(num))

elif choice == '8':
    num = float(input("Enter an angle in degrees: "))
    print("Sine of", num, "is", math.sin(math.radians(num)))

elif choice == '9':
    num = float(input("Enter an angle in degrees: "))
    print("Cosine of", num, "is", math.cos(math.radians(num)))

elif choice == '10':
    num = float(input("Enter an angle in degrees: "))
    print("Tangent of", num, "is", math.tan(math.radians(num)))

else:
    print("Invalid input")
