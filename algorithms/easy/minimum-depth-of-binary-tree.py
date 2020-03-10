class Solution:
    def minDepth(self, root: TreeNode, flag=1) -> int:
        if root:
            if not (root.left or root.right):
                return 1
            return min([self.minDepth(leaf) for leaf in [root.left,root.right] if leaf])+1
        else:
            return 0