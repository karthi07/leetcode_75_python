# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
approach:

maintain queue, 
add elements to queue


"""
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        previous = (root, -1)
        result = []
        while len(queue) > 0:
            current, level = queue.popleft()
            if previous[1] != level:
                result.append(current.val)
            previous = (current, level)
            if current.right:
                queue.append((current.right, level+1))
            if current.left:
                queue.append((current.left, level+1))
        return result
