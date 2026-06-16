num = int(input("Enter a number to print the table: "))

print(f"Multiplication table of {num} is: ")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")