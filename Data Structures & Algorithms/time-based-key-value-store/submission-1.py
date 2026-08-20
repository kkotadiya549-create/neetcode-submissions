from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        values = self.keyStore[key]

        # Find insertion position
        i = bisect_right(values, (timestamp, chr(127))) - 1

        if i >= 0:
            return values[i][1]

        return ""