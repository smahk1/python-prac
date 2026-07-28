r"""                  Strong Password Detection (using regex)
    Write a function that uses regular expressions to make sure the password
    string it is passed is strong.
    A strong password has several rules:
    It must be at least eight characters long [X] 
    Contains both uppercase and lowercase characters [X] 
    Has at least one digit [X] 
    
    Hint: It’s easier to test the string against
    multiple regex patterns than to try to come up with a single regex that can
    validate all the rules. """

import re
import string

def strength_detector(input_string):
    """ Function that checks the validity and strength of a password. """
    
    # Case 1: Lenth = 8 or not
    if len(input_string) < 8: return "Invalid"
    # Check 2: Both cases or not 
    char_lower_pattern = re.compile(r'[a-z]')
    char_upper_pattern = re.compile(r'[A-Z]') 
    # Check 3: Has atleast one digit 
    digit_pattern = re.compile(r'\d')
    # Extra: Checking special characters, string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    special_char_pattern = re.compile(rf'[{re.escape(string.punctuation)}]')
    
    # Finding the remaining lengths 
    hasLower = bool(re.search(char_lower_pattern, input_string))
    hasUpper = bool(re.search(char_upper_pattern, input_string))
    hasDigit = bool(re.search(digit_pattern, input_string))
    hasSpecialChar = bool(re.search(special_char_pattern, input_string))

    # Validating
    check_passed = 1
    if hasLower and hasUpper: check_passed += 1
    if hasDigit: check_passed += 1
    if hasSpecialChar: check_passed += 1
    
    # Results
    match check_passed:
        case 1:
            return "Weak"
        case 2:
            return "Medium"
        case 3:
            return "Strong"
        case 4:
            return "Extra Strong"

