A,B,C = map(int,input().split())

def dice(A,B,C):
    if A == B and B== C :
        return (10000 + A*1000)
    elif A==B or A==C:
        return (1000+ A*100)
    elif B==C:
        return (1000+ B*100)
    else :
        return (max(A,B,C)*100)
    

print(dice(A,B,C))
