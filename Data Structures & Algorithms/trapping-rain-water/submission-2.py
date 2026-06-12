class Solution:
    def trap(self, height: List[int]) -> int:
        preList = [0 for _ in range(len(height))]
        maxHeight = 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
            preList[i] = maxHeight
        # can we do this in a way that stores values
        # solve naively first

        #we can solve this tomorrow by cutting out the extra loops
        maxHeight = 0
        total = 0
        #postList = [0 for _ in range(len(height))]
        for i in range(len(height) - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            total += min(preList[i], maxHeight) - height[i]
        #heightList = [0 for _ in range(len(height))]
        #total = 0
        #for i in range(len(height)):
            #total += min(preList[i], postList[i]) - height[i]
        return total
        



