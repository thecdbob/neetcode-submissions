import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first naive solution
        sumNums = [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
        return sumNums
