class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(i) + 32) if 64 < ord(i) < 97 else i for i in str])