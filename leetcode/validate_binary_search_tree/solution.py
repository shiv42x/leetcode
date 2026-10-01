# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def check(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return check(node.left, left, node.val) and check(node.right, node.val, right)
        
        return check(root, left=float("-inf"), right=float("inf"))

        
            