class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def seeDepth(node):
            if node:
                a,b = seeDepth(node.left),seeDepth(node.right)
                low = min(a[1],b[1])+1
                high =  max(a[1],b[1])+1
                blc = a[2] and b[2]
                if high-low>1:
                    blc = False
                return low,high,blc
            else:
                return 0,0,True
        return seeDepth(root)[2]