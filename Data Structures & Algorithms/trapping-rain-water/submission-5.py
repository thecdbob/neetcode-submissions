class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        leftPointer = 0
        rightPointer = len(height) - 1
        maxLeft = height[leftPointer]
        maxRight = height[rightPointer]
        totalWater = 0
        # O(n) Complexity
        # O(1) Space
        while  leftPointer < rightPointer:       
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
                maxLeft = max(maxLeft, height[leftPointer])
                totalWater += maxLeft - height[leftPointer]
            else:
                rightPointer -= 1
                maxRight = max(maxRight, height[rightPointer])
                totalWater += maxRight - height[rightPointer]
        return totalWater