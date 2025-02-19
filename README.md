TASK 1
This task demonstrates the use of logical operators (and, or, not) in Python.

Initialization: Age = 30 assigns the integer value 30 to the variable Age.

Logical Expressions and Results:

Result1 = Age > 18 and Age < 65: This checks if Age is greater than 18 and less than 65. Since 30 is within this range, Result1 will be True.
Result2 = Age < 18 or Age > 65: This checks if Age is less than 18 or greater than 65. Since 30 is not in either of these ranges, Result2 will be False.
Result3 = not (Age == 25): This checks if Age is not equal to 25. Since 30 is not 25, Result3 will be True.
Output: The print() statements display the results of each logical expression.

TASK 2
This task takes a number as input from the user and checks if it's both even and positive.

Input: number = int(input('ENTER THE NUMBER : ')) prompts the user to enter a number, converts the input to an integer, and stores it in the number variable.

Conditional Check: if number % 2 == 0 and number > 0: checks two conditions:

number % 2 == 0: Checks if the remainder when number is divided by 2 is 0 (meaning it's even).
number > 0: Checks if the number is greater than 0 (meaning it's positive). Both conditions must be true for the if block to execute.
Output: If both conditions are true, it prints True; otherwise, it prints False.

TASK 3
This task checks if a user is old enough to drive.

Driving Age Limit: driving_licence_limit = 18 sets the minimum driving age to 18.

Input: Age = int(input('ENTER YOUR AGE : ')) prompts the user for their age, converts the input to an integer, and stores it in the Age variable.

Conditional Check: if Age >= driving_licence_limit: checks if the user's age is greater than or equal to the driving age limit.

Output: If the user's age is greater than or equal to 18, it prints "You can drive"; otherwise, it prints "You can't drive".
