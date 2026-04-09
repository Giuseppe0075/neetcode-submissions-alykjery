class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:       
        l = 0
        arr = self.d[key]
        r = len(arr)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m-1
        return res
