'''
트리 클래스 만들기
'''
class Node:
    def __init__(self, value):
        self.value = value # 노드 자체의 값
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드

# 노드 만들기
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

# 트리 구조 연결하기
a.left = b
a.right = c
b.left = d
b.right = e

'''
        a
       / \
      b   c
     / \
    d   e
'''

# 전위 순회
def preorder(node):
    if node is None :
        return
    print(node.value)
    preorder(node.left) # 왼쪽 자식 노드 재귀
    preorder(node.right) # 오른쪽 자식 노드 재귀
preorder(a) # A B D E C

# 전위 순회 리스트로 넣기
def preorder(tree):
    result = []
    result.append(tree.index) # 1. 루트 먼저
    if tree.left != None:
        result += preorder(tree.left) # 왼쪽 자식 노드가 있으면 방문
    if tree.right != None:
        result += preorder(tree.right) # 오른쪽 자식 노드가 있으면 방문
    return result


# 이진 트리 만들기
class Tree:
    def __init__(self, i, l, r):
        self.index = i # 노드의 value
        self.left = l
        self.right = r
    def addNode(self, i, l, r):
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None # l이 None 이면 None,None,None 노드 추가되는거 막음
            self.right = Tree(r,None,None) if r != None else None
            return True
        else : #현재 노드가 비어있지 않거나 지금 인덱스랑 다를때 왼쪽 노드부터 탐색
            if self.left != None:
                if self.left.addNode(i, l, r) == True: #좌측노드 인덱스에서 탐색
                    return True
                if self.right.addNode(i, l, r) == True:
                    return True
                return False
    
