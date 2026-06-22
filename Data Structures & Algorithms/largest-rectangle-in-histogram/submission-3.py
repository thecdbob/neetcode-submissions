class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hStack = []
        maxH = 0
        for i in range(len(heights)):
            while hStack and heights[i] < heights[hStack[-1]]:
                lastBuilding = hStack.pop()
                if hStack:
                    width = i - hStack[-1] - 1
                else:
                    width = i
                area = width * heights[lastBuilding]
                maxH = max(maxH, area)
            hStack.append(i)
        i = len(heights)
        while hStack:
            lastBuilding = hStack.pop()
            if hStack:
                width = i - hStack[-1] - 1
            else:
                width = i
            area = width * heights[lastBuilding]
            maxH = max(maxH, area)
        return maxH