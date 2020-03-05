class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if target < 0:
            return []
        elif target == 0:
            return [[]]
        if candidates==[]:
            return []
        return [[candidates[0]]+i for i in self.combinationSum(candidates,target-candidates[0])] + self.combinationSum(candidates[1:],target)