#friedship calculator
def compatibility(name1,name2):
    name1,name2 = name1.lower(),name2.lower()
    score =0
    shared_letters = set(name1) & set(name2)
    vowels = set("aeiou")
    score += len(shared_letters)*5
    score += len(vowels & shared_letters)*10
    return min(score,100)  # very good use .. think goo on this , return and and see this is good😏

def run_friendship_calculator():
    print("💖 Friendship Compatibility Calculator")
    name1=input("Enter name 1: ")
    name2=input("Enter name 2: ")
    score= compatibility(name1,name2)
    print(f"\n{score}")
run_friendship_calculator()
