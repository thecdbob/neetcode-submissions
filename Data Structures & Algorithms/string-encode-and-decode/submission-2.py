class Solution:
    # Solution #1, the non standard character and the non standard word
    """
    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return "ThisStringDoesntExist"
        encodedString = "é".join(strs)
        return encodedString

    def decode(self, s: str) -> List[str]:
        if s == "ThisStringDoesntExist":
            return []
        decodedList = s.split("é")
        return decodedList
    """
    def encode(self, strs: List[str]) -> str:
        encodedString = "".join(map(lambda x: str(len(x))+"#"+x, strs))
        return encodedString
    def decode(self, s: str) -> List[str]:
        returnList = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            wordLen = int(s[i:j])
            returnList.append(s[j+1:j+1+wordLen])
            i = j + 1 + wordLen
        return returnList
            
            
