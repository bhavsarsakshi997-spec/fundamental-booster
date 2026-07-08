# Fundamental Booster

 1. Python Module Used
datetime Module

The datetime module is a built-in Python module used for handling dates and time. In this program, the datetime class is imported to retrieve the current year from the system. The current year is later used to calculate the approximate birth year of the user.

Purpose:

Retrieves the current system year.
Helps perform birth year calculation automatically.
Eliminates the need to enter the current year manually.

Syntax:

from datetime import datetime
2. Functions Used
print() Function

The print() function is a built-in output function in Python. It is used to display messages, variables, and calculation results on the screen.

Purpose:

Displays welcome and goodbye messages.
Shows user-entered information.
Displays the calculated birth year.
input() Function

The input() function is a built-in input function used to receive data from the user during program execution. By default, it accepts data as a string.

Purpose:

Collects user information.
Makes the program interactive.
Accepts dynamic values at runtime.
int() Function

The int() function is used for type conversion. It converts a string value into an integer.

Purpose:

Converts the user's age into an integer.
Converts the favourite number into an integer.
Enables arithmetic operations.
float() Function

The float() function converts a string value into a floating-point number.

Purpose:

Converts the height entered by the user into decimal format.
Allows storing fractional values.
type() Function

The type() function returns the data type of a variable or object.

Purpose:

Identifies the type of stored data.
Helps verify whether the value is String, Integer, or Float.
id() Function

The id() function returns the unique memory address (identity) of an object in Python.

Purpose:

Displays the memory location of variables.
Demonstrates how Python stores data in memory.
datetime.now().year

The datetime.now().year statement retrieves the current year from the system date.

Purpose:

Obtains the current year automatically.
Used in calculating the approximate birth year.
3. Data Types Used
String (str)

A String is a sequence of characters enclosed in quotation marks. It is used to store textual information.

Used For:

Name
Integer (int)

An Integer is a whole number without a decimal point.

Used For:

Age
Favourite Number
Current Year
Birth Year
Float (float)

A Float is a numeric data type used to store decimal values.

Used For:

Height


4. Type Casting
Type Casting is the process of converting one data type into another data type.
In this program:

int() converts String into Integer.
float() converts String into Float.

Advantages of Type Casting:
1.Performs mathematical calculations.
2.Prevents data type mismatch.
3.Improves data accuracy.

input image:
<img width="1225" height="875" alt="image" src="https://github.com/user-attachments/assets/c313e414-0a69-48aa-aa6a-5eea0b74d9e7" />

output image:
<img width="897" height="530" alt="image" src="https://github.com/user-attachments/assets/80df4b09-79e8-40ea-8c72-5e47b19d1707" />



5. Operators Used
Arithmetic Operator (-)

The subtraction operator (-) is used to subtract one value from another.

Purpose:

Calculates the user's approximate birth year.

Formula:

Birth Year = Current Year − Age

6. Variables Used

Variables are named memory locations used to store data during program execution.

Variables Used in this Program:

name
age
height
fav_number
current_year
birth_year

Each variable stores a different type of information and is used throughout the program.

7. Formatted String (f-string)

An f-string (formatted string literal) is a feature introduced in Python that allows variables and expressions to be embedded directly inside a string using curly braces {}.

Purpose:

Produces clean and readable output.
Displays variable values without string concatenation.
Improves code readability and efficiency.
8. Memory Management

Python automatically allocates memory to variables when values are assigned. The id() function is used to display the unique memory address of each object stored in memory.

Purpose:

Demonstrates object identity.
Helps understand Python memory allocation.
9. Program Logic

The program follows the following execution flow:

Import the required module.
Display a welcome message.
Collect user information.
Convert input values into appropriate data types.
Display the entered information.
Show the data type and memory address of each variable.
Retrieve the current year.
Calculate the approximate birth year.
Display the final result.
Terminate the program with a thank-you message.

video link:
https://drive.google.com/file/d/137T1YdCOZ2Ze-bQxdtijMQWM7bVljtyI/view?usp=drive_link


