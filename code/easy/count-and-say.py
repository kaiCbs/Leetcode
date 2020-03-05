class Solution:
    def countAndSay(self, n: int, num="1") -> str:
        if (n==1):
            return num
        else:
            result = ""
            last = num[0]
            group = ""
            splited = []
            for c in num:
                if c==last:
                    group+=c
                else:
                    splited.append(group)
                    group = c
                last = c
            splited.append(group)
            for i in splited:
                result+=str(len(i))
                result+=str(i[0])
            return Solution.countAndSay(self,n-1, num=result)