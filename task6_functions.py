# Task 6: User-Defined Functions

def square(number):
    """Return the square of a number."""
    return number ** 2

def average(first, second, third):
    """Return the average of three numbers."""
    return (first + second + third) / 3

value = float(input("Enter a number to find its square: "))
print(f"Square of {value} = {square(value)}")

a = float(input("\nEnter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print(f"Average = {average(a, b, c):.2f}")
