# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global res
        res = True

        def solve(node):
            if not node:
                return 0

            left = solve(node.left)
            right = solve(node.right)
            if abs(left-right)>1:
                global res
                res = False
            return 1 + max(left,right)
        
        solve(root)
        return res

        