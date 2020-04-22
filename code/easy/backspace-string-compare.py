class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            file = []
            for l in s:
                if l == "#":
                    if file:
                        file.pop()
                else:
                    file.append(l)
            return file

        return helper(S) == helper(T)