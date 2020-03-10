class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(n):
            now = ''
            if not (i+1)%3:
                now += 'Fizz'
            if not (i+1)%5:
                now += 'Buzz'
            if not now:
                now = str(i+1)
            ans.append(now)
        return ans