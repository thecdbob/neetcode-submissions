class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        tempStack = []
        for i in range(len(temperatures)):
            while tempStack and temperatures[tempStack[-1]] < temperatures[i]:
                prevIndex = tempStack.pop()
                result[prevIndex] = i - prevIndex
            tempStack.append(i)
        return result

