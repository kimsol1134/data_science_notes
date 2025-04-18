h, m = map(int,input().split())
c = int(input())

def clock(h,m,c):
    if c+m <60:
        return h ,c+m
    else :
        new_m = (c+m)%60
        new_h = h+(c+m)//60
        if new_h >= 24 :
            new_h = new_h - 24
        return new_h, new_m

result = clock(h,m,c)
print(*result)