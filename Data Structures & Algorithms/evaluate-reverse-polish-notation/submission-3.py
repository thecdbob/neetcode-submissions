from functools import reduce

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tempArray = []
        #reduce won't work because operators will process results in order
        for i in range(len(tokens)):
            if tokens[i] in {"+", "-", "/", "*"}:
                symbol = tokens[i]
                right = tempArray.pop()
                left = tempArray.pop()
                if symbol == "+":
                    tempArray.append(left + right)
                elif symbol == "-":
                    tempArray.append(left - right)
                elif symbol == "*":
                    tempArray.append(left * right)
                elif symbol == "/":
                    tempArray.append(int(left/right))
            else:
                tempArray.append(int(tokens[i]))
        return tempArray[0]