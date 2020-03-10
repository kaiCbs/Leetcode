class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 0:
            return []
        elif target == 0:
            return [[]]
        if candidates==[]:
            return []
        ans = [[candidates[0]]+i for i in 
                self.combinationSum2(candidates[1:],target-candidates[0])] + self.combinationSum2(candidates[1:],target)
        res = []
        for i in ans:
            i.sort()
            if i not in res:
                res.append(i)
        return res