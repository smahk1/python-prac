""" Small program written with regex to extract phone numbers and emails. """
# TODO: Copy text from the clipboard to process it: [X]
# TODO: Once text is extracted extract the email and phone no. through regex: [X]
# TODO: Paste the result to the clipboard: [X]

import pyperclip as clip
import re
import sys
import time

def extractor():
    # Copy to the clipboard
    text = str(clip.paste())
    
    # Regex compiling:            
    email_pattern = email_re = re .compile(r'''(
    [a-z0-9._%+-]+                  # username
    @                               # @ symbol
    [a-z0-9.-]+                     # domain name
    (\.[a-z]{2,4})                  # dot-something
    )''', re.VERBOSE | re.IGNORECASE)

    phone_pattern = re.compile(r'''
    (\d{3})                         # Area code
    (-|\s|\.)                       # space or dash
    (\d{3})                         # First 3 digits
    (-|\s|\.)                       # space or dash
    (\d{4})                         # Final 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension 
    ''', re.VERBOSE)

    # Finding the data
    email_match = email_pattern.findall(text)
    phone_match = phone_pattern.findall(text)
    print(phone_match)
    email = ''
    phone = ''
    for i in range(len(email_match)):
        email = email + email_match[i][0]
        email += '\n'    
    for i in range(len(phone_match)):
        if i + 1 <= len(phone_match):
            for j in range(8):
                phone = phone + phone_match[i][j]
        phone += '\n'
    result = f'Emails found:\n{"".join(email)}\nPhone Numbers found:\n{"".join(phone)}'
    # Paste to the clipboard
    print("Pasted to clipboard:\n" + result)
    clip.copy(result)


""" Refactoring Notes: This code can be written much more cleanly for example by using 
    list comprehensions. There are a few bugs here and there that can be resolved but 
    for a little exercise this is decent I suppose. Much to be improved here.
"""
