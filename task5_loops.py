# Task 5: Loops

# 1. Print numbers from 1 to 20 using a for loop
print("Numbers from 1 to 20:")
for number in range(1, 21):
    print(number, end=" ")
print()

# 2. Multiplication table of a number
table_number = int(input("\nEnter a number for its multiplication table: "))
print(f"Multiplication table of {table_number}:")
for i in range(1, 11):
    print(f"{table_number} x {i} = {table_number * i}")

# 3. Print even numbers from 1 to 50 using a while loop
print("\nEven numbers from 1 to 50:")
number = 2
while number <= 50:
    print(number, end=" ")
    number += 2
print()
