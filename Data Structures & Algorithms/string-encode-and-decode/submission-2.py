class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for stri in strs:
            res += str(len(stri)) + "#" + stri

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i 
            while s[j] != "#":
                j = j + 1
            res.append(s[j + 1 : j + 1 + int(s[i:j])])
            i = j + 1 + int(s[i:j])
        return res

