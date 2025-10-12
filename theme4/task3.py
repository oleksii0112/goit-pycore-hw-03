import re
raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "5125",
    "38050 111 22 11   ",
]
def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    phone_number = re.sub(r"[^+\d]", "", phone_number)
    if phone_number.startswith("+380"):
        return phone_number
    elif phone_number.startswith("380"):
        return "+" + phone_number
    elif phone_number.startswith("0"):
        return "+38" + phone_number
    else:
        print (f"its not a phone number: {phone_number}")
sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Normalized phone numbers:", sanitized_numbers)

# не дуже розумію як без колхозу перестати виводи ти None в кінці списку
