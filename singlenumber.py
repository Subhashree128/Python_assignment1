nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
single_number = 0
for num in nums:
    single_number ^= num
print(f"The single number in the array is: {single_number}")

'''Output:
 Enter numbers separated by spaces: 12 5 6 19 23 7
The single number in the array is: 12'''