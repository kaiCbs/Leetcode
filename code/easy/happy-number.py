class Solution(object):
    def isHappy(self, n):
        shown = {n}
        while 1:
            n = sum([int(i)**2 for i in str(n)])
            if n==1:
                return True
            elif n in shown:
                return False
            else:
                shown.add(n)