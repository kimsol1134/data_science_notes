T = int(input())
Q = 25
D = 10
N = 5
P = 1
for i in range(T):
    C = int(input())
    num_Q = C // Q
    C = C % Q
    num_D = C // D
    C = C % D
    num_N = C // N
    C = C % N
    num_P = C //P
    print(num_Q, num_D, num_N, num_P)
