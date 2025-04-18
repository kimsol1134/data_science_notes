import sys

input = sys.stdin.readline

N= int(input())
N_card = [int(v) for v in input().split()]

M = int(input())
M_card = [int(v) for v in input().split()]

for i in M_card :
    print(N_card.count(i), end=" ")