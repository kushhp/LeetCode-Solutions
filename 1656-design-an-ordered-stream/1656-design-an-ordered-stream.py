class OrderedStream:

    def __init__(self, n: int):
        self.stream = [''] * (n + 1)
        self.i = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        res = []

        while self.stream[self.i]:
            res.append(self.stream[self.i])
            self.i += 1
        
        return res