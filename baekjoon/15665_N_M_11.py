from itertools import product
n, m = map(int, input().split())

num_list = [int(x) for x in input().split()]
num_list = sorted(num_list)
result = list(product(num_list, repeat=m))
result = sorted(list(set(result)))
for w in result :
    print(*w)