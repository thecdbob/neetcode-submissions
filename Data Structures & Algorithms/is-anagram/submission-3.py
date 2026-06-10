import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(t) == collections.Counter(s)
        """ better solution
        if len(t) != len(s):
            return False
        sDict = dict()
        for letter in s:
            sDict[letter] = sDict.get(letter, 0) + 1
        for letter in t:
            sDict[letter] = sDict.get(letter, 0) - 1
            if sDict[letter] < 0:
                return False
        return True 
        """


        """ Naive Solution
        return sorted(s) == sorted(t)
        """