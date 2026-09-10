class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ("".join(c for c in s if c.isalnum())).lower()
        h = 0
        b = len(ss)-1
        while h < b:
            if not ss[h] == ss[b]:
                return False
            h += 1
            b -= 1
        return True