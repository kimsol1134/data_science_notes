class Stack:
    def __init__(self):
        self.lis = []
    
    def push(self,n):
        self.lis.append(int(n))

    def pop(self):
        if len(self.lis)  == 0:
            return -1
        else :
            return self.lis.pop()
        
    def size(self):
        return (len(self.lis))

    def empty(self):
        if len(self.lis) == 0:
            return 1
        else : 
            return 0
    def top(self):
        if len(self.lis) == 0:
            return -1
        else :
            return self.lis[-1]

n = int(input())
s = Stack()

for _ in range(n):
    a = input().split()

    if a[0] == "push":
        s.push(a[1])
    elif a[0] == "pop":
        s.pop()
    elif a[0] == "size":
        s.size()
    elif a[0] == "empty":
        s.empty()
    elif a[0] == "top":
        s.top()

