
group=int(input("How may people are there in the group ? :"))
peoples=[]
for i in range(group):
    name=input(f"Enter the name of Person {i+1} : ").strip()
    peoples.append(name)
bill=int(input("What was the Final Bill : "))
Owe = bill/group
print('*'*20)
for i in peoples:
    print(f"{i} Ows {Owe}")
print('*'*20)
