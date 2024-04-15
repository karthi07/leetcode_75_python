# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
queue = []
dict = {}
1 -> {1:1}

2 -> 7 + 0 {2:7}

"""

from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        maxSum, res, level = float('-inf'), 0, 0
        while len(queue):
            level += 1
            currSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                currSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if maxSum < currSum:
                res = level
                maxSum = currSum
        return res
