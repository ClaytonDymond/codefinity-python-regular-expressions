import re

def extract_hashtags(text):
    pattern = r'(?<!\w)#\w+' 
    return re.findall(pattern, text)

extract_hashtags("#Excited for the #Python3_12 release! #coding #AI #100Day#sOfCode")
