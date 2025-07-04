from collections import deque

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, max_node, cnt):
        if root == None:
            return cnt
        print(f"방문 노드: {root.val}, 현재까지의 max_node: {max_node}, good node 개수: {cnt}")

        max_node = max(max_node,root.val)
        if max_node == root.val:
            cnt +=1
            print(f"-> good node 발견! cnt 증가: {cnt}")
        cnt = self.dfs(root.left, max_node, cnt)
        cnt = self.dfs(root.right, max_node, cnt)
        return cnt

    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        max_node =-10000000
        return self.dfs(root, max_node, cnt)

# 입력 배열 (LeetCode 스타일)
values = [3, 1, 4, 3, None, 1, 5]

# 트리 생성
root = build_tree(values)

# Solution 객체 생성 및 메서드 호출
sol = Solution()
print(sol.goodNodes(root))