class Solution:
    def twoSum(self, numbers, target):
        index1 = 0
        index2 = 1
        while True:
            tempSum = numbers[index1] + numbers[index2]
            if tempSum == target:
                return [index1+1, index2+1]
            elif tempSum > target:
                index1 += 1
                index2 = index1 + 1
                continue
            index2 += 1
            if index2 > len(numbers) - 1:
                index1 += 1
                index2 = index1 + 1