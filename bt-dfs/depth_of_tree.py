#
#  # Recursion
#  def maxDepth(self, root: Optional[TreeNode]) -> int:      
#        if not root:
#            return 0
#        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#
#


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        depth = 0
        while stack:
            node, currDepth = stack.pop()
            if node:
                depth = max(depth, currDepth)
                if node.left:
                    stack.append([node.left, depth + 1])
                if node.right:
                    stack.append([node.right, depth + 1])
        return depth
