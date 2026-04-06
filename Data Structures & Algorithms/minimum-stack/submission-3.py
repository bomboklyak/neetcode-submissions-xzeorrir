class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val):
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)
    def pop(self):
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
        return val
    def top(self):
        return self.stack[-1]
    def getMin(self):
        if not self.minStack:
            return None
        return self.minStack[-1]