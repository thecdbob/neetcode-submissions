from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        l, r = 1, maxSpeed
        bestSpeed = maxSpeed
        while l <= r:
            timeTaken = 0
            m = l + ((r-l)>>1)
            for pile in piles:
                timeTaken += ceil(pile/m)
            if timeTaken <= h:
                bestSpeed = m
                r = m-1
            else:
                l = m+1
        return bestSpeed


        