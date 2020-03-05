class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        size = len(nums)
        if size==0:
            return None
        if size==1:
            return TreeNode(nums[0])
        elif size==2:
            rt = TreeNode(nums[1])
            rt.left = TreeNode(nums[0])
            return rt
        else:
            rt = TreeNode(nums[size//2])
            rt.left = self.sortedArrayToBST(nums[:size//2])
            rt.right = self.sortedArrayToBST(nums[size//2+1:])
            return rt