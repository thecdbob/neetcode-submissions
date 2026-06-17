class Solution:
    def isValid(self, s: str) -> bool:
        # this solution is not faster than my first solution
        
        stack = list()
        bracketDict = {
            "}" : "{",
            ")": "(",
            "]": "["
        }
        for char in s:
            if char in bracketDict:
                if stack and bracketDict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack