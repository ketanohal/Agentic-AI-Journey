#variable is a named container used to store data in memory.
name = "ketan"

#basic data types in python
#1. int - integer data type
age = 25

#2. float - floating point data type
height = 5.9

#3. str - string data type
city = "New York"

#4. bool - boolean data type
is_student = True


# print(name)

#checking type of variable

# print(type(name))

#user input
# name = input("Enter the username: ")
# Everything entered through input() is a string.
# age = int(input("Enter your age: "))
# print(type(age))
# print(type(name))

#Instead of:
# name = "Ketan Ohal"
# print("Hello " + name)

# Assignment 1

# Create a program that asks:

# Name
# Age
# City
# Current Company

# Output:

# Employee Details

# Name: Ketan
# Age: 27
# City: Pune
# Company: Technosys

empname = input("Enter your name: ")
empage = int(input("Enter your age: "))
empcity = input("Enter your city: ")
empcompany = input("Enter your current company name: ")

print("\nEmployee Details")
print(f"Name: {empname}")
print(f"Age: {empage}")       # Added f-string formatting
print(f"City: {empcity}")       # Added f-string formatting
print(f"Company: {empcompany}") # Added f-string formatting
