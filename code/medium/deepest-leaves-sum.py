class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def next(ls):
            return [p.left for p in ls if p.left] + [p.right for p in ls if p.right]
        last = [p for p in [root] if p]
        res = 0
        while last:
            res = sum([p.val for p in last]) 
            last = next(last)
        return res
            
 