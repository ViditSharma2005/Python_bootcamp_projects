email = "vidit@gmail.com"

if ' ' in email:
    print("Invalid Email Address")

elif '@' not in email:
    print("Invalid Email Address")

else:
    parts = email.split('@')

    if len(parts) != 2:
        print("Invalid Email Address")

    elif '.' not in parts[1]:
        print("Invalid Email Address")
    
    elif "."in parts[1]:
        dot=len((parts[1]).split('.'))
        print("Valid Email Address") if dot==2 else print("invlid")

    else:
        print("Valid Email Address")
