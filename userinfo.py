# Key Programming Activities with Country

# 1. Reading input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

# 2. Performing a calculation
birth_year = 2023 - age

# 3. Conditional statement
if age >= 18:
    status = "adult"
else:
    status = "minor"

# 4. Looping
for i in range(1, 6):
    print("Count:", i)

# 5. Function definition
def greet(name):
    print("Hello, " + name + "!")

# 6. Function call
greet(name)

# 7. File I/O
file_name = "output.txt"
with open(file_name, "w") as file:
    file.write("Country: " + country + "\n")

print("Program execution complete.")
