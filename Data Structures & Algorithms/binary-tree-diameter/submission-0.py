# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x = 0
        def dfs(root):
            nonlocal x
            if not root: return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            x = max(x, left[0] + right[0] + 1)
            return [max(left[0], right[0]) + 1, x]
        return max(dfs(root)[0], dfs(root)[1]) - 1
        