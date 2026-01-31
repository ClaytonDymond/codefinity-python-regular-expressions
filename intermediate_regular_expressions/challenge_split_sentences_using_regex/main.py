import re

def split_sentences(paragraph):
    pattern = r'[^.!?]+[.!?]'
    result = re.findall(pattern,paragraph, re.DOTALL)
    return [sentence.strip() for sentence in result]

print(split_sentences(" Hello world. How are you? I'm fine! "))
print(split_sentences("First sentence across " + 
                      "multiple lines! Second one."))