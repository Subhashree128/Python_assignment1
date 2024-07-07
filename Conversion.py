decimal =int(input("Enter the decimal number:"))
binary =""
while decimal>0:
     binary=str(decimal%2)+binary
     decimal=decimal//2

print("binary equvalence of the given decimal number is:",binary)

'''Output:
    Enter the decimal number:67
    binary equvalence of the given decimal number is: 1000011'''