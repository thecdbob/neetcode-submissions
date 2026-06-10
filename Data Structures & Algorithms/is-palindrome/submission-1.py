class Solution:
    def isPalindrome(self, s: str) -> bool:
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