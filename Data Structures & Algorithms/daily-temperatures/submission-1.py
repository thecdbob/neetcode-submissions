class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultArray = [0] * len(temperatures)
        tempStack = []
        for i in range(len(temperatures)):
            while tempStack and temperatures[i] > temperatures[tempStack[-1]]:
                popTemp = tempStack.pop()
                resultArray[popTemp] = i-popTemp
            tempStack.append(i)
        return resultArray