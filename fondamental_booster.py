from datetime import datetime


print("Welcome to the Interactive Personal Data Collector!\n")


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print()
print("Thank you! Here is the information we collected:\n")


# Output
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

print()

# Birth Year Calculation
current_year = datetime.now().year
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})\n")

print()
print("Thank you for using the Personal Data Collector. Goodbye!")