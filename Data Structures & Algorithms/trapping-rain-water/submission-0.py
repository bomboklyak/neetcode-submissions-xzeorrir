class Solution:
    def trap(self, height):
        print(height)
        left = []
        right = []
        for i in range(len(height)):
            if i == 0:
                left.append(0)
                right.append(max(height))
                continue
            if i == len(height) - 1:
                left.append(max(height[:i]))
                right.append(0)
                continue
            left.append(max(height[:i]))
            right.append(max(height[i+1:]))
        area = 0
        for i in range(len(height)):
            a = min(left[i], right[i]) - height[i]
            if a > 0:
                area += a
        return area