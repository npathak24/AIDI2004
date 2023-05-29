# Key Programming Activities

# 1. Reading input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# 2. Performing a calculation
birth_year = 2023 - age

# 3. Conditional statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

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
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Birth Year: " + str(birth_year) + "\n")

print("Program execution complete.")
