class Solution:
    def rand10(self):
        a = rand7() * 7 + rand7()
        if a<17:
            return self.rand10()
        return a%10+1