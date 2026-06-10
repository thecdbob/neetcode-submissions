class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        else:
            return False