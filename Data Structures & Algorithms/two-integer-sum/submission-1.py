class Solution:
    def twoSum(self, nums, target: int):
        myDict = {}
        for i in range(len(nums)):
            a = myDict.get(target - nums[i], -1)
            if a != -1:
                return [a, i]
            myDict[nums[i]] = i        