import re

def mask_credit_card_numbers(text):
    def mask_match(match):
        number = match.group()
        # Remove separators to count digits
        digits = re.sub(r"[ -]", "", number)
        if len(digits) != 16:
            return number  # Not a valid card number, do not mask

        masked = []
        digit_count = 0
        for c in number[::-1]:
            if c.isdigit():
                digit_count += 1
                if digit_count > 4:
                    masked.append('*')
                else:
                    masked.append(c)
            else:
                masked.append(c)

        return ''.join(masked[::-1])
    
    pattern = r'((?:\d{4}[- ]?){3}\d{4})'
    return re.sub(pattern, mask_match, text)

print(mask_credit_card_numbers("Pay with 4111 1111 1111 1111 or 5500-0000-0000-0004 today."))
print(mask_credit_card_numbers("Card: 1234-5678-9012-3456; Backup: 4444 3333 2222 1111."))
print(mask_credit_card_numbers("Not a Card: 1234-5678-9012"))
print(mask_credit_card_numbers("Also not a Card: 1234 5678 9012"))
