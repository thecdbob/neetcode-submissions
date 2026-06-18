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
        while r < len(s):
            sDict[s[r]] = sDict.get(s[r], 0) + 1
            while all(sDict.get(char, 0) >= count for char, count in tDict.items()):
                if minLength is not None:
                    if r-l < minStop-minStart:
                        minStart, minStop = l, r
                else:
                    minStart, minStop = l, r
                minLength = minStop-minStart
                sDict[s[l]] = sDict.get(s[l], 0) - 1
                l+=1
            r+=1
        if minLength is None:
            return ""
        else: return s[minStart:minStop+1]




        
