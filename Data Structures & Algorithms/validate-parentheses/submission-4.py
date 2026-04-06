class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack or pairs[char] != stack.pop():
                    return False
        return not stack