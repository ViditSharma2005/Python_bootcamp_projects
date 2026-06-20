from datetime import datetime as D

def minutes_calc(age):
    year=365.25
    y=D.now().year
    h=D.now().hour
    m=D.now().minute
    days=int(365.25*age)
    hours=int(days*24)
    minutes=int(days*24*60)
    print("--You are --")
    print(f"- {days:,} days old")
    print(f"- {hours:,} hours old")
    print(f"- {minutes:,} minutes old")


while(True):
    umar=int(input("\nEnter yout age : ").strip())
    minutes_calc(umar)
    ask=input("Wanna Continue - (Y/N) : ")
    if ask.upper()!="Y":
        print("Terminating...")
        break