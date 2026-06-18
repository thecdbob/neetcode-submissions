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
        while l < len(s):
            r = l
            sDict = {}
            # we never add 0 right now
            while r < len(s):
                #logic, we basically add an item to the temporary sDict{}
                # then we see if the count in the entire dictionary is above
                # or equal to 
                # t for all items 
                # this is not optimal, the goal is to get this to work first
                # naively
                sDict[s[r]] = sDict.get(s[r], 0) + 1
                if all(sDict.get(char, 0) >= count for char, count in tDict.items()):
                    if minLength is not None:
                        if r-l < minStop-minStart:
                            minStart, minStop = l, r
                    else:
                        minStart, minStop = l, r
                    minLength = minStop-minStart
                    break
                r+=1

                
                #we need to set a bit or break or something to indicate 
                #we didn't meet the condition or we did
            l += 1
        if minLength is None:
            return ""
        #may be off by one
        else: return s[minStart:minStop+1]




        
