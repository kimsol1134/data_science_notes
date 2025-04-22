def find_factor(N):
    f_list = []
    for i in range(1, N):
        if N%i == 0:
            f_list.append(i)
    return f_list

while True:
    N = int(input())
    if N == -1:
        break
    else :
        f_list = find_factor(N)
        if sum(f_list) == N:
            print(N,"=", 1,end="")
            for i in range(1,len(f_list)):
                print(" +", f_list[i], end="")
            print()
        else :
            print(N,"is","NOT","perfect.")