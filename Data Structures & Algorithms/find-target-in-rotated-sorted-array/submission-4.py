class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + ((r-l)>>1)
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] <= nums[r]:
                r = m
        p = l
        l, r = 0, len(nums) - 1
        if nums[p] <= target <= nums[len(nums)-1]:
            l=p
        else:
            r = p-1
        while l <= r:
            p = l + ((r-l)>>1)
            if nums[p] == target:
                return p
            elif nums[p] < target:
                l = p+1
            else:
                r = p - 1
        return -1

