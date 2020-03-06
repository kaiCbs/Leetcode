class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            if root.left == root.right == None:
                return [str(root.val)]
            return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + [
                    str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        return []