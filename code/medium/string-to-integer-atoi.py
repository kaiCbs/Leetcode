import re
class Solution:
    def myAtoi(self, str: str) -> int:
        rex = re.match(' *([-+]?\d+)',str)
        if rex:
            value = int(rex.group(1))
            return max(min(value,2**31-1),-2**31)
        else:
            return 0

# See how regular expression make your life much easier.