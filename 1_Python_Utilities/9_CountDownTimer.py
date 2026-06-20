import time
while True:
    try:
        seconds=int(input("Enter time in seconds"))
        if seconds<1:
            print("Pleae Enter a Number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid Input , Enter an Whole number")
print("\n 🔔 Time Started....")
for remaining in range(seconds,0,-1):
    mins,secs= divmod(remaining,60)
    time_format=f"{mins:02}:{secs:02}"
    print(f"⏰ Time Left: {time_format} ",end="\r")
    time.sleep(1)
print("\n Times up! Take a break.")
# print("\a") #makes a beep sound