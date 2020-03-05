class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(node1,node2):
            if node1==node2==None:
                return True
            if not (node1 and node2):
                return False
            cond1 = (node1.val == node2.val)
            cond2 = mirror(node1.left,node2.right)
            cond3 = mirror(node1.right,node2.left)
            return cond1 and cond2 and cond3
        if not root:
            return True
        return mirror(root,root)