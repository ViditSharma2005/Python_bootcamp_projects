l=["apple", "banana", "cherry"]

def long(l):
    c=0
    w=""
    for i in l:
        if len(i)>c:
            c=len(i)
            w=i
    return w

print(f"longest word = {long(l)}")