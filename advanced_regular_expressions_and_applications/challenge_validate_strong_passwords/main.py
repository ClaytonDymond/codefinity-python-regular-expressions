import re

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
   #     print('Failed length')
        return False
    elif len(re.findall(r'[A-Z]',password)) == 0:
   #     print('Failed capital letters')
        return False
    elif len(re.findall(r'[a-z]',password)) == 0:
   #     print('Failed small letters')
        return False
    elif len(re.findall(r'\d',password)) == 0:
   #     print('Failed digits')
        return False
    elif len(re.findall(f'[^A-Za-z0-9]',password)) == 0:
 #       print('Failed special characters')
        return False
    else:
  #      print(re.findall(f'[^A-Za-z0-9]',password))
  #      print('Passed')
        return True
        
    

print(is_strong_password("Abcdef1!"))
print(is_strong_password("weakpass"))
print(is_strong_password("Abcdefg1"))