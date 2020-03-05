class Solution:
    def trailingZeroes(self, n: int) -> int:
        def count5(num):
            if num<5:
                return 0
            return num//5 + count5(num//5)
        return count5(n)