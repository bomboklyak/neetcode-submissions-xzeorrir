class Solution:
    def isAnogram(self,s, t):
        if len(t) == len(s):
            s = "".join(sorted(s))
            t = "".join(sorted(t))
            return s == t
        else:
            return False
    def groupAnagrams(self, strs):
        anograms = []
        for str1 in strs:
            if len(anograms) == 0:
                anograms.append([str1])
                continue
            for a in range (len(anograms)):
                if self.isAnogram(anograms[a][0], str1):
                    anograms[a].append(str1)
                    break
            else:
                anograms.append([str1])
        return anograms