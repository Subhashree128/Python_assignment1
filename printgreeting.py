name = input("Enter your name: ")
age_input = input("Enter your age (or leave blank to use the default age of 25): ")
if age_input == "":
  age = 25
else:
  age = int(age_input)
print(f"Hello, {name}! You are {age} years old.")

'''Output:
Enter your name: Subhashree
Enter your age (or leave blank to use the default age of 25): 19
Hello, Subhashree! You are 19 years old. '''