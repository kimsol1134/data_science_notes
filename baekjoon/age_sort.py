import sys

input = sys.stdin.readline #입력 빠르게 받기

N = int(input())
answer = []
for i in range(N):
    A,B = input().split()
    word = (int(A),B)
    answer.append(word)
answer = sorted(answer, key= lambda x : x[0])

for i in answer:
    print(i[0],i[1])