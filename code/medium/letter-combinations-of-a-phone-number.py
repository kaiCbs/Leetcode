class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
                 '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if not digits: return []
        if len(digits) == 1:
            return list(phone[digits[0]])
        return [i+j for i in phone[digits[0]] for j in 
               self.letterCombinations(digits[1:])]