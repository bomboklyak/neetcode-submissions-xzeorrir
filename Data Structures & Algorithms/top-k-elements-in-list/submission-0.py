class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            try:
                counter[num] +=1
            except KeyError:
                counter[num] = 1
        sorted_counter = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
        return sorted_counter[:k]