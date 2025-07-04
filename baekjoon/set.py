class Set_1:
    def __init__(self):
        self.S = set()
    def add(self, x):
        if x not in self.S:
            self.S.add(x)
    def remove(self, x):
        if x in self.S:
            self.S.remove(x)
    def check(self, x):
        if x in self.S:
            print(1)
        else :
            print(0)
    def toggle(self, x):
        if x in self.S:
            self.S.remove(x)
        else :
            self.S.add(x)
    def all(self):
        self.S = {i for i in range(1,21)}
    def empty(self):
        self.S = set()

S = Set_1()
M = int(input())
for _ in range(M):  
    O_list= input().split()
    if O_list[0] == "add":
        S.add(int(O_list[1]))
    elif O_list[0]== "remove":
        S.remove(int(O_list[1]))
    elif O_list[0] == "check":
        S.check(int(O_list[1]))
    elif O_list[0] == "toggle":
        S.toggle(int(O_list[1]))
    elif O_list[0]== "all":
        S.all()
    elif O_list[0] == "empty":
        S.empty()

