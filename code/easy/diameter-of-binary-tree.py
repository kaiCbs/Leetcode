from functools import lru_cache


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        @lru_cache(1000)
        def depth(node):
            if node:
                left, right = depth(node.left), depth(node.right)
                self.res = max(self.res, left + right)
                return max(left, right) + 1
            return 0

        depth(root)
        return self.res