import sys
input = sys.stdin.readline

m,n = map(int, input().split())

password_dict = {}
for _ in range(m):
    domain, password = input().split()
    password_dict[domain] = password

for _ in range(n):
    domain = input().strip()
    print(password_dict[domain])