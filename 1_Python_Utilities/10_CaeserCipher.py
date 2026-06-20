#ceaser cipher
#secret message encrypter and decrypter

def encrypt(message,key):
    result=""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = ((ord(char) - base + key) % 26 + base)
            result+= chr(shifted)
        else:
            result+=char
    return result

def decrypt(message,key):
    return encrypt(message,-key)

sm = "my name is vidit"
en=encrypt(sm,2)
de=decrypt(en,2)
print(en)
print(de)