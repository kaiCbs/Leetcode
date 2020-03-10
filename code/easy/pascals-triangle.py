class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ans = self.generate(numRows-1)
            l = ans[-1]
            ans.append([1]+[l[i]+l[i+1] for i in range(len(l)-1)]+[1])
            return ans