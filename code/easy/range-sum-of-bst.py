class Solution(object):
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        if root.val > R : return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)