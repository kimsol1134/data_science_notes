a,b,n,w = map(int, input().split())
# a 양이 하루 먹는 먹이양, b 염소가 하루 먹는 먹이양, 
# x 양 , y 염소 둘다 1이상

#(a, b)(x)= (w)
#(1, 1)(y)= (n)
#n = x+y 
#w = ax+by

if a == b :
    print(-1)
else :
    x = (w-n*b) / (a-b)
    y = (-w+a*n) / (a-b)
    if x >=1 and int(x) == x :
        if y >=1 and int(y) == y :
            print(int(x),int(y))
    else :
        print(-1)
