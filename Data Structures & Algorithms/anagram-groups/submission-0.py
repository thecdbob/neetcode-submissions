class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs]
        sortedDict = dict()
        for word in strs:                    
            sortedWord = "".join(sorted(word))
            if sortedWord in sortedDict:
                sortedDict[sortedWord].append(word)
            else:
                sortedDict[sortedWord] = list()
                sortedDict[sortedWord].append(word)
        return list(sortedDict.values())