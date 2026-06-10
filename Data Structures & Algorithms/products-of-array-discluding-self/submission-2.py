import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first naive solution
        """
        sumNums = [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
        return sumNums
        """
        # second better prefix postfix solution
        """
        finalList, preList, postList = [1] * len(nums), [1]* len(nums), [1]* len(nums)
        for i in range(1,len(nums)):
            preList[i] = preList[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            postList[i] = postList[i+1] * nums[i+1]
        for i in range(len(nums)):
            postList[i] = preList[i] * postList[i]
        return postList
        """
        # third, even less space
        finalList = [1] *len(nums)
        for i in range(1, len(nums)):
            finalList[i] = finalList[i-1] * nums[i-1]
        postFixVal = 1
        for i in range(len(nums)-1, -1, -1):
            finalList[i] = finalList[i] * postFixVal
            postFixVal *= nums[i]
        return finalList

