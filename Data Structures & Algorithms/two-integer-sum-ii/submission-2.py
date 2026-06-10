class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1
        while leftPointer < rightPointer:
            pointerSum = numbers[rightPointer] + numbers[leftPointer]
            if pointerSum < target:
                leftPointer += 1
            elif pointerSum > target:
                rightPointer -= 1
            elif pointerSum == target:
                return [leftPointer + 1, rightPointer + 1]
        