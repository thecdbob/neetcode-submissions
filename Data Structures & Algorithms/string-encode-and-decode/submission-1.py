class Solution:

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
