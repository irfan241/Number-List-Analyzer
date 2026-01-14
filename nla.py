"""
NumberListAnalyzer Program

This program asks the user to enter 5 numbers,
stores them in a list, and then displays:
- all entered numbers
- the total sum
- the maximum value
- the minimum value
"""

# Create an empty list to store user numbers
empty_list = []

# Inform the user about the input requirement
print("Please enter 5 numbers one by one")

# Loop 5 times to take numbers from the user
for i in range(1, 6):
    user_numbers = int(input(f"Enter your number {i}: "))
    empty_list.append(user_numbers)

# Display all numbers entered by the user
print(f"All numbers: {empty_list}")

# Display the sum of all numbers in the list
print(f"Total sum: {sum(empty_list)}")

# Display the maximum number from the list
print(f"Maximum number: {max(empty_list)}")

# Display the minimum number from the list
print(f"Minimum number: {min(empty_list)}")
