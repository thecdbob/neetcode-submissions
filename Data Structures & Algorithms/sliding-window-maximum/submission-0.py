from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        returnList = []
        r = k - 1
        tempStack = deque()
        for i in range(k):
            tempStack.append(nums[i])
        returnList.append(max(tempStack))
        l = 0
        r = k - 1
        while r < len(nums) - 1:
            r+=1
            l+=1
            tempStack.popleft()
            tempStack.append(nums[r])
            returnList.append(max(tempStack))
        return returnList



