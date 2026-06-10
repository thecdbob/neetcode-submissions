class Solution:
    def isPalindrome(self, s: str) -> bool:
        ### First Solution
        # O(N) Space 
        # O2(N) Complexity
        """
        sAlpha = "".join([char for char in s if char.isalnum()]).lower()
        leftPointer = 0
        rightPointer = len(sAlpha) - 1
        while leftPointer < rightPointer:
            if leftPointer == rightPointer:
                return True
            if sAlpha[leftPointer] != sAlpha[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True
        """
        ### Solution, we want O(1) space
        leftPointer = 0
        rightPointer = len(s) - 1
        while leftPointer < rightPointer:
            while not s[leftPointer].isalnum() and leftPointer < rightPointer:
                leftPointer += 1
            while not s[rightPointer].isalnum() and leftPointer < rightPointer:
                rightPointer -= 1
            if not s[leftPointer].lower() == s[rightPointer].lower():
                return False
            leftPointer += 1
            rightPointer -= 1
            
        return True
            

