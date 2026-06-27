from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsCombined = sorted(nums1+nums2)
        return median(numsCombined)