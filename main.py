def String_Sum_of_Digits(s : str) -> int:
    '''This function takes a string as input and returns the sum of all the digits in the string.'''
    # Initialize the sum to 0
    sum = 0
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            sum += int(char)
    # Return the sum of the digits
    return sum