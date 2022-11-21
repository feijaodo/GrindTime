# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ph=root
        while ph:
            if ph.val<p.val and ph.val<q.val:
                ph=ph.right
            elif ph.val>p.val and ph.val>q.val:
                ph=ph.left
            else:
                return ph