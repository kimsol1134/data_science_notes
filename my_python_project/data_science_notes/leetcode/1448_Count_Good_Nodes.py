# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, max_node, cnt):
        if root == None:
            return
        else :
            max_node = max(max_node,root.val)
            if max_node == root.val:
                cnt +=1
            self.dfs(root.left, max_node, cnt)
            self.dfs(root.right, max_node, cnt)
        return cnt

    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        max_node =-10000000
        return self.dfs(root, max_node, cnt)
