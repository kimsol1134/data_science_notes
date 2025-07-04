N = int(input())
f_list = [int(v) for v in input().split()]

if len(f_list) == 1 :
    print(f_list[0]**2)
else :
    f_list = sorted(f_list)
    print(f_list[0]*f_list[-1])