class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        cond1 = (p.val == q.val)
        cond2 = self.isSameTree(p.left,q.left)
        cond3 = self.isSameTree(p.right,q.right)
        return cond1 and cond2 and cond3