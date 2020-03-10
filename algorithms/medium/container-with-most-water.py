class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        ans = (j-i) * min(height[i],height[j])
        while j-i>0:
            if height[i] < height[j]:
                water = height[i]*(j-i)
                i+=1
            else:
                water = height[j]*(j-i)
                j-=1
            if water > ans:
                ans = water
        return ans