class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numA = 0
        numB = len(nums)
        numDict = dict()
        for i, item in enumerate(nums):
            difference = target - item
            if difference in numDict:
                return [numDict[difference], i]
            numDict[item] = i
 