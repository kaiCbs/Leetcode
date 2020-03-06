class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            q, p = p, q
        if root:
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                return self.lowestCommonAncestor(root.right, p, q)
            return self.lowestCommonAncestor(root.left, p, q)
        
