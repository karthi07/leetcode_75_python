# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leafs):
            if not node:
                return
            if not node.left and not node.right:
                leafs.append(node.val)
                return
            dfs(node.left, leafs)
            dfs(node.right, leafs)
        leafs1, leafs2 = [], []
        dfs(root1, leafs1)
        dfs(root2, leafs2)
        return leafs1 == leafs2
