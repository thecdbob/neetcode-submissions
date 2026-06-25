class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        rotations = 0
        while l < r:
            m = l +((r-l)>>1)
            rotations +=1 
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] <= nums[r]:
                r = m
        return nums[l]
                