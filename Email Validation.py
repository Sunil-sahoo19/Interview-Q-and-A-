import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

email_input = input("Enter your email: ")
print(validate_email(email_input))