import re
from functools import reduce

def sum_digits(inputString):
    str_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    try:
        # preprocess input
        inputString = inputString.strip().lower()

        # check if input is empty
        if len(inputString) == 0:
            return "Input cannot be empty. Please enter a value"

        # extract all possible digits
        for str_digit, digit in str_digits.items():
            # count number of occurance of given numerical string
            str_digit_count = inputString.count(str_digit)
            # if count > 0 (found) replace it with its corrsponding digit
            if str_digit_count > 0:
                inputString = inputString.replace(str_digit, digit)
        
        # extract all digits
        digits = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", inputString)

        # if digit is found
        if len(digits) > 0:
            # convert it into its corssponding daat type representation
            digits = [int(d) if d.isdigit() else float(d) for d in digits]
            
            # take summition of digits
            total = reduce(lambda x, y: x + y, digits)

            # return total sum
            return total
        
        else:
            return f"There is no digit Found in '{inputString}'!"

    except (TypeError, AttributeError):
        return f"Input must be a string type, got {type(inputString)}."


print(sum_digits("hello there hi and welcome to 1 and two three four 5 6 7"))
# print(sum_digits("hello there hi and welcome to 1 and two "))
# print(sum_digits("hello there hi and welcome to 1.1 and two minus one "))
print(sum_digits([1, 2, 3, 4]))
print(sum_digits(""))