# @leet start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min   = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(val)
        else:
            if val < self.min:
                self.stack.append(2*val - self.min)
                self.min = val
            else:
                self.stack.append(val)


    def pop(self) -> None:
        # assuming stack is not empty
        y = self.stack.pop()
        retval = y
        if y < self.min:
            retval = self.min
            self.min = 2*self.min - y
        return retval
        

    def top(self) -> int:
        return max(self.stack[-1], self.min)
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
