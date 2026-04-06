class Solution:
    def threeSum(self, nums):
        pairs = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i+1, len(nums) - 1
            while left < right:
                tempSum = nums[left] + nums[right]
                if tempSum == target:
                    pairs.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif tempSum > target:
                    right -= 1
                else:
                    left += 1
        return pairs
        