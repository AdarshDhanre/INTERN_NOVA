# Task 8: Basic File Handling
name = input("Enter your name: ")
college = input("Enter your college name: ")
branch = input("Enter your branch: ")

introduction = (
    f"My name is {name}. I study at {college}. "
    f"My branch is {branch}. I am learning Python for data analytics."
)

file_name = "my_introduction.txt"

# Create a file and write the introduction
with open(file_name, "w", encoding="utf-8") as file:
    file.write(introduction)

print(f"\nIntroduction successfully written to '{file_name}'.")

# Open the same file and display its contents
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print("\nContents of the file:")
print(content)
