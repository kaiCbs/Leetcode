class Solution(object):
    def sumOfLeftLeaves(self, root, label=0):
        if not root:
            return 0
        if label and (not (root.left or root.right)):
            return root.val
        else:
            return self.sumOfLeftLeaves(root.left,1)+self.sumOfLeftLeaves(root.right,0)

# not good
            