class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [" ", "!", ",", "?", ":", "", "'", "."]
        for t in temp:
            s = s.replace(t, "")
        s = s.lower()
        sLen = len(s)
        for i in range(int(sLen/2)):
            if s[i] != s[sLen-i-1]:
                return False
        return True