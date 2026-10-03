# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def find(node, subNode):
            if not subNode:
                return True

            if not node:
                return False
            
            if match(node, subNode):
                return True
            
            return find(node.left, subNode) or find(node.right, subNode)
            


        
        def match(root, subRoot):

            if not root and not subRoot:
                return True

            if root and subRoot and root.val == subRoot.val:
                return match(root.left, subRoot.left) and match(root.right, subRoot.right)
            
            return False
        
        return find(root, subRoot)





            

