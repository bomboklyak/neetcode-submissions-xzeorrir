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
                if len(stack) == 0:
                    return False
                if pairs[char] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True