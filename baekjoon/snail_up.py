import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())

print(math.ceil((V-A)/(A-B)) + 1)

# 하루에 올라가는 높이 A
# 떨어지는 높이 B
# 총 올라가야하는 높이 V

# 하루 총 올라가는 높이 (A-B)*(n-1) + A > V


#10 7 101 하루 3씩 올라가는데 마지막날엔 10
# (101-10) / 3 31 + 1
# V - A = V // (A-B)

#10 8 101 (101-10)/2 올림 45 + 1
