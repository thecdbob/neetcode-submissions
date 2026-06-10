import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # O n log n
        # n space
        sortedDict = dict()
        for number in nums:
            if number in sortedDict:
                sortedDict[number] += 1
            else:
                sortedDict[number] = 1
        # n space
        sortedList = list()
        for key, value in sortedDict.items():
            sortedList.append((key, value))
        #sortedList.sorted()
        for i in range(len(sortedList)):
            j = i
            while j > 0 and sortedList[j-1][1] > sortedList[j][1]:
                temp = sortedList[j]
                sortedList[j] = sortedList[j-1]
                sortedList[j-1] = temp
                j = j-1
        return [value[0] for value in sortedList[-k:]]
        """
        # sorting the list in place might have exactly the same solution as what we have here
        # but without the dictionary which just adds computational complexity

         # O n log n
        # n space
        """
        sortedDict = dict()
        for number in nums:
            if number in sortedDict:
                sortedDict[number] += 1
            else:
                sortedDict[number] = 1
        # n space
        letterFrequency = [[] for i in range(len(nums) + 1)]
        for key, value in sortedDict.items():
            letterFrequency[value].append(key)
        #sortedList.sorted()
        numList = list()
        for i in range(len(letterFrequency) -1, 0, -1):
            for number in letterFrequency[i]:
                numList.append(number)
                if len(numList) == k:
                    return numList
        """
        ### Implimenting the solution that uses heaps
        sortedDict = {}
        for number in nums:
            sortedDict[number] = 1 + sortedDict.get(number, 0)
        returnNums = []
        for number, quantity in sortedDict.items():
            if len(returnNums) < k:
                heapq.heappush(returnNums, (quantity, number))
            else:
                heapq.heappushpop(returnNums, (quantity, number))
            #if len(returnNums) > k:
                
                #heapq.heappop(returnNums)
        return [item[1] for item in returnNums]

