def increment_array_elements(arr):
    # Increment each element in the array by 1
    incremented_array = [x + 1 for x in arr]
    return incremented_array

input_array = input("Enter a list of integers (without spaces): ")
# Convert input string to a list of integers
array = [int(digit) for digit in input_array]
# Get the incremented array
incremented_array = increment_array_elements(array)
# Print the incremented array
print("".join(map(str, incremented_array)))
