from itertools import permutations
n, m = map(int, input().split())

num_list = [int(x) for x in input().split()]
num_list = sorted(num_list)
result = list(permutations(num_list, m))

for w in result :
    print(*w)