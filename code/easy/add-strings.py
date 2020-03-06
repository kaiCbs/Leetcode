from functools import reduce
class Solution:
    def addStrings(self, num1: str, num2: str, l="0") -> str:
        def int2str(i):
            return chr(i+48)
        def str2int(i):
            return ord(i)-48
        def sumList(l):
            l=list(l)
            if not l:
                return 0
            if len(l)==1:
                return l[0]
            return reduce(lambda x,y:10*x+y,l)
        num1 = sumList(map(str2int,num1))
        num2 = sumList(map(str2int,num2))
        n = num1+num2
        res = []
        while n:
            res.append(int2str(n%10))
            n//=10
        if not res:
            return "0"
        return "".join(res[::-1])

# not good