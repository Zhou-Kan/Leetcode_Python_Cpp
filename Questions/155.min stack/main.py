class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            cur_min = min(val, self.stack[-1][1])
            self.stack.append((val, cur_min))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    

test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)
print(test.stack)
print(test.getMin())
test.pop()
print(test.stack)
print(test.top())
print(test.getMin())