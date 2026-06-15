class TimeMap:

    store: dict[List[Tuple[str, int]]]

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            val, ts = values[m]
            if ts <= timestamp:
                result = val
                l = m + 1
            else:
                r = m - 1
        return result
