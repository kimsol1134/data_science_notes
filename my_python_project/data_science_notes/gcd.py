def gcd(a, b):
    while b: #b가 0이 될때까지 반복
        a, b = b, a % b 
    return a

import math
math.gcd(a,b)