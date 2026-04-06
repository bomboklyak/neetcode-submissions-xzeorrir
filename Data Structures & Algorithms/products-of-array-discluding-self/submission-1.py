class Solution:
    def productExceptSelf(self, nums):
        myArray = [1]*len(nums)
        for i in range(len(myArray)):
            for k in range(len(myArray)):
                if i == k:
                    continue
                myArray[i] *= nums[k]
        return myArray