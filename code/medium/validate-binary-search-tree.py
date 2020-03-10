class Solution:
    def isValidBST(self, root: TreeNode, mi = float('-inf'), ma = float('inf')) -> bool:
        if not root:
            return True
        if (root.val >= ma) or (root.val <= mi):
            return False
        return self.isValidBST(root.left,mi,root.val) and self.isValidBST(root.right,root.val,ma)