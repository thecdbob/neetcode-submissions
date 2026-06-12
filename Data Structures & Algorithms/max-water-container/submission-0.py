class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) -1
        area = 0
        while leftPointer < rightPointer:
            height = min(heights[leftPointer], heights[rightPointer])
            width = rightPointer - leftPointer
            if (height * width) > area:
                area = height * width
            
            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            elif heights[leftPointer] > heights[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
                rightPointer -=1
                
        
        return area