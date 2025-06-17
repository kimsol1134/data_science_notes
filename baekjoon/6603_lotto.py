from itertools import combinations

first_case = True
while True:
    n = input()
    if n == '0' :
        break
    n_list = list(map(int, n.split()))
    n_list = n_list[1:]
    n_list = sorted(n_list)
    result = combinations(n_list, 6)
    if not first_case:
        print()
    first_case = False
    for word in result :
        print(*word)
