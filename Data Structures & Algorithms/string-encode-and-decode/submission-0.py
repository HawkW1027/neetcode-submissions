class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            length = int(s[i])
            j = i+1
            word = ""
            while j <= i+length:
                word += s[j]
                j += 1
            res.append(word)
            i=j
        return res