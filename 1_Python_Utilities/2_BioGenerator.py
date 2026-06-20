name = input("What is your Name - ").strip()
prof = input("What is your Profession - ").strip()
passion = input("What is your Passion - ").strip()
emo = input("What is your Emoji - ").strip()
site = input("What is your Website - ").strip()
lay= input("\n We have 3 layouts enter which one u want (1 , 2 , 3) - \n")

layout_1= (
    f"{name} | {prof}\n{passion}+{emo}\n🔗 {site}"
)
layout_2 = (
    f"👤 {name}\n"
    f"💼 Profession: {prof}\n"
    f"🔥 Passion: {passion}\n"
    f"💫 Vibe: {emo}\n"
    f"🌐 Portfolio: {site}"
)
layout_3 = (
    f"✨ {name} — {prof}\n"
    f"❤️ Driven by: {passion}\n"
    f"⚡ Energy: {emo}\n"
    f"🔗 Check me out: {site}"
)

if(lay=="1"):
    print(layout_1)
    lay=layout_1
elif(lay=="2"):
    print(layout_2)
    lay=layout_2
elif(lay=="3"):
    print(layout_3)
    lay=layout_3
else:
    print("Invalid Input !!")

user=input("\nDo you want to save this in a file (Y/N) - ").strip().upper()
if user=="Y":
    f_name=f"{name.lower().replace(' ','_')}_bio.txt"
    with open(f_name,"w",encoding="utf-8") as f:
        f.writelines(lay)
        print("SAVED")
else:
    print("No File Created")
