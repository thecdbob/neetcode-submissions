class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0
        l=0
        charCounts = dict()
        maxValidLength = 0
        mostPopularChar = 0
        for r in range(len(s)):
            charCounts[s[r]] = charCounts.get(s[r], 0) + 1
            mostPopularChar = max(charCounts[s[r]], mostPopularChar)
            windowLength=r-l+1
            if windowLength - mostPopularChar > k:
                charCounts[s[l]] -= 1
                l+=1
            maxValidLength = max(maxValidLength, r-l+1)
        return maxValidLength 

            
