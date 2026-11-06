# Task 7: Strings and Collections

# 1. String operations
message = "Python is useful for data analytics"
print("Original string:", message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace Python with SQL:", message.replace("Python", "SQL"))
print("Position of 'useful':", message.find("useful"))


# 2. List operations
marks = [78, 92, 65, 85]
print("\nOriginal list:", marks)
marks.append(88)
print("After append(88):", marks)
marks.remove(65)
print("After remove(65):", marks)
marks.sort()
print("After sort():", marks)

# 3. Tuple creation and indexing
student = ("Riya", 21, "Computer Science")
print("\nTuple:", student)
print("First item:", student[0])
print("Third item:", student[2])

# 4. Dictionary storing student information
student_info = {
    "name": "Riya",
    "roll_no": 101,
    "branch": "Computer Science",
    "marks": 88
}
print("\nStudent dictionary:", student_info)
print("Student name:", student_info["name"])

# 5. Set operations
subjects = {"Python", "SQL", "Excel"}
print("\nOriginal set:", subjects)
subjects.add("Power BI")
print("After add():", subjects)
subjects.remove("Excel")
print("After remove():", subjects)
