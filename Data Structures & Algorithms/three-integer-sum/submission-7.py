class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #naive solution, too slow O(n^3) runtime
        #O(n) space?
        """
        outputSet = set()
        for i in range(len(nums) -2):
            for j in range(i+1, len(nums) -1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        candiateNums = sorted([nums[i], nums[j], nums[k]])
                        outputSet.add(tuple(candiateNums))
        return [list(item) for item in outputSet]
        """
        ### we want O(NlogN runtime)
        # NlogN runtime to sort
        # this logic is wrong in terms of time and this isn't going well
        # come back to this
        # logic in this isn't great; this was terrible
        nums.sort()
        outputList = []
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            leftPointer = i+1
            rightPointer = len(nums) -1
            target = -nums[i]
            while leftPointer < rightPointer:
                if nums[leftPointer] + nums[rightPointer] == target:
                    outputList.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    rightPointer -=1
                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                        leftPointer += 1
                elif nums[leftPointer] + nums[rightPointer] < target:
                    leftPointer += 1
                else:
                    rightPointer -=1
        return outputList
                




