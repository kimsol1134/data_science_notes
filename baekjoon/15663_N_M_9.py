from itertools import permutations
n, m = map(int, input().split())

num_list = [int(x) for x in input().split()]

result = list(permutations(num_list, m))
result = list(set(result))
result = sorted(result)

for w in result :
    print(*w)