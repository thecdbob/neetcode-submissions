class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my naive solution, a bit clumsy
        """
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
        """
        # using the idea that 0s can relate to the keys of letters
        zeroDict = dict()
        # a is 97 in ascii which is just ord('a')
        for word in strs:
            zeroList = [0] * 26
            # zeroList
            for letter in word:
                value = ord(letter) - ord('a')
                zeroList[value] += 1
            tupZeroList = tuple(zeroList)
            #zeroWord = tuple([ord(letter) - ord('a') for letter in word])
            if tupZeroList in zeroDict:
                zeroDict[tupZeroList].append(word)
            else:
                zeroDict[tupZeroList] = list()
                zeroDict[tupZeroList].append(word)
        return list(zeroDict.values())

