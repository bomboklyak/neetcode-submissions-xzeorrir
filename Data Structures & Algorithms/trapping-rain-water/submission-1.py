class Solution:
    def trap(self, height):
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = 0
        for i in range(1, len(height)):
            left_max[i] = max([left_max[i-1], height[i-1]])

        right_max[-1] = 0
        for i in range(n-2, 0, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        area = 0
        for i in range(len(height)):
            a = min(left_max[i], right_max[i]) - height[i]
            if a > 0:
                area += a
        return area