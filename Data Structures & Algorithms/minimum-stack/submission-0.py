class MinStack:

    stack: List[int]
    minimum: float | int

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum = val
            return
        # The stack stores the running prefix of the value.
        self.stack.append(val - self.minimum)
        if val < self.minimum:
            self.minimum = val
        

    def pop(self) -> None:
        if not self.stack:
            return
        pop: int = self.stack.pop()
        if pop < 0:
            self.minimum -= pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.minimum
        return self.minimum
        

    def getMin(self) -> int:
        return self.minimum
        
