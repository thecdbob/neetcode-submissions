class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #O(NlogN) time to sort the array, reverse to sort by largest to
        #smallest
        sortedCars = sorted(zip(position, speed), reverse=True)
        carStack = []
        for pos, spd in sortedCars:
            time = (target - pos) / spd
            if not carStack or time > carStack[-1]:
                carStack.append(time)
            #if len(carStack) > 1 and time <= carStack[-2]:
                #carStack.pop()
        return len(carStack)

