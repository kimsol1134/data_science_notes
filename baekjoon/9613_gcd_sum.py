import math
n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    sum = 0

    for i in range(1, num_list[0]+1):
        for j in range(i+1, num_list[0]+1):
            sum += math.gcd(num_list[i],num_list[j])
    
    print(sum)