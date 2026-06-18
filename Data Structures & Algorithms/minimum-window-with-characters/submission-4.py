class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tDict = {}
        minStart, minStop = -1, -1
        minLength = None
        #populate counts for each in t
        for char in t:
            tDict[char] = tDict.get(char, 0) + 1
        #for this non ideal solution create a dictionary for s
        #but don't populate it until the loop
        
        #iterate through s
        #we are going to just get a O(n^2)*0m solution by double looping
        # don't even include optimizations for the end of the array
        # for - len t, just get it working
        
        l, r = 0, 0
        while l <= len(s) - len(t):
            r = l
            sDict = {}
            while r < len(s):
                sDict[s[r]] = sDict.get(s[r], 0) + 1
                shortestFound = False
                if all(sDict.get(char, 0) >= count for char, count in tDict.items()):
                    if minLength is not None:
                        if r-l < minStop-minStart:
                            minStart, minStop = l, r
                    else:
                        minStart, minStop = l, r
                    minLength = minStop-minStart
                    shortestFound = True
                    break
                if shortestFound == True:
                    break
                r+=1
            l += 1
        if minLength is None:
            return ""
        #may be off by one
        else: return s[minStart:minStop+1]




        
