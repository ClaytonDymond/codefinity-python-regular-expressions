import re

def is_valid_phone_number(phone):
    # Your code here
    templist = []
    re.findall(r"\A[0-9]{3}-[0-9]{3}-[0-9]{4}\Z",phone)
    
    if len(re.findall(r"\A[0-9]{3}-[0-9]{3}-[0-9]{4}\Z",phone)) != 0:
        return True
    else:
        return False

print(is_valid_phone_number("123-456-7890"))
print(is_valid_phone_number("1234567890"))
print(is_valid_phone_number("123-45-6789"))
print(is_valid_phone_number("abc-def-ghij"))