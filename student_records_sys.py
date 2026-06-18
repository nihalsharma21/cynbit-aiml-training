students = [
    {
        "name": "Ram",
        "id": 1289,
        "age": 22
    },
    {
        "name": "Khushal",
        "id": 3627,
        "age": 18
    },
    {
        "name": "Rahul",
        "id": 1639,
        "age": 20
    }
]

print("Student Records")
for student in students:
    print(f"\nName is: {student["name"]}")
    print(f"Id is: {student["id"]}")
    print(f"Age is: {student["age"]}")