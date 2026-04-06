class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)] = res.get(tuple(count),[]) + [s]
        return list(res.values())        