class MyRange:
    def __init__(self, start, end, step = 1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += self.step
            return current
        else:
            raise StopIteration()

for i in MyRange(0, 5):
    print(i)

