word = input()

cnt = 0
for w in word :
    if w in ["A","B","C"]:
        cnt+=3
    elif w in ["D","E","F"]:
        cnt+=4
    elif w in ["G","H","I"]:
        cnt+=5
    elif w in ["J","K","L"]:
        cnt+=6
    elif w in ["M","N","O"]:
        cnt+=7
    elif w in ["P","Q","R","S"]:
        cnt+=8
    elif w in ["T","U","V"]:
        cnt+=9
    elif w in ["W","X","Y","Z"]:
        cnt+=10
print(cnt)