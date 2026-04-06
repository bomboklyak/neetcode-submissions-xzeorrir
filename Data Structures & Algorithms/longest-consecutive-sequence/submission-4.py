class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for el in nums:
            posl = 1
            while True:
                if el+posl in nums:
                    posl += 1
                else:
                    if posl > longest:
                        longest = posl
                    break
        return longest