from datetime import datetime

print("Welcome to your Journal Logger")
text=input("Enter your journal text :\n")
rating=input("Rate yout day outof 10 :")
time=datetime.now().time()
date=datetime.today().date()
text=f"DATE-{date}\nTIME-{time}\n{text}\nYou rated you day as {rating}/10\n"
with open("journal.txt","a+",encoding="utf-8") as file:
    file.writelines(text+"\n")
    print("Added Succesfully")
    