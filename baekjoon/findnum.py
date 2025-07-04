import sys

input = sys.stdin.readline

N = int(input())
A = []

A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else :
        print(0)

# 시간초과 뜸 , 트리로 해야할듯??