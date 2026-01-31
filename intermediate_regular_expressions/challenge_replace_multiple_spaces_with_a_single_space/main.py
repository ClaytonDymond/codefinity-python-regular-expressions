import re

def normalize_spaces(text):
    return re.sub(r" {2,}"," ",text)

print(normalize_spaces("Hello   world   !"))
print(normalize_spaces("A  B    C     D"))