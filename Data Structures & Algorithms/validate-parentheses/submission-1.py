class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracketDict = {
            "}" : "{",
            ")": "(",
            "]": "["
        }
        for i in range(len(s)):
            if len(stack) > 0 and bracketDict.get(s[i], "") == stack[-1]:
                stack.pop()
            else:
                if s[i] not in bracketDict.values():
                    return False
                stack.append(s[i])
        if len(stack) > 0:
            return False
        else:
            return True