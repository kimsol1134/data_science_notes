import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
x = int(input())

num_list = sorted(num_list)
num_set = set(num_list)
cnt = 0
for i in num_list:
    if i > x//2 :
        break
    if x != 2*i and x-i in num_set:
        cnt +=1
print(cnt)
