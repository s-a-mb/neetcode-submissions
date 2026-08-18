# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# go all the way down the left path to find smallest value
# 3 5 6

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        value = root.val
        i = k

        def dfs(root):
            nonlocal i, value

            if not root:
                return

            dfs(root.left)

            i -= 1

            if i == 0:
                value = root.val

            dfs(root.right)
        
        dfs(root)

        return value
        