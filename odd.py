def print_Odd(N):
    # Print the number 2 first
    print(2)
    # Loop through numbers from 3 to N
    for num in range(3, N + 1):
        # Check if the number is odd
        if num % 2 != 0:
            print(num)

N = int(input("Enter a number: "))
print_Odd(N)
