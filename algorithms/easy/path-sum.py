class Solution:
    def hasPathSum(self, root: TreeNode, sum1: int) -> bool:
        if root:
            children = [ch for ch in [root.left,root.right] if ch]
            if children:
                return sum([self.hasPathSum(ch,sum1-root.val) for ch in children]) > 0
            else:
                return root.val == sum1
        return False