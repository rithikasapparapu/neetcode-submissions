class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = [float('inf')]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        smaller = min(self.stack[-1], self.stackmin[-1])
        self.stackmin.append(smaller)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stackmin[-1]
        
