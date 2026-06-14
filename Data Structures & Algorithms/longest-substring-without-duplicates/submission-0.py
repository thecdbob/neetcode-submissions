class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 1
        l = 0
        r = 1
        if len(s) < 2:
            return len(s)
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                tempLen = len(s[l:r+1])
                maxLen = max(maxLen, tempLen)
                r+=1
        return maxLen
