from itertools import permutations

n = int(input())

n_list = [int(x) for x in range(1, n+1)]

per_list = permutations(n_list, n)

for i in per_list:
    print(*i)