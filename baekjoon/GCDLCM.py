A, B = map(int,input().split())

if A>=B :
    for i in range(B,0,-1):
        if A % i == 0 and B % i == 0 :
            GCD = i
            break
    LCM =(A // i)*(B //i) * i
else :
    for i in range(A,0,-1):
        if A % i == 0 and B % i == 0 :
            GCD = i
            break
    LCM =(A // i)*(B //i) * i
print(GCD)
print(LCM)