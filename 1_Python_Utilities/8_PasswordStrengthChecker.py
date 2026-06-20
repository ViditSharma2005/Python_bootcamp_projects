import string
import random
import getpass

def check_pass(p):
    issues=[]
    if len(p)<8:
        issues.append("Too Short! Minimum 8 characters")
    if not any(c.islower() for c in p):
        issues.append("Missing lowercase letter")
    if not any(c.isupper() for c in p):
        issues.append("Missing uppercase letter")
    if not any(c.isdigit() for c in p):
        issues.append("Missing digits")
    if not any(c in string.punctuation for c in p):
        issues.append("Missing a special character")
    return issues

def generate_pass(length=12):
    chars =  string.ascii_letters + string.digits +string.punctuation

    return "".join(random.choice(chars) for _ in range(length)) 

passw = getpass.getpass("Enter a password - ")

issues= check_pass(passw)
if not issues:
    print("strong password you are good to go")
else:
    print("you have got a weak password")
    for i in issues:
        print(i)

print("\nSuggesting you a strong password")
print(generate_pass())