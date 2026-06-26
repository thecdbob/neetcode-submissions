class TimeMap:

    def __init__(self):
        self.keyStore = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))

                

    def get(self, key: str, timestamp: int) -> str:
        item = self.keyStore.get(key, "")
        if not item:
            return ""
        l, r = 0, len(item) -1
        while l <= r:
            m = l+((r-l)>>1)
            if item[m][0] < timestamp:
                l = m+1
            elif item[m][0] > timestamp:
                r = m - 1
            else:
                return item[m][1]
        if r >= 0:
            return item[r][1]
        return ""
            
