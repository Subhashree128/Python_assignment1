a =int(input("Enter your first number :"))
b =int(input("Enter your second number :"))
print(f"Before swapping the numbers: first number = {a}, second number = {b}")
a = a+b
b = a-b
a = a-b
print(f"After swapping the numbers: first number = {a}, second number = {b}")

'''Output:
    Enter your first number :56
Enter your second number :98
Before swapping the numbers: first number = 56, second number = 98
After swapping the numbers: first number = 98, second number = 56'''