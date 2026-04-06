class Solution:
    def isAnagram(self,  s: str, t: str) -> bool:
        d = [0] * 26
        if len(s) == len(t):

            for i in range(len(s)):
                d[ord(s[i]) - ord('a')] += 1

                d[ord(t[i]) - ord('a')] -= 1
        else: return False
        for u in d:
            if u != 0 :
                return False

        return True

