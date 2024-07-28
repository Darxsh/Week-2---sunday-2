def joinStrings(*args):
    # Concatenate all the input strings
    result = ''.join(args)
    return result

input_strings = input("Enter the strings separated by spaces: ")

# Split the input into a list of strings
string_list = input_strings.split()

# Get the concatenated string
result = joinStrings(*string_list)

# Print the result
print("The concatenated string is:", result)
