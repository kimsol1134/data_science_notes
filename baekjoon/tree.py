'''
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''
class Tree:
    def __init__(self, i, l ,r):
        self.index = i
        self.left = l
        self.right = r
    
    def addNode(self, i, l, r):
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None
            return True
        else :
            if self.left != None:
                if self.left.addNode(i, l, r) == True :
                    return True
            if self.right != None:
                if self.right.addNode(i, l, r) == True :
                    return True
            return False

def preorder(tree):
    result = []
    result.append(tree.index)
    if tree.left != None:
        result = result + preorder(tree.left)
    if tree.right != None:
        result = result + preorder(tree.right)
    return result

def inorder(tree):
    result = []
    if tree.left != None:
        result = result + inorder(tree.left)
    result.append(tree.index)        
    if tree.right != None:
        result = result + inorder(tree.right)
    return result

def postorder(tree):
    result = []
    if tree.left != None:
        result = result + postorder(tree.left)
    if tree.right != None:
        result = result + postorder(tree.right)
    result.append(tree.index)
    return result

n = int(input())
t = Tree(None,None,None)



for i in range(n) :
    myList = [v for v in input().split()]

    if myList[1] == "." :
        myList[1] = None

    if myList[2] == "." :
        myList[2] = None

    t.addNode(myList[0], myList[1], myList[2])

print("".join(preorder(t)))
print("".join(inorder(t)))
print("".join(postorder(t)))