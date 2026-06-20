# string = input("Enter a name = ").strip()

def count(st):
    cha=list(st.lower())
    # unique=list(set(cha))
    uni=[]
    for i in cha:
        if i not in uni:
            uni.append(i)
    print(uni)
    dic={}
    for i in uni:
        c=0
        for j in cha:
            if i == j:
                c+=1
        dic[i]=c
    print(dic)


count("Shristy")
