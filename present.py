def sum_of_digits(number):
    # Initialize sum to 0
    total = 0
    # Loop through each digit in the number (convert number to string)
    for digit in str(number):
        # Add the integer value of the digit to total
        total += int(digit)
    return total

number = int(input("Enter a number: "))
# Get the sum of the digits
result = sum_of_digits(number)
print("The sum of the digits is:", result)
