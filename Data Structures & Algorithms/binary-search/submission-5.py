from math import log2, ceil

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        count = 0
        counter = ceil(log2(len(nums))) + 1
        i = len(nums)>>1
        jump = len(nums)>>1
        while count < counter:
            i = max(0, min(i, len(nums) - 1))
            jump = max(1, jump >> 1)
            if nums[i] > target:
                i -= jump
            elif nums[i] < target:
                i += jump
            else:
                return i
            count += 1
        return -1
