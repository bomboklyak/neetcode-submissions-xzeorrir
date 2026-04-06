class Solution:
    def longestConsecutive(self, nums):
        myMap = {}
        startElements = []
        for i, el in enumerate(nums):
            myMap[el] = 1
            if el-1 not in nums:
                startElements.append(el)
        longest = 0
        for startEl in startElements:
            posl = 1
            while True:
                el = myMap.get(startEl+posl, -1)
                if el != -1:
                    posl +=1
                else:
                    if posl > longest:
                        longest = posl
                    break
        return longest