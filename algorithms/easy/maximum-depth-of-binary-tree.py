class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if (root.left == root.right == None):
            return 1
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))