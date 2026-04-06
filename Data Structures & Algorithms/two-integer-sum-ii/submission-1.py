class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            tempSum = numbers[left] + numbers[right]
            if tempSum == target:
                return [left+1, right+1]
            elif tempSum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]