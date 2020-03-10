class Solution(object):
    def selfDividingNumbers(self, left, right):
        def isSelfDividing(num):
            for i in str(num):
                if (i=='0') or (num%int(i)):
                    return False
            return True
        return [i for i in range(left,right+1) if isSelfDividing(i)]