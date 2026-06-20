from datetime import date
from functools import wraps

def print_para():
    print(
    f"{name} is {age} years old and currently lives in {city}."
    f"Working as a {profession}, {name} is known for being dedicated and passionate."
    f"In their free time, {name} enjoys {hobby}, which adds a creative and refreshing balance to their daily routine."

    f"\nLogged on {date.today().isoformat()}"
    )
    return None

def my_decor(fun):
    @wraps(fun)
    def wrapper():
        print('*'*20)
        print('*'*20)
        fun()
        print('*'*20)
        print('*'*20+"\n")
    return wrapper
        


name=input("Enter your Name -")
age=input("Enter your Age -")
city=input("Enter your City -")
profession=input("Enter your Profession -")
hobby=input("Enter your Hobby -")

print_para = my_decor(print_para)
print_para()




