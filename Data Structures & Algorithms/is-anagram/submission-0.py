class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            s = "".join(sorted(s)).lower()
            t = "".join(sorted(t)).lower()
            return s == t
        else:
            return False