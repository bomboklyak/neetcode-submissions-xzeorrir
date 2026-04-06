class Solution:
    def maxArea(self, heights):
        if len(heights) == 2:
            return min(heights)
        area = 0
        n = len(heights)
        left = 0
        right = left+1
        while left < n-2:
            if right == n:
                left +=1
                right = left + 1
            tempArea = min(heights[left], heights[right]) * abs(left-right)
            if tempArea > area:
                area = tempArea
            right += 1
        return area