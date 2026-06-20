emotions = {
    "happy": "😊",
    "love": "❤️",
    "excited": "🤩",
    "sad": "😢",
    "angry": "😡",
    "surprised": "😲",
    "confident": "💪",
    "proud": "🏆",
    "calm": "😌",
    "nervous": "😬",
    "grateful": "🙏",
    "bored": "😐",
    "motivated": "🔥",
    "confused": "😕",
    "tired": "😴"
}
sentence= input("Enter your Sentence : ")
cont=sentence.split()
emos=emotions.keys()
for i in range(len(cont)):
    if cont[i] in emos:
        cont[i]+=f" {emotions[cont[i]]}"
for j in cont:
    print(f"{j} ",end="")
