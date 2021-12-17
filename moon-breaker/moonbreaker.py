'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
.codé en : UTF-8
.langage : python 3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

version = "0.2"

def TtoB(text):
    return(''.join(format(ord(i), '08b') for i in text))

def MakeKey(bina,key):
    basse = 1
    for x in range(2,len(bina)*key + 20):
        basse *= int(bina[x%(len(bina))])+1
    while True:
        if len(str(basse)) > 10: basse //= 10
        elif len(str(basse)) < 10: basse *= 10
        else: break
    return basse
        

def moonbreaker(txt, key = 2):
    return MakeKey(TtoB(txt)+"1",key)

if __name__ == "__main__":
    while True: print(moonbreaker(input("Texte : ")))