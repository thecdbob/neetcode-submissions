class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # brute force solution:
        longestSeq = 0
        setNums = set(nums)
        for i in range(len(nums)):
            candiateSeq = 1
            if not nums[i] - 1 in setNums:
                targetNum = nums[i] + 1 
                while (targetNum) in setNums:
                    candiateSeq += 1
                    targetNum += 1
                if candiateSeq > longestSeq:
                    longestSeq = candiateSeq
        return longestSeq