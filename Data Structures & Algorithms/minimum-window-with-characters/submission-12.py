class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tDict = {}
        minStart, minStop = -1, -1
        minLength = None
        for char in t:
            tDict[char] = tDict.get(char, 0) + 1
        l, r = 0, 0
        sDict = {}
        windowLetters = 0
        requiredLetters = len(tDict)
        while r < len(s):
            sDict[s[r]] = sDict.get(s[r], 0) + 1
            if s[r] in tDict and sDict.get(s[r], 0) == tDict[s[r]]:
                    windowLetters += 1
            while windowLetters == requiredLetters and l <= len(s) - len(t):
                if minLength is not None:
                    if r-l < minStop-minStart:
                        minStart, minStop = l, r
                else:
                    minStart, minStop = l, r
                minLength = minStop-minStart
                if minLength == len(t) -1:
                    return s[minStart:minStop+1]
                sDict[s[l]] = sDict.get(s[l], 0) - 1
                if s[l] in tDict and sDict.get(s[l], 0) < tDict[s[l]]:
                    windowLetters -= 1
                l+=1
            r+=1
        if minLength is None:
            return ""
        else: return s[minStart:minStop+1]




        
