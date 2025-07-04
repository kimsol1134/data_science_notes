A = int(input())
B = int(input())
C = int(input())

if A+B+C != 180:
    print("Error")
elif A == B == C == 60 :
    print("Equilateral")
elif A != B and B != C and A !=C:
    print("Scalene")
else :
    print("Isosceles")