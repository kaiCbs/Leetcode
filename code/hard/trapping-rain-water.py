class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0 ,len(height)-1
        ans = 0
        while i<j-1:
            leftMark, rightMark = height[i], height[j]
            if height[i] <= height[j]:
                i+=1
                while height[i] < leftMark:
                    ans += (leftMark-height[i])
                    i+=1
            else:
                j-=1
                while height[j] < rightMark:
                    ans += (rightMark-height[j])
                    j-=1
        return ans