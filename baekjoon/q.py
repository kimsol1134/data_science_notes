import sys

input = sys.stdin.readline
print = sys.stdout.write

class Queue:
    def __init__(self):
        self.q = []
    
    def push(self, n):
        self.q.append(n)

    def pop(self):
        if len(self.q) == 0 :
            return print(-1)
        else :
            return print(self.q.pop(0))
        
    def size(self):
        return print(len(self.q))

    def empty(self):
        if len(self.q) == 0 :
            return print(1)
        else :
            return print(0)
    
    def front(self):
        if len(self.q) == 0 :
            return print(-1)
        else : 
            return print(self.q[0])
    def back(self):
        if len(self.q) == 0 :
            return print(-1)
        else :
            return print(self.q[-1])        
        
n = int(input())
q = Queue()

for _ in range(n):
    a = input().split()

    if a[0] == "push":
        q.push(int(a[1]))
    elif a[0] == "pop":
        q.pop()
    elif a[0] == "size":
        q.size()
    elif a[0] == "empty":
        q.empty()
    elif a[0] == "front":
        q.front()
    elif a[0] == "back":
        q.back()
