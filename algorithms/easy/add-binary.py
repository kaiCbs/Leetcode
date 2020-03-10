class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        last = 0
        ans = []
        while (a and b):
            dig_sum = a.pop() + b.pop() + last
            ans.append(str(dig_sum%2))
            last = dig_sum//2
        
        if not (a or b):
            ans.append("1"*last and str(last))
            return "".join(ans[::-1])
        
        if not a:
            a = b
        
        while (a):
            dig_sum = a.pop() + last
            ans.append(str(dig_sum%2))
            last = dig_sum//2
            
        ans.append("1"*last and str(last))
        return "".join(ans[::-1])

# not good