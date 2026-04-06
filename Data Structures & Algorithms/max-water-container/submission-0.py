class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        for i in range(n):
            for k in range(n):
                if i == k:
                    continue
                tempArea = min(heights[i], heights[k]) * abs(i-k)
                if tempArea > area:
                    area = tempArea
        return area