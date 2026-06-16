class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len (s2):
            return False
        letterArrayS1 = [0] * 26
        letterArrayS2 = [0] * 26
        letterConversion = lambda x : ord(x) - ord("a")
        for i in range(len (s1)):
            letterArrayS1[letterConversion(s1[i])] += 1
            letterArrayS2[letterConversion(s2[i])] += 1
        windowSize = len(s1)
        r = windowSize
        while r < len(s2):
            if letterArrayS1 == letterArrayS2:
                return True
            letterArrayS2[letterConversion(s2[r-windowSize])] -= 1
            letterArrayS2[letterConversion(s2[r])] += 1
            r+=1
        return letterArrayS1 == letterArrayS2
            

        
      