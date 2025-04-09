'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

1. 트리 만들기
2. 
'''



class Tree:
    def __init__(self,p,c):
        self.p = p
        self.c = c
    def addNode(self, p, c):
        if self.p == None or self.p == p:
            self.p = p
            self.c = Tree(c,None) if c != None else None
            return True
        else :
            if self.c.addNode(p, c) == True:
                return True
            return False
        
# 전위 순회 리스트로 넣기
def preorder(tree):
    result = []
    result.append(tree.index) # 1. 루트 먼저
    if tree.left != None:
        result += preorder(tree.left) # 왼쪽 자식 노드가 있으면 방문
    if tree.right != None:
        result += preorder(tree.right) # 오른쪽 자식 노드가 있으면 방문
    return result

N = int(input())

